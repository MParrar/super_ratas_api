from database.db import get_connection
from .entities.Role import Role
from .entities.UserRole import UserRole


class UserRoleModel():

    @classmethod
    def get_user_roles(self):
        print('Este no es')
        try:
            connection = get_connection()
            user_roles = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT public.user.id, public.user.name,surname,email,phone_number,
                role_id,address,password, role.name FROM public.user JOIN public."role" ON "role".id = "user".role_id""")
                resulset = cursor.fetchall()

                for row in resulset:
                    user_role = UserRole(row[0], row[1], row[2],
                                         row[3], row[4], row[5], row[6], row[7], row[8])
                    user_roles.append(user_role.to_JSON())
            connection.close()
            return user_roles
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_user_role(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT public.user.id, public.user.name,surname,email,phone_number,
                role_id,address,password, role.name FROM public.user JOIN public."role" ON "role".id = "user".role_id WHERE public.user.email = %s""", (user.email,))
                row = cursor.fetchone()

                found_user = None
                if row != None:
                    found_user = UserRole(row[0], row[1], row[2],
                                          row[3], row[4], row[5], row[6], row[7], row[8])
                    if found_user.password == user.password:
                        found_user = found_user.to_JSON()
                    else:
                        return -1
                else:
                    return None
            connection.close()
            return found_user
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_user_role(self, user):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("(SELECT MAX(id)+1 FROM public.user)")
                id = cursor.fetchone()
                cursor.execute("""INSERT INTO public.user (id, name,surname,email,phone_number,
                role_id,address,password) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)""", (id, user.name, user.surname, user.email, user.phone_number, user.role_id, user.address, user.password))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_user_role(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM public.user WHERE id = %s", (id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_user_role(self, user):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public.user SET name = %s,surname= %s,email= %s,phone_number= %s,
                role_id= %s,address= %s,password= %s WHERE id = %s """, (user.name, user.surname, user.email, user.phone_number, user.role_id, user.address, user.password, user.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
