import os,sys
from flask import request
from wafer_project.utils.common import load_object
from pathlib import Path
from wafer_project import logger
import pandas as pd
from dataclasses import dataclass

@dataclass
class PredictionPipelineConfig: 
    prediction_output_dirname: str="predictions"
    prediction_file_name: str="predicted_file.csv"
    prediction_file_path:str= os.path.join(prediction_output_dirname,prediction_file_name )
    


class PredictPipeline:
    def __init__(self, request: request): 
        self.request=request
        self.prediction_pipeline_config=PredictionPipelineConfig()
    
    def save_input_files(self): 
        try: 
            pred_file_input_dir="Prediction_artifacts"
            os.makedirs(pred_file_input_dir, exist_ok=True)
            
            input_csv_file=self.request.files['file']
            
            pred_file_path=os.path.join(pred_file_input_dir, input_csv_file.filename)
            
            input_csv_file.save(pred_file_path)
            
            return pred_file_path
        except Exception as e:
            raise e
        
        
    def predict_model(self, features): 
        try: 
            model=load_object(file_path=Path('artifacts\model_trainer\model.pkl'))
            preprocessor=load_object(file_path=Path('artifacts\data_transformation\preprocessor.pkl'))
            logger.info(f"Model and preprocessor loaded sucessfully")

            transform_features=preprocessor.transform(features)
            
            pred=model.predict(transform_features)
            
            return pred
            
            
            
        except Exception as e: 
            raise e
        
    def get_predicted_dataframe(self, input_dataframe_path: Path): 
        try: 
            prediction_column_name: str="GOOD/Bad"
            input_dataframe=pd.read_csv(input_dataframe_path)
            input_dataframe=input_dataframe.drop(columns="Unnamed: 0") if "Unnamed: 0" in input_dataframe.columns else input_dataframe
            
            predictions=self.predict_model(input_dataframe)
            
            input_dataframe[prediction_column_name]=[pred for pred in predictions]
            
            target_column_mapping={0:'bad', 1: 'good'}
            input_dataframe[prediction_column_name]=input_dataframe[prediction_column_name].map(target_column_mapping)
            
            os.makedirs(self.prediction_pipeline_config.prediction_output_dirname ,exist_ok=True)
            input_dataframe.to_csv(os.path.join(self.prediction_pipeline_config.prediction_file_path), index=False)
            logger.info("prediction completed")
            
        except Exception as e: 
            raise e
        
        
    def run_pipeline(self): 
        try: 
            input_csv_file=self.save_input_files()
            logger.info(f"Input csv file {input_csv_file}")
            self.get_predicted_dataframe(Path(input_csv_file))
            
            return self.prediction_pipeline_config
        except Exception as e: 
            raise e
            
        