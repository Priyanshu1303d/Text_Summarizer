from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


# STAGE_NAME = "Data Ingestion Stage"

# try:
#     logger.info(f'--------->{STAGE_NAME} started !!!<---------')
#     data_obj = DataIngestionPipeline()
#     data_obj.main()
#     logger.info(f'--------->{STAGE_NAME} completed !!!<-------')
# except Exception as e:
#     logger.exception(e)
#     raise e

# print("\n\n----------------------------------\n\n")
# STAGE_NAME = "Data Validation Stage"

# try:
#     logger.info(f'--------->{STAGE_NAME} started !!!<---------')
#     data_obj = DataValidationPipeline()
#     data_obj.main()
#     logger.info(f'---------->{STAGE_NAME} completed !!!<------')
# except Exception as e:
#     logger.exception(e)
#     raise e

# print("\n\n----------------------------------\n\n")

# STAGE_NAME = "Data Transfromation Stage"

# try:
#     logger.info(f'---------->{STAGE_NAME} started !!!<-----')
#     data_obj = DataTransformationPipeline()
#     data_obj.main()
#     logger.info(f'------>{STAGE_NAME} completed !!!<-------')
# except Exception as e:
#     logger.exception(e)
#     raise e

# print("\n\n----------------------------------\n\n")


STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f'-------->{STAGE_NAME} started !!!<--------')
    data_obj = ModelTrainerPipeline()
    data_obj.main()
    logger.info(f'------>{STAGE_NAME} completed !!!<--------')
except Exception as e:
    logger.exception(e)
    raise e

print("\n\n----------------------------------\n\n")


STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f'--------->{STAGE_NAME} started !!!<--------')
    data_obj = ModelEvaluationPipeline()
    data_obj.main()
    logger.info(f'------>{STAGE_NAME} completed !!!<---------')
except Exception as e:
    logger.exception(e)
    raise e

print("\n\n----------------------------------\n\n")