
from wafer_project import logger
from wafer_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from wafer_project.pipeline.stage_02_data_transformation import DataTransformationPipeline
from wafer_project.pipeline.stage_03_model_trainer import ModelTrainerPipeline


"""
stage_name="Data_Ingestion"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Data {stage_name} Started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Data {stage_name} End>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
    raise e

"""
stage_name="Data_Transfromation_stage"


try: 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {stage_name} Started>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
    raise e

stage_name= "Model_Trainer"

if __name__ == '__main__': 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    try: 
        obj=ModelTrainerPipeline()
        obj.main()
    except Exception as e: 
        raise e
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    