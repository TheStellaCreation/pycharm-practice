class Student:

    def __init__(self, name, major, gpa):
        # all student object data gonna passed into init this function, when we create the student object we actually
        # calling this function.
        # (self, name, major, gpa, is_on_probation) this are just parameters we passed in
        # belows self.name are actual value.
        self.name = name  # the name of the student object is equal to the name we passed in eg: student1.name
        self.major = major  # etc.
        self.gpa = gpa

# this is defining what is student data type is

# we can use functions inside this class
# we can create a function inside this class and all student objects could access this class
    def on_honor_roll(self):
        if self.gpa >= 3.5:  # referring to the actual student gpa
            return True
        else:
            return False
