listCar = [
    ["Toyota" , "10000$"],
    ["Lexus", "20000$"]
]

class Garage:
    listCar = []
    totalPrice = 0
    
    def __init__(self,name):
        self.ownerName = name
    
    def checkCar(self,carName):
        check_car_exist = False
        for car in self.listCar:
            if carName in car[0]: 
                check_car_exist = True
                break
        if check_car_exist:
            print(f"Có xe {carName} trong gara")
        else:
            print(f"Không có xe {carName} trong gara ")
        return check_car_exist

    def owner(self):
        return self.ownerName

    def addCar(self , carName , price):
        if (self.checkCar):
            self.listCar.append((carName,price))
            self.totalPrice += price
            print(f"Thêm thành công xe {carName} với giá {price}")

    def useCar(self,carName):
        for car in self.listCar:
            if car[0] == carName:
                carPrice = car[1]
                carPrice -= carPrice*0.2
                self.totalPrice -= carPrice*0.02
                break
    
    def sellCar(self,carName):
        for car in self.listCar:
            if car[0] == carName:
                carPrice = car[1]
                self.listCar.remove(car)
                self.totalPrice -= carPrice
                break