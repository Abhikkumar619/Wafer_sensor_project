from wafer_project.utils.common import read_yaml, create_directories
from wafer_project.constant import *
from wafer_project.entity.config_entity import (DataIngestionConfig, DataTransformationConfig, ModelTrainerConfig)




class ConfigurationManager: 
    def __init__(self, config_file_path=CONFIG_FILE_PATH,
                 params_file_path=PARAMS_FILE_PATH,
                 schema_file_path=SCHEMA_FILE_PATH
                 ): 
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        self.schema=read_yaml(schema_file_path)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
         
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            data_source=config.data_source,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            data_to_store=config.data_to_store)
        
        return data_ingestion_config
    
    def get_data_transformation_config(self)-> DataTransformationConfig: 
        
        config=self.config.data_transformation
        create_directories([config.root_dir])
        
        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            preprocessor_obj_file=config.preprocessor_obj_file,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            scaled_train_data=config.scaled_train_data,
            scaled_test_data=config.scaled_test_data
        )
        
        return data_transformation_config  
    
    def get_model_trainer_config(self)-> ModelTrainerConfig: 
        config=self.config.model_trainer
        create_directories([config.root_dir])
        
        model_trainer_config=ModelTrainerConfig(
            root_dir=config.root_dir, 
            model_path=config.model_path,
            model_yaml=config.model_yaml,
            train_arr_path=config.train_arr_path,
            test_arr_path=config.test_arr_path
            
        )
        return model_trainer_config