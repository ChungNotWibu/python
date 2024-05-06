# class Student:
#     def __init__(self , name , age , math_score , language_score ):
#         self.name = name
#         self.age = age
#         self.math_score = math_score
#         self.language_score = language_score
#     def average_score(self):
#         return(float(self.math_score + self.language_score) / 2)

# student1 = Student("Chung" , 17 , 5 , 5.5)
# averange_point = student1.average_score()

# print(f"{student1.name}'s averange score is : {averange_point}")
    

# class Timer:
#     def __init__(self, hours = 0 , minutes = 0 , seconds = 0):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def tick(self):
#         self.seconds += 1
#         if self.seconds == 60:
#             self.seconds = 0
#             self.minutes += 1
#             if self.minutes == 60:
#                 self.minutes = 0
#                 self.hours += 1
#                 if self.hours == 24:
#                     self.hours = 0

#     def reset(self):
#         self.hours = 0
#         self.minutes = 0
#         self.seconds = 0

#     def toString(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"



# A = Timer()
# while True:
#     print("Chọn cài đặt")
#     print("1.Dừng")
#     print("2.In thời gian")
#     print("3.Cài lại đồng hồ")
#     print("4.Tăng s")
#     option = input()

#     if option == "1":
#         break
#     elif option == "2":
#         print(A.toString())
#     elif option == "3":
#         A.reset
#         print("Reset time")
#     elif option == "4":
#         A.tick()
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


        
