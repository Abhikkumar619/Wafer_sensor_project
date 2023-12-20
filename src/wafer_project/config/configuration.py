from wafer_project.utils.common import read_yaml, create_directories
from wafer_project.constant import *
from wafer_project.entity.config_entity import DataIngestionConfig




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