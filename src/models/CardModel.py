from unicodedata import category
from database.db import get_connection
from models.entities.Buyer import Buyer
from models.entities.Card import Card


class CardModel():

    @classmethod
    def get_cards(self):
        try:
            connection = get_connection()
            cards = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT public.card.id, price,observation,points,user_id,category_id,status_id,
                created_date, updated_date,public.category.name,public.status.name,public.user.name,public.user.surname,
                public.user.phone_number,public.user.email, public.user.address
                FROM public.card JOIN public."user" ON "user".id = "card".user_id
                JOIN public.category ON category.id = card.category_id
                JOIN public.status ON status.id = card.status_id
                ORDER BY public.card.created_date DESC
                """)
                resulset = cursor.fetchall()

                for row in resulset:
                    card = Card(row[0], row[1], row[2],
                                row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
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
                id = (cursor.fetchone()[0])
                id = id + 1
                print(type(id))
                print(id)
                if id == (None,):
                    id = 1
                cursor.execute("""INSERT INTO public.card ( price,observation,points,user_id,
                category_id,status_id,created_date) VALUES ( %s,%s,%s,%s,%s,%s,%s)""", (card.price, card.observation, card.points, card.user_id, card.category_id, card.status_id, card.created_date))
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

    @classmethod
    def add_buyer(self, buyer):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("(SELECT MAX(id)+1 FROM buyer)")
                id = cursor.fetchone()
                print((id))
                if id == (None,):
                    id = 1
                cursor.execute("""INSERT INTO buyer (id, user_id,card_id) 
                                VALUES (%s, %s,%s)""", (id, buyer.user_id, buyer.card_id))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_cards_by_category(self, category):
        try:
            connection = get_connection()
            cards = []
            print(category)
            with connection.cursor() as cursor:
                cursor.execute("""SELECT public.card.id, price,observation,points,user_id,category_id,status_id,
                created_date, updated_date,public.category.name,public.status.name,public.user.name,public.user.surname,
                public.user.phone_number,public.user.email, public.user.address
                FROM public.card JOIN public."user" ON "user".id = "card".user_id
                JOIN public.category ON category.id = card.category_id
                JOIN public.status ON status.id = card.status_id
                WHERE public.category.name = (%s)
                ORDER BY public.card.created_date DESC
                """, (category,))
                resulset = cursor.fetchall()

                for row in resulset:
                    card = Card(row[0], row[1], row[2],
                                row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                    cards.append(card.to_JSON())
            connection.close()
            return cards
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_buyer(self, buyer):
        try:
            connection = get_connection()
            buyers = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT buyer.id,user_id, card_id,public.user.name,public.user.surname 
                FROM buyer
                JOIN public."user" ON public."user".id = buyer.user_id
                WHERE buyer.card_id = %s
                """, (buyer.card_id),)
                resulset = cursor.fetchall()

                for row in resulset:
                    buyer = Buyer(row[0], row[1], row[2], row[3], row[4])
                    buyers.append(buyer.to_JSON())
            connection.close()
            return buyers
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_cards_by_status(self, status):
        try:
            connection = get_connection()
            cards = []
            with connection.cursor() as cursor:
                cursor.execute("""SELECT public.card.id, price,observation,points,user_id,category_id,status_id,
                created_date, updated_date,public.category.name,public.status.name,public.user.name,public.user.surname,
                public.user.phone_number,public.user.email, public.user.address
                FROM public.card JOIN public."user" ON "user".id = "card".user_id
                JOIN public.category ON category.id = card.category_id
                JOIN public.status ON status.id = card.status_id
                WHERE status_id = (%s)
                ORDER BY public.card.created_date DESC
                """, (status,))
                resulset = cursor.fetchall()

                for row in resulset:
                    card = Card(row[0], row[1], row[2],
                                row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                    cards.append(card.to_JSON())
            connection.close()
            return cards
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_cards_by_status_and_category(self, filter):
        try:
            connection = get_connection()
            cards = []
            with connection.cursor() as cursor:
                if (filter.category_id != None and filter.status_id != None):
                    print('los 2')
                    cursor.execute("""SELECT public.card.id, price,observation,points,user_id,category_id,status_id,
                created_date, updated_date,public.category.name,public.status.name,public.user.name,public.user.surname,
                public.user.phone_number,public.user.email, public.user.address
                FROM public.card JOIN public."user" ON "user".id = "card".user_id
                JOIN public.category ON category.id = card.category_id
                JOIN public.status ON status.id = card.status_id
                WHERE status_id = (%s) AND category_id = (%s)
                ORDER BY public.card.created_date DESC
                """, (filter.status_id, filter.category_id,))
                elif filter.category_id != None:
                    print('category')
                    cursor.execute("""SELECT public.card.id, price,observation,points,user_id,category_id,status_id,
                created_date, updated_date,public.category.name,public.status.name,public.user.name,public.user.surname,
                public.user.phone_number,public.user.email, public.user.address
                FROM public.card JOIN public."user" ON "user".id = "card".user_id
                JOIN public.category ON category.id = card.category_id
                JOIN public.status ON status.id = card.status_id
                WHERE category_id = (%s)
                ORDER BY public.card.created_date DESC
                """, (filter.category_id,))
                else:
                    print('status')
                    cursor.execute("""SELECT public.card.id, price,observation,points,user_id,category_id,status_id,
                created_date, updated_date,public.category.name,public.status.name,public.user.name,public.user.surname,
                public.user.phone_number,public.user.email, public.user.address
                FROM public.card JOIN public."user" ON "user".id = "card".user_id
                JOIN public.category ON category.id = card.category_id
                JOIN public.status ON status.id = card.status_id
                WHERE card.status_id = (%s)
                ORDER BY public.card.created_date DESC
                """, (filter.status_id,))

                resulset = cursor.fetchall()

                for row in resulset:
                    card = Card(row[0], row[1], row[2],
                                row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                    cards.append(card.to_JSON())
            connection.close()
            return cards
        except Exception as ex:
            raise Exception(ex)
