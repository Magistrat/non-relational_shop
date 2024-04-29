from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Общие настройки
BASE_LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True
}

APP = 'main:app'
APP_VERSION = str(getenv('APP_VERSION'))
OPEN_API_VERSION = '3.0.1'
HOST = '0.0.0.0'
PORT = int(str(getenv('INTERNAL_PORT')))

SWAGGER_TITLE = "Swagger"
SWAGGER_TAGS_METADATA = [
    {
        'name': "Swagger",
        'description': 'Swagger documentation'
    },
]