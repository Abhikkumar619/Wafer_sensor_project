


class ModelTrainerPipeline: 
    def __init__(self): 
        pass
    def main(self): 
        try: 
            configmanager=ConfigurationManager()
            config_model_config=configmanager.get_model_trainer_config()
            model_trainer=ModelTrainer(config_model_config)
            model_trainer.initate_model_trainer()
        except Excption as e: 
            raise e


if __main__ == '__name__': 
    
    