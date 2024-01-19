import pandas as pd
from Wine_Quality_ML_Project import logger
from Wine_Quality_ML_Project.entity.config_entity import ModelEvaluationConfig
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from pathlib import Path
import os
from Wine_Quality_ML_Project.utils.common import save_json

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual,pred):

        acc = accuracy_score(actual,pred)
        return acc

    def save_results(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column],axis=1)
        test_y = test_data[[self.config.target_column]]

        predicted_qualities = model.predict(test_x)

        acc = self.eval_metrics(test_y,predicted_qualities)

        scores = {"accuracy":acc}
        save_json(path=Path(self.config.metric_file_name),data=scores)
