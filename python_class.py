
class Student:

    def __init__(self , name):
        print ("Hello there Your name is entered.\n")
        self.studentName = name
    
    def display(self):
        print("Your name is ", self.studentName)


object = Student("Ram")
object.display()