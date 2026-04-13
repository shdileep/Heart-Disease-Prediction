import os
import sys
import pandas as pd
from src.Heart.logger import logging
from src.Heart.utils.utils import load_object
from src.Heart.exception import customexception

class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,features):
        try:
            preprocessor_path=os.path.join("Artifacts","Preprocessor.pkl")
            model_path=os.path.join("Artifacts","Model.pkl")
            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)
            scaled_data=preprocessor.transform(features)
            pred=model.predict(scaled_data)
            return pred

        except Exception as e:
            raise customexception(e,sys)
    
class CustomData:
    def __init__(self,
                 age:int,
                 sex:int,
                 cp:int,
                 trestbps:int,
                 chol:int,
                 fbs:int,
                 restecg:int,
                 thalach:int,
                 exang:int,
                 oldpeak:float,
                 slope:int,
                 ca:int,
                 thal:int):
