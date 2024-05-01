from motor.motor_asyncio import AsyncIOMotorDatabase


class MongoService:
    """
    Сервис взаимодействия с Mongo.
    """
    def __init__(self, mongo_collection: AsyncIOMotorDatabase):
        self._mongo_collection: AsyncIOMotorDatabase = mongo_collection
