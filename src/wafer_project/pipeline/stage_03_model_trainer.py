from wafer_project.config.configuration import ConfigurationManager
from wafer_project.components.Model_Trainer import ModelTrainer
from wafer_project import logger



stage_name= "Model_Trainer"

class ModelTrainerPipeline: 
    def __init__(self): 
        pass
    def main(self): 
        try: 
            configmanager=ConfigurationManager()
            config_model_config=configmanager.get_model_trainer_config()
            model_trainer=ModelTrainer(config_model_config)
            model_trainer.initate_model_trainer()
        except Exception as e: 
            raise e

if __name__ == '__main__': 
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Started >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    try: 
        obj=ModelTrainerPipeline()
        obj.main()
    except Exception as e: 
        raise e
    logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> stage {stage_name} Ended >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    
    
    