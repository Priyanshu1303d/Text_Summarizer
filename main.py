from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'-------------->{STAGE_NAME} started !!!<------------')
    data_obj = DataIngestionPipeline()
    data_obj.main()
    logger.info(f'-------------->{STAGE_NAME} ended !!!<------------')
except Exception as e:
    logger.exception(e)
    raise e