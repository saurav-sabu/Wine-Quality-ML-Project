from Wine_Quality_ML_Project import logger
from Wine_Quality_ML_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Wine_Quality_ML_Project.pipeline.stage_02_data_validation import DataValidationTrainingPipeline



STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f"{STAGE_NAME} STARTED")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED")
except Exception as e:
        logger.exception(e)
        raise(e)


STAGE_NAME = "Data Valdiation Stage"

try:
        logger.info(f"{STAGE_NAME} STARTED")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED")
except Exception as e:
        logger.exception(e)
        raise(e)
