from flask import Flask, render_template, request,send_file
import os
import numpy as np
import pandas as pd
from wafer_project.pipeline.predict import PredictPipeline
from wafer_project import logger


app=Flask(__name__)

@app.route('/', methods=['GET'])
def homePage(): 
    return render_template("index.html")

@app.route("/train", methods=['GET'])
def training(): 
    os.system("python main.py")
    
@app.route("/predict", methods=['GET','POST'])
def upload(): 
    try: 
        if request.method == 'POST':
             
    
            predict_obj=PredictPipeline(request)
            predict_config=predict_obj.run_pipeline()
            
            logger.info("Prediction completed")
            
            # Now for downloading the predicted file.
            return send_file(predict_config.prediction_file_path,
                             download_name=predict_config.prediction_file_name,
                             as_attachment=True)            
                
            
        else: 
            return render_template("upload_file.html")
        
    except Exception as e: 
        raise e
        
        
    
    





if __name__ == "__main__": 
    app.run(host="0.0.0.0", debug=True)