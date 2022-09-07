from database.db import get_connection
from .entities.Status import Status


class StatusModel():

    @classmethod
    def get_all_status(self):
        try:
            connection = get_connection()
            all_status = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name FROM status')
                resulset = cursor.fetchall()

                for row in resulset:
                    status = Status(row[0], row[1])
                    all_status.append(status.to_JSON())
            connection.close()
            return all_status
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_status(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name FROM status WHERE id = %s", (id,))
                row = cursor.fetchone()

                status = None
                if row != None:
                    status = Status(row[0], row[1])
                    status = status.to_JSON()
            connection.close()
            return status
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_status(self, status):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("(SELECT MAX(id)+1 FROM status)")
                id = cursor.fetchone()
                if id == (None,):
                    id = 1
                cursor.execute("""INSERT INTO status (id, name) 
                                VALUES (%s, %s)""", (id, status.name))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_status(self, status):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM status WHERE id = %s", (status,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_status(self, status):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE status SET name = %s 
                                WHERE id = %s """, (status.name, status.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
