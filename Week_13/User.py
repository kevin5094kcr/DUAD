from datetime import datetime

class User:
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age

def check_adult(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError("User is not an adult!")
        return func(user)
    return wrapper

@check_adult
def enter_club(user):
    print("Welcome to the club!")

adult_user = User(datetime(2000, 8, 11))
young_user = User(datetime(2010, 8, 11))

enter_club(adult_user)
enter_club(young_user)
