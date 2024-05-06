class Employee :
    def __init__(self,name,position) :
        self.name = name
        self.position = position
    def SayHi(self):
        print(f"Hi my name is {self.name}")
    
    def TellPosition(self):
        print(f"I'm a {self.position}")

john = Employee("John","Software Engineer")
john.SayHi()
john.TellPosition()