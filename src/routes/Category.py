from flask import Blueprint, jsonify, request

# Entities
from models.entities.Category import Category
# Models
from models.CategoryModel import CategoryModel


main = Blueprint('category_blueprint', __name__)


@main.route('/')
def get_categories():
    try:
        categories = CategoryModel.get_categories()
        return jsonify(categories)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500


@main.route('/<id>')
def get_category(id):
    try:
        category = CategoryModel.get_category(id)
        if category != None:
            return jsonify(category)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_category():
    try:
        name = request.json['name']
        category = Category(None, name)
        affected_rows = CategoryModel.add_category(category)
        if affected_rows == 1:
            return jsonify({"status": True})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_category(id):
    try:
        category = Category(id)
        affected_rows = CategoryModel.delete_category(id)

        if affected_rows == 1:
            return jsonify(category.id)
        else:
            return jsonify({'message': "No Category deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_category(id):
    try:
        name = request.json['name']
        category = Category(id, name)

        affected_rows = CategoryModel.update_category(category)

        if affected_rows == 1:
            return jsonify(category.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
