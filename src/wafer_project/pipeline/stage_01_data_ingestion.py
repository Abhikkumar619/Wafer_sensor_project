
from wafer_project import logger
from wafer_project.config.configuration import ConfigurationManager
from wafer_project.components.data_ingestion import DataIngestion


stage_name="Data_Ingestion"


class DataIngestionPipeline:
    def __init__(self): 
        pass
    
    def main(self): 
        try: 
            config_manager=ConfigurationManager()
            ingestion_config=config_manager.get_data_ingestion_config()
            dataIngestion=DataIngestion(ingestion_config)
            dataIngestion.initiate_data_ingestion()
        except Exception as e: 
            raise e
        
        
        
if __name__=="__main__": 
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Data {stage_name} Started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Data {stage_name} End>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e