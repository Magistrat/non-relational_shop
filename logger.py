from logging import CRITICAL
from logging import DEBUG
from logging import ERROR
from logging import FileHandler
from logging import Formatter
from logging import getLogger
from logging import INFO
from logging import StreamHandler
from logging import WARNING
from logging.config import dictConfig

from settings import BASE_LOGGING_CONFIG


class CustomFormatter(Formatter):
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'
    format_config = '%(levelname)s:     %(filename)s:%(lineno)d %(message)s'

    FORMATS = {
        DEBUG: grey + format_config + reset,
        INFO: blue + format_config + reset,
        WARNING: yellow + format_config + reset,
        ERROR: red + format_config + reset,
        CRITICAL: bold_red + format_config + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = Formatter(log_fmt)
        return formatter.format(record)


# Get the Logger
dictConfig(BASE_LOGGING_CONFIG)
app_logger = getLogger('app')
app_logger.setLevel(INFO)

# Add CustomFormatter and File to the Handler
custom_format_handler = StreamHandler()
custom_format_handler.setFormatter(CustomFormatter())
app_logger.addHandler(custom_format_handler)

file_format = Formatter('%(asctime)s %(levelname)s:     %(filename)s:%(lineno)d %(message)s')
file_handler = FileHandler('logfile.log')
file_handler.setFormatter(file_format)
app_logger.addHandler(file_handler)


UNICORN_LOGGING_CONFIG = {
    **BASE_LOGGING_CONFIG,
    'formatters': {
        'default': {
            '()': CustomFormatter,
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'INFO',
        },
    },
    'loggers': {
        'uvicorn.access': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'uvicorn.error': {
            'handlers': ['default'],
            'level': 'ERROR',
            'propagate': True
        },
        'app': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
    }
}
