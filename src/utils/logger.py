import logging.config
import logging


class Logger:
    def __init__(self , filename):
        self.filename = filename
        self.LOGGER_STRUCT = {
            "version": 1,
            "handlers":{
                "fileHandler":{
                    "class": "logging.FileHandler",
                    "formatter": "myFormatter",
                    "filename": self.filename
                }
            },
            "formatters":{
                "myFormatter":{
                    "format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                }
            },
            "loggers": {
                "exlogger":{
                    "handlers": ["fileHandler"],
                    "level": "INFO"
                }
            }
        }
    
    def log(self , message):
        logging.config.dictConfig(self.LOGGER_STRUCT)
        logger = logging.getLogger('exlogger')
        logger.info(message)