class person:
    counter=0  #this is clas=ed as class attribute
    
     #we want that we give a name and gender and it creates a person 
            
    def __init__(self , a='Ravi' , b='Male'):                         # called as instance methods or methods
     self.name = a                                                    # ---> Attributes or #  --->  instance variable
     self.gender= b 
     person.counter=person.counter + 1 
     #calling it using function[showinfo]
    def ShowInfo(self):
        print('name:', self.name)                                       #FROM THIS WE CAN SEE THAT WE CAN MAKE A CLASS AND THEN WE CAN USE IT FOR MAKING VARIOUS OTHER OBJECT 
        print('gender: ' , self.gender)
    @classmethod
    def Showcount(cls):
        print("Number of objects created:", cls.counter)

'''
p1 = person('Roahn' , 'Male')
p2 = person('Vaibhav' , 'Male')
p3 = person('Ravi' , 'Male')
person.Showcount()  '''

#getter and setter methods

class car:
    def __init__(self , a=40):
        self.speed=a
    def get_speed(self):
        return self._speed                 
    def set_speed(self , a):
        if a<=0 or a>=160:
            print("The speed need to be between 0-160")
        else:
            self._speed=a
    speed = property(get_speed , set_speed)
        

c1 = car()
c1.set_speed(-50)
print(c1.get_speed())  

#property function
