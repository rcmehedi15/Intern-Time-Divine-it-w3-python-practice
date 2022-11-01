class Student:
    roll =""
    gpa = ""
rahim = Student()
print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.7
print(f"Roll : {rahim.roll},GPA : {rahim.gpa}")
rahim = Student()
print(isinstance(rahim,Student))
rahim.roll = 101
rahim.gpa = 3.70
print(f"Roll :{rahim.roll},GPA : {rahim.gpa}")
