from flask import Blueprint, jsonify, request

# Entities
from models.entities.Role import Role
# Models
from models.RoleModel import RoleModel
from models.UserRoleModel import UserRoleModel
from models.entities.UserRole import UserRole


main = Blueprint('user_role_blueprint', __name__)


@main.route('/')
def get_user_roles():
    print('Este no es')

    try:
        user_roles = UserRoleModel.get_user_roles()
        return jsonify(user_roles)
    except Exception as ex:
        return jsonify({'msj': str(ex)}), 500


@main.route('/login')
def get_user_role():

    try:
        email = request.json['email']
        password = request.json['password']

        user = UserRole(None, None, None, email, None,
                        None, None, password, None)
        role = UserRoleModel.get_user_role(user)
        if role == -1:
            return jsonify({'message': 'clave o usuario incorrecto'}), 500
        if role != None:
            return jsonify(role)
        else:
            return jsonify({'message': 'usuario no existe'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/add', methods=['POST'])
def add_user_role():
    try:
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        phone_number = request.json['phone_number']
        role_id = request.json['role_id']
        address = request.json['address']
        password = request.json['password']

        user = UserRole(None, name, surname, email,
                        phone_number, role_id, address, password)
        affected_rows = UserRoleModel.add_user_role(user)
        if affected_rows == 1:
            return jsonify({"status": True})
        else:
            return jsonify({'message': "Error on insert"}), 500
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_role(id):
    try:
        affected_rows = UserRoleModel.delete_user_role(id)

        if affected_rows == 1:
            return jsonify(id)
        else:
            return jsonify({'message': "No Status deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/update/<id>', methods=['PUT'])
def update_role(id):
    try:
        name = request.json['name']
        surname = request.json['surname']
        email = request.json['email']
        phone_number = request.json['phone_number']
        role_id = request.json['role_id']
        address = request.json['address']
        password = request.json['password']
        user = UserRole(id, name, surname, email,
                        phone_number, role_id, address, password)
        affected_rows = UserRoleModel.update_user_role(user)

        if affected_rows == 1:
            return jsonify(user.id)
        else:
            return jsonify({'message': "Error on insert"}), 500

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
