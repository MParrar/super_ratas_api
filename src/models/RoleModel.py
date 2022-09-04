from database.db import get_connection
from .entities.Role import Role


class RoleModel():

    @classmethod
    def get_roles(self):
        try:
            connection = get_connection()
            roles = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name FROM role')
                resulset = cursor.fetchall()

                for row in resulset:
                    role = Role(row[0], row[1])
                    roles.append(role.to_JSON())
            connection.close()
            return roles
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_role(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name FROM role WHERE id = %s", (id,))
                row = cursor.fetchone()

                role = None
                if row != None:
                    role = Role(row[0], row[1])
                    role = role.to_JSON()
            connection.close()
            return role
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_role(self, role):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("(SELECT MAX(id)+1 FROM role)")
                id = cursor.fetchone()
                cursor.execute("""INSERT INTO role (id, name) 
                                VALUES (%s, %s)""", (id, role.name))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_role(self, role):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM role WHERE id = %s", (role,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_role(self, role):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE role SET name = %s 
                                WHERE id = %s """, (role.name, role.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
