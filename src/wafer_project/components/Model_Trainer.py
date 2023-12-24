import sys
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV





class ModelTrainer: 
    def __init__(self, config=ModelTrainerConfig): 
        self.config=config
        
        self.model={
            'Grd': GradientBoostingClassifier(), 
            'Random_forest': RandomForestClassifier(), 
            'GRboost': GradientBoostingClassifier()
        }
        
        
        
    def evaluate_models(self, x_train, y_train, x_test, y_test, models): 
        try: 
            report={}
            y_train=np.array(y_train)
            y_test=np.array(y_test)
            
            for i in range(len(models)):
                model= list(models.values())[i]
                logger.info("model is created") 
                model.fit(x_train, y_train)
                
                y_train_pred=model.predict(x_test)
                
                test_model_score=accuracy_score(y_test, y_train_pred)
                
                report[list(models.keys())[i]]=test_model_score
            
            return report
                
                
                
                # logger.info(f"Model: {model}") 
                
        except Exception as e:
            raise e
    
    def fine_tune_best_model(self, best_model_object: object,
                             best_model: str, x_train, y_train,
                             params: dict
                             ):
        grid_search=GridSearchCV(best_model_object,
                                 param_grid=params,
                                 cv=5,
                                 verbose=3
                                 )
        logger.info("finetuning started\n\n")
        grid_search.fit(x_train,y_train)
        best_params=grid_search.best_params_
        
        logger.info(f"Best paramater for {best_model} is {best_params}")
        
        finetuned_model=best_model_object.set_params(**best_params)
        
        return finetuned_model
        
                
    def initate_model_trainer(self):
        try: 
            train_arr=self.config.train_arr_path
            test_arr=self.config.test_arr_path
            
            x=pd.read_csv(train_arr)
            y=pd.read_csv(test_arr)
            
            x_train=x.drop("Good/Bad", axis=1)
            y_train=x["Good/Bad"]
            x_test=y.drop("Good/Bad", axis=1)
            y_test=y["Good/Bad"]
                        
            # logger.info(f"x_train: {x_train.head(2)}\n\\n\n")
            # logger.info(f"y_train: {y_train.head(2)}\n\\n\n")
            # logger.info(f"x_test: {x_test.head(2)}\n\\n\n")
            # logger.info(f"y_test: {y_test.head(2)}\n\\n\n")
            model_report: dict=self.evaluate_models(x_train=x_train,
                                                    y_train=y_train,
                                                    x_test=x_test,
                                                    y_test=y_test,
                                                    models=self.model) 
               
            logger.info(f"Model Report : {model_report}")
            
            best_model_score=max(sorted(model_report.values()))
            
            Best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            
            logger.info(f"Best model Name: {Best_model_name}")
            
            Best_model=self.model[Best_model_name]
            
            params_grid={
                'n_estimators': [100, 200, 300],
                'max_depth': ['None', 5, 10],
                'min_samples_split': [2, 5, 10],
                'min_samples_leaf': [1, 2, 4]}
                            
            best_model_tune=self.fine_tune_best_model(best_model_object=Best_model,
                                                 best_model=Best_model_name,
                                                 x_train=x_train, 
                                                 y_train=y_train,
                                                 params=params_grid
                                                 )
            best_model_tune.fit(x_train,y_train)
            y_pred=best_model_tune.predict(x_test)
            
            model_accuracy=accuracy_score(y_test, y_pred)
            
            logger.info(f"The best model name: {Best_model_name} with accuracy: {model_accuracy}")
            
            save_object(file_path=Path(self.config.model_path), obj=best_model_tune)
            logger.info(f"Model saved at {self.config.model_path}")
                 
        except Exception as e: 
            raise e
            
    
    