import pandas as pd
import numpy as np
from wafer_project import logger
from sklearn.model_selection import train_test_split
from wafer_project.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion: 
    def __init__(self, config=DataIngestionConfig): 
        self.config=config
        
    def initiate_data_ingestion(self): 
        try: 
            path=Path("Data\wafer_dataset.csv")
            data=pd.read_csv(path)
            logger.info(f"Dataset : {data.head(2)}")
            data=data.drop("Unnamed: 0", axis=1)
            logger.info(f"Deleting the column-- Unnamed: 0")
            
            data.to_csv(self.config.data_to_store, index=False, header=True)
            
            (train_data, test_data)=train_test_split(data, test_size=0.2, random_state=42)
            
            train_data.to_csv(self.config.train_data_path, index=False, header=True)
            logger.info(f"Train data {train_data.head(2)}")
            
            test_data.to_csv(self.config.test_data_path, index=False, header=True)
            logger.info(f"Test data {test_data.head(2)}")
            
        except Exception as e: 
            raise e
        