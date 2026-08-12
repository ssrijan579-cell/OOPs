# intilize a class

class employee:
    # special methos/magic method/dunder method-constructor
    def __init__(self):
        self.id=222
        self.salary=100000
        self.designation="DS"

    def travel(self,destination):
        print(f"Employee is travelling to {destination}")


# Create an obj/instance of class
sam = employee()
print(sam.salary)
sam.travel("Mumbai")