class Buyer():

    def __init__(self, id, user_id=None, card_id=None, user_name=None, user_surname=None) -> None:
        self.id = id
        self.user_id = user_id,
        self.card_id = card_id,
        self.user_name = user_name,
        self.user_surname = user_surname

    def to_JSON(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'card_id': self.card_id,
            'user_name': self.user_name,
            'user_surname': self.user_surname,

        }
