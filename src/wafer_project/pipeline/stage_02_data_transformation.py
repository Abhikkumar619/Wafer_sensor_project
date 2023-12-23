from wafer_project.config.configuration import ConfigurationManager
from wafer_project.components.data_transformation import DataTransformation
from wafer_project import logger

stage_name="Data_Transfromation_stage"

class DataTransformationPipeline: 
    def __init__(self): 
        pass
    def main(self): 
        try: 
            configManager=ConfigurationManager()
            data_transformation_config=configManager.get_data_transformation_config()
            data_transformation=DataTransformation(data_transformation_config)
            data_transformation.initiate_data_transformation()
        except Exception as e: 
            raise e
        
if __name__ == "__main__": 
    try: 
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {stage_name} Started>>>>>>>>>>>>>>>>>>>>>>>>>")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    except Exception as e: 
        raise e