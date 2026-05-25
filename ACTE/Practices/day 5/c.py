#---------------CREATE CLASS and object------------

class book :
    def james(self):
        print("Hi")
c = book()    #must call class name and function name to run code successfully 
d = c.james()

#--------INIT---(Constructor)
class std :
    def student(self,name , roll):
        self.n = name
        self.r = roll
        print(f"{self.n},{self.r}")
st = std()
s = st.student("Gopi" , 87)

#------------ENCAPSULATION-------------
