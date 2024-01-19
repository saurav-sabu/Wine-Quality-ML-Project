from Wine_Quality_ML_Project.config.configuration import ConfigurationManager
from Wine_Quality_ML_Project.components.model_evaluation import ModelEvaluation
from Wine_Quality_ML_Project import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        model_evaluation.save_results()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} STARTED")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED")
    except Exception as e:
        logger.exception(e)
        raise(e)