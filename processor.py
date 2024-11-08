from vipas.exceptions import UnauthorizedException, NotFoundException, BadRequestException, ForbiddenException, ConnectionException, ClientException
from vipas.logger import LoggerClient

# Initialize the logger
logger = LoggerClient(__name__)

def pre_process(input_data):
    """
    Preprocess the input data for the model. 
    This could include resizing, normalizing, or augmenting images.
    """
    try:
        # Example preprocessing logic (replace with your own)
        # Preprocess logic here: e.g., normalization, feature extraction
        preprocessed_data = input_data  # Replace this line with actual preprocessing
        logger.info("Preprocessing completed successfully.")
        return preprocessed_data
    except ConnectionException as err:
        logger.error(f"ConnectionException: {err}")
        raise
    except ClientException as err:
        logger.error(f"ClientException: {err}")
        raise
    except Exception as err:
        logger.critical(f"Unexpected error in preprocessing: {str(err)}")
        raise

def post_process(output_data):
    """
    Postprocess the model output.
    This could include formatting, decoding, or further analysis on model predictions.
    """
    try:
        # Example postprocessing logic (replace with your own)
        # Postprocess logic here: e.g., output formatting, thresholding
        postprocessed_output = output_data  # Replace this line with actual postprocessing
        logger.info("Postprocessing completed successfully.")
        return postprocessed_output
    except ConnectionException as err:
        logger.error(f"ConnectionException: {err}")
        raise
    except ClientException as err:
        logger.error(f"ClientException: {err}")
        raise
    except Exception as err:
        logger.critical(f"Unexpected error in postprocessing: {str(err)}")
        raise
