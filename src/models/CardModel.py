from database.db import get_connection
from models.entities.Card import Card


class CardModel():

    @classmethod
    def get_cards(self):
        try:
            connection = get_connection()
            cards = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT public.card.id, price,observation,points,user_id,category_id,status_id,
                created_date, updated_date,public.category.name,public.status.name,public.user.name,public.user.surname
                FROM public.card JOIN public."user" ON "user".id = "card".user_id
                JOIN public.category ON category.id = card.category_id
                JOIN public.status ON status.id = card.status_id
                """)
                resulset = cursor.fetchall()

                for row in resulset:
                    card = Card(row[0], row[1], row[2],
                                row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
                    cards.append(card.to_JSON())
            connection.close()
            return cards
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_card(self, card):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("(SELECT MAX(id)+1 FROM public.user)")
                id = cursor.fetchone()
                cursor.execute("""INSERT INTO public.card (id, price,observation,points,user_id,
                category_id,status_id,created_date) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)""", (id, card.price, card.observation, card.points, card.user_id, card.category_id, card.status_id, card.created_date))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def change_status_card(self, card):
        try:
            connection = get_connection()
            print(card.updated_date)
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE public.card SET status_id= %s, updated_date=%s WHERE id = %s """, (card.status_id, card.updated_date, card.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_card(self, card):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public.card SET price = %s,observation= %s,points= %s,user_id= %s,
                category_id= %s,status_id= %s WHERE id = %s """, (card.price, card.observation, card.points, card.user_id, card.category_id, card.status_id, card.id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
