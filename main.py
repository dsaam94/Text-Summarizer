from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"----------- stage {STAGE_NAME} started -------------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"----------- stage {STAGE_NAME} finished -------------")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"----------- stage {STAGE_NAME} started -------------")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"----------- stage {STAGE_NAME} finished -------------")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"----------- stage {STAGE_NAME} started -------------")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"----------- stage {STAGE_NAME} finished -------------")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"----------- stage {STAGE_NAME} started -------------")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f"----------- stage {STAGE_NAME} finished -------------")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f"----------- stage {STAGE_NAME} started -------------")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f"----------- stage {STAGE_NAME} finished -------------")
except Exception as e:
    logger.exception(e)
    raise e