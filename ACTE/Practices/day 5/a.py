class student :
    def __init__(self, name,roll):
        self.n = name
        self.r = roll
        print(f"Name is {self.n} , Roll is {self.r}")
stud = student("Alice ", 87)


class cars:
    wheels = 4
    def __init__(self,name,color,year):
        self.n = name
        self.c = color
        self.y = year
        
    def card(self):
        print(f"Car Name is {self.n} , Car Colour is {self.c},Manufactured in {self.y}")

c1 = cars("Toyato", "White" , 1975)
c2 = cars("Tata" , "Red" , 1960 )

c1.card()
c2.card()