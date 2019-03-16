class animal:
    age =10
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("have something")
        print(self.name)

class bird(animal):
    def __init__(self,name,color):
        super(bird,self).__init__(name)
        self.color=color
    def fly(self):
        print(self.name)
        print(self.color)

if __name__=='__main__':
#    a = animal("xiaoli")
#   a.eat()
    b =bird("xiaoniao","red")
    b.fly()
    b.eat()
    print(b.__dict__)