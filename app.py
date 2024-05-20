import os
from src.logger.logging import logging
from src.exception.exception import CustomException
from src.components.data_ingestion import DataIngestion
#from src.components.data_ingestion import DataIngestionConfig
import sys
if __name__ == "__main__ ":
    logging.info("The execution started")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initite_data_ingestion()
    except Exception as e:
        logging.info("Custome Exception")
        raise CustomException(e,sys)