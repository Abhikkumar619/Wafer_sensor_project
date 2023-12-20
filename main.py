
from wafer_project import logger
from wafer_project.pipeline.stage_01_data_ingestion import DataIngestionPipeline




stage_name="Data_Ingestion"
try:
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Data {stage_name} Started>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Data {stage_name} End>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
except Exception as e: 
    raise e