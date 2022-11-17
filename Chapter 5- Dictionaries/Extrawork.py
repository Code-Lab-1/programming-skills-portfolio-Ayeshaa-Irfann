student= { "Name" : "Ayesha Irfan", "Age" : 19 , "Nationality" : "Pakistani" , "Course" : "CC"}
print(student)

print(student["Name"])

print(student.keys())

print(student.values())

print(student.items())

student.update({"University": "Bathspa"})
print(student)

student["Age"] = 30
print(student)

student.pop("Course")
print(student)

student.popitem()
print(student)