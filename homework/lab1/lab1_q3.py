import datetime

class CustomDate:
    def __init__(self) :
        self.current_datetime = datetime.datetime.now()
    
    def get_date(self):
        return self.current_datetime.strftime("%d/%m/%Y")

    def get_time(self):
        return self.current_datetime.strftime("%H:/%M:%S")

now = CustomDate()
print(now.get_date())
print(now.get_time())