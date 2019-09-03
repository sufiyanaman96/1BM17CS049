class Student:
    def __init__(self,age,marks):
        self.age=age
        self.marks=marks

  
            
         
    def validate1(self):
        if(self.age<=20):
            print("age  not eligible")
            return 0
        while True:
            if self.marks<0 or self.marks>100:
                self.marks=int(input("enter the valid marks"))
            else:
                break
                
    def validate(self):
           if(self.age<=20 or self.marks<65): print(" not eligible ")
           else : print("eligible ")      
             



b=int(input("enter age"))
a=int(input("enter the marks"))


c1=Student(b,a)
c1.validate1()
c1.validate()
