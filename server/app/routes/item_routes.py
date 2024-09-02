from flask import Blueprint, request, jsonify
from ..services.item_service import ItemService

item_bp = Blueprint('items', __name__)
item_service = ItemService()

@item_bp.route('/items', methods=['GET'])
def get_items():
    items = item_service.get_all_items()
    return jsonify(items)

@item_bp.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = item_service.get_item_by_id(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
