class Filter():

    def __init__(self, status_id=None, category_id=None) -> None:
        self.status_id = status_id
        self.category_id = category_id

    def to_JSON(self):
        return {
            'status_id': self.status_id,
            'category_id': self.category_id
        }
