from flask.json.provider import DefaultJSONProvider
from bson import ObjectId
from datetime import datetime

class MongoJsonProvider(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)