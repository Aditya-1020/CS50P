class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    
    ...
"""wizard as a class is taking care of all of the 
assignment as a student or a professor and is even doing
error checking for the name """

class Student(Wizard):
    def ____init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...
"""Student is inheriting all of the fucntionality and using
it by calling super class's own init method and aditionaly taking the 
house passed in student and assigning to its own variable of self.house"""
    
class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    
    
    ...
"""Professor is similarly to student but resetoring self.subject"""

wizard = Wizard("Albus")
student = student("Harry", "Gryffindor")
professor = Professor("Severus", "Defence Against the Dark Arts") 