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

# Настройки Swagger
SWAGGER_TITLE = "Swagger"

# Настройки Redis
REDIS_HOST = str(getenv('REDIS_HOST', default='localhost'))
REDIS_PORT = str(getenv('REDIS_PORT'))
REDIS_PW = str(getenv('REDIS_PW'))
REDIS_CONNECTION_PATH = f'redis://:{REDIS_PW}@{REDIS_HOST}:{REDIS_PORT}/'

# Настройки MongoDB
MONGO_HOST = str(getenv('MONGO_HOST', default='localhost'))
MONGO_PORT = str(getenv('MONGO_PORT'))
MONGO_LOGIN = str(getenv('MONGO_LOGIN'))
MONGO_PW = str(getenv('MONGO_PW'))
MONGO_COLLECTION_SHOP = 'shop'
MONGO_COLLECTION_ORDERS = 'orders'
MONGO_PATH = f'mongodb://{MONGO_LOGIN}:{MONGO_PW}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_COLLECTION_SHOP}?authSource=admin'
