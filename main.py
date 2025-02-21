from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f'-------------->{STAGE_NAME} started !!!<------------')
    data_obj = DataIngestionPipeline()
    data_obj.main()
    logger.info(f'-------------->{STAGE_NAME} ended !!!<------------')
except Exception as e:
    logger.exception(e)
    raise e

print("\n\n------------------------------------------------------------------\n\n")
STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f'-------------->{STAGE_NAME} started !!!<------------')
    data_obj = DataValidationPipeline()
    data_obj.main()
    logger.info(f'-------------->{STAGE_NAME} ended !!!<------------')
except Exception as e:
    logger.exception(e)
    raise e

print("\n\n------------------------------------------------------------------\n\n")