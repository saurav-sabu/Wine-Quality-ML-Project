from Wine_Quality_ML_Project.config.configuration import ConfigurationManager
from Wine_Quality_ML_Project.components.model_trainer import ModelTrainer
from Wine_Quality_ML_Project import logger
from pathlib import Path

STAGE_NAME = "Model Trainer Stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} STARTED")
        obj = ModelTrainerTrainingPipeline()()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED")
    except Exception as e:
        logger.exception(e)
        raise(e)