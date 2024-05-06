class MathList:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return str(self.data)
    def __iadd__(self, value):
        self.data = [x + value for x in self.data]
        return self

m_list = MathList([1, 2, 3, 4, 5])
print(m_list) 
m_list += 2  
print(m_list)  