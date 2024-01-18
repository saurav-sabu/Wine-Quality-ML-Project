from Wine_Quality_ML_Project import logger
from Wine_Quality_ML_Project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f"{STAGE_NAME} STARTED")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED")
except Exception as e:
        logger.exception(e)
        raise(e)

