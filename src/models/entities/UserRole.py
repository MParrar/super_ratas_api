class UserRole():
    def __init__(self, id, name=None, surname=None, email=None, phone_number=None, role_id=None, address=None, password=None, role_name=None) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.role_id = role_id
        self.address = address
        self.password = password
        self.role_name = role_name

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone_number': self.phone_number,
            'role_id': self.role_id,
            'address': self.address,
            'password': self.password,
            'role_name': self.role_name
        }
