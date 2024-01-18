from Wine_Quality_ML_Project.config.configuration import ConfigurationManager
from Wine_Quality_ML_Project.components.data_ingestion import DataIngestion
from Wine_Quality_ML_Project import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
    
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_files()


if __name__ == "__main__":
    try:
        logger.info(f"{STAGE_NAME} STARTED")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} COMPLETED")
    except Exception as e:
        logger.exception(e)
        raise(e)