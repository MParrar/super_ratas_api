from database.db import get_connection
from .entities.Category import Category


class CategoryModel():

    @classmethod
    def get_categories(self):
        try:
            connection = get_connection()
            categories = []

            with connection.cursor() as cursor:
                cursor.execute('SELECT id, name FROM category')
                resulset = cursor.fetchall()

                for row in resulset:
                    category = Category(row[0], row[1])
                    categories.append(category.to_JSON())
            connection.close()
            return categories
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_category(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, name FROM category WHERE id = %s", (id,))
                row = cursor.fetchone()

                category = None
                if row != None:
                    category = Category(row[0], row[1])
                    category = category.to_JSON()
            connection.close()
            return category
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_category(self, category):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("(SELECT MAX(id)+1 FROM category)")
                id = cursor.fetchone()
                cursor.execute("""INSERT INTO category (id, name) 
                                VALUES (%s, %s)""", (id, category.name))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_category(self, category):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM category WHERE id = %s", (category,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_category(self, category):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE category SET name = %s 
                                WHERE id = %s """, (category.name, category.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
