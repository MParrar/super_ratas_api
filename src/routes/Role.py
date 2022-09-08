from flask import Blueprint, jsonify, request

# Entities
from models.entities.Role import Role
# Models
from models.RoleModel import RoleModel


main = Blueprint('role_blueprint', __name__)


@main.route('/')
def get_roles():
    try:
        roles = RoleModel.get_roles()
        return jsonify(roles)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500


@main.route('/<id>')
def get_role(id):
    try:
        role = RoleModel.get_role(id)
        if role != None:
            return jsonify(role)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_role():
    try:
        name = request.json['name']
        role = Role(None, name)
        affected_rows = RoleModel.add_role(role)
        if affected_rows == 1:
            return jsonify({"status": True})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_role(id):
    try:
        role = Role(id)
        affected_rows = RoleModel.delete_role(id)

        if affected_rows == 1:
            return jsonify(role.id)
        else:
            return jsonify({'message': "No Status deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_role(id):
    try:
        name = request.json['name']
        role = Role(id, name)

        affected_rows = RoleModel.update_role(role)

        if affected_rows == 1:
            return jsonify(role.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
