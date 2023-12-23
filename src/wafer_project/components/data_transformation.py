import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.combine import SMOTETomek # Handling the imbalance dataset
from sklearn.compose import ColumnTransformer
from wafer_project.entity.config_entity import DataTransformationConfig
from wafer_project import logger




class DataTransformation: 
    def __init__(self, config=DataTransformationConfig):
        self.config=config
       
    def get_data_transformation_object(self, NUM_C): 
        try: 
            num_pipeline=Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='mean')),
                ('scaler', StandardScaler())
            ]
                
            )
            
            preprocessor=ColumnTransformer([('num_pipeline', num_pipeline, NUM_C)])
            return preprocessor
            
        except Exception as e: 
            raise e 
         
    def initiate_data_transformation(self): 
        try: 
            train_path=self.config.train_data_path
            test_path=self.config.test_data_path
            
            target_column_name='Good/Bad'
            
            train_data=pd.read_csv(train_path)
            # logger.info(f"Train data from Data Transformation: {train_data.head(2)}\n\\n\n\n")
            
            test_data=pd.read_csv(test_path)
            # logger.info(f"Test data from Data Transformation: {test_data.head(2)}\n\n\n")
            
            # Training dataframe
            input_feature_train_df=train_data.drop(columns=[target_column_name], axis=1)
            target_feature_train_df=np.where(train_data[target_column_name]==-1,0,1)
            
            # logger.info(f"Input feature train_df : {input_feature_train_df.head(2)}")
            # logger.info(f"targer features train df: {target_feature_train_df}")
            
            
            # Testing dataframe
            input_feature_test_df=test_data.drop(columns=[target_column_name], axis=1)
            target_feature_test_df=np.where(test_data[target_column_name]==-1,0, 1)
            
            # logger.info(f"Input features for test_df: {input_feature_test_df.head(2)}")
            # logger.info(f"Target features for test_df: {target_feature_test_df}")
            
            
            num_col=[col for col in input_feature_train_df.columns if input_feature_train_df[col].dtype != "O" ]
            logger.info(f"Numerical col : {num_col}")
            
            
            
            preprocessor=self.get_data_transformation_object(num_col)
            logger.info(f"Preprocessor Pipeline is created: {preprocessor}")
            
            
            

            # Scaling the x_train, x_test
            x_train_scaled=preprocessor.fit_transform(input_feature_train_df)
            
            x_train_scaled_df=pd.DataFrame(x_train_scaled, columns=preprocessor.get_feature_names_out())
            
            
            
            x_test_scaled=preprocessor.fit_transform(input_feature_test_df)
            x_test_scaled_df=pd.DataFrame(x_test_scaled, columns=preprocessor.get_feature_names_out())
            # logger.info(f"x_test_scaled df: {x_test_scaled_df.head()}")
            
            
            
            
            
            target_df=pd.DataFrame(np.array(target_feature_train_df), columns=['Good/Bad'])
            target_df2=pd.DataFrame(np.array(target_feature_test_df), columns=['Good/Bad'])
            # logger.info(f"target_dataframe: {target_df}")
            
            train_arr=pd.concat([x_train_scaled_df, target_df], axis=1)
            test_arr=pd.concat([x_test_scaled_df, target_df2], axis=1)
            
            train_arr.to_csv(self.config.scaled_train_data, index=False, header=True)
            test_arr.to_csv(self.config.scaled_test_data, index=False, header=True) 
            # logger.info("train arr saved")
            
            # logger.info(f"train arr Datafrae: {train_arr}")
            
        except Exception as e: 
            raise e
        