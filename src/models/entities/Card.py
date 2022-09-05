from utils.DateFormat import DateFormat


class Card():
    def __init__(self, id, price=None, observation=None, points=None, user_id=None, category_id=None,
                 status_id=None, created_date=None, updated_date=None, name_category=None, name_status=None, name_user=None, surname_user=None) -> None:
        self.id = id
        self.price = price
        self.observation = observation
        self.points = points
        self.user_id = user_id
        self.category_id = category_id
        self.status_id = status_id
        self.created_date = created_date
        self.updated_date = updated_date
        self.name_category = name_category
        self.name_status = name_status
        self.name_user = name_user
        self.surname_user = surname_user

    def to_JSON(self):
        return {
            'id': self.id,
            'price': self.price,
            'observation': self.observation,
            'points': self.points,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'status_id': self.status_id,
            'created_date':  DateFormat.convert_date(self.created_date),
            'updated_date':  DateFormat.convert_date(self.updated_date),
            'name_category': self.name_category,
            'name_status': self.name_status,
            'name_user': self.name_user,
            'surname_user': self.surname_user

        }
