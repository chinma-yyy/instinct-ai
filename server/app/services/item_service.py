from bson import ObjectId
from ..models.item_model import Item
from ..utils.mongo_client import mongo

class ItemService:
    def get_all_items(self):
        collection = mongo.db.items
        items = list(collection.find())
        return items

    def get_item_by_id(self, item_id):
        collection = mongo.db.items
        item = collection.find_one({'_id': ObjectId(item_id)})
        return item
