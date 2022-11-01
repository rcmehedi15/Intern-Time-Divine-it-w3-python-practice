class Student:
    roll =""
    gpa = ""
    def set_Value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
    def display(self):
        print(f"Roll : {self.roll},GPA : {self.gpa}")

rahim = Student()
rahim.set_Value(101,3.75)
rahim.display()

# rahim = Student()
# rahim.set_Value()
# rahim.display()