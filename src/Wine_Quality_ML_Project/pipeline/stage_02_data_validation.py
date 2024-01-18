from Wine_Quality_ML_Project.config.configuration import ConfigurationManager
from Wine_Quality_ML_Project.components.data_validation import DataValidation
from Wine_Quality_ML_Project import logger

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
    
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} STARTED")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED")
    except Exception as e:
        logger.exception(e)
        raise(e)