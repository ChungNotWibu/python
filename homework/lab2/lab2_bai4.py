from datetime import datetime


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def welcome(self):
        print(f"Welcome, {self.username}")
    def check_password(self, password):
        return self.password == password

class SubscribedUser(User):
    def __init__(self, username, password, expiration_date):
        super().__init__(username, password)
        self.expiration_date = expiration_date
    def is_expired(self):
        current_date = datetime.now()
        return current_date > self.expiration_date


user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))
subscribed_user = SubscribedUser('s_mindx', '56789', datetime(2024, 1, 31))
subscribed_user.welcome()
print(subscribed_user.check_password('56789'))
print(subscribed_user.is_expired())