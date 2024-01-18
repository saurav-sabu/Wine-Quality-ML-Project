import pandas as pd
from sklearn.model_selection import train_test_split
from Wine_Quality_ML_Project import logger
from Wine_Quality_ML_Project.entity.config_entity import DataTransformationConfig
import os

class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info("Splitting the data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)
        