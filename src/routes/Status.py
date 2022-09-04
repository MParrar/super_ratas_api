import json
from flask import Blueprint, jsonify, request

# Entities
from models.entities.Status import Status
# Models
from models.StatusModel import StatusModel


main = Blueprint('status_blueprint', __name__)


@main.route('/')
def get_all_status():
    try:
        all_status = StatusModel.get_all_status()
        return jsonify(all_status)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500


@main.route('/<id>')
def get_status(id):
    try:
        status = StatusModel.get_status(id)
        if status != None:
            return jsonify(status)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_status():
    try:
        name = request.json['name']
        status = Status(name)
        affected_rows = StatusModel.add_status(status)
        if affected_rows == 1:
            return jsonify({"status": True})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_status(id):
    try:
        status = Status(id)
        print(id)
        affected_rows = StatusModel.delete_status(id)

        if affected_rows == 1:
            return jsonify(status.id)
        else:
            return jsonify({'message': "No Status deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_status(id):
    try:
        name = request.json['name']
        status = Status(id, name)

        affected_rows = StatusModel.update_status(status)

        if affected_rows == 1:
            return jsonify(status.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
