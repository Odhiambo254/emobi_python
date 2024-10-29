"""write classes and methods"""

class Andrew:
    def __init__(self, name, age, address): #constructor.
        self.name = name
        self.age = age
        self.address = address
#this ia method of my class Andrew.
    def state(self):
        print(f'my name is {self.name} and i am  {self.age } years and i come from {self.address}')


#lets create an instance 
              
self=Andrew(name="Andrew", age=26, address="MUMIAS")
self.state()