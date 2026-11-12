print (" Creating a Simple Dictionary")
Student = {
    "name" : "Sarmad",
    "Age"  : 21,
    "Height": 5.8
}
print (Student)
print (" Acessing Values")
print ("Name :" ,Student["name"] )
print ("Age :", Student["Age"])

print ("Accesing Key Values")
Student ["Grade"] =  "A"
print (Student)

print("Modifying Key Values")
Student ["Grade"] = "B+"
print (Student)
print ("Updated Grade" ,Student["name"]  , Student["Grade"])

print("Removing a Key Value")
del Student["Grade"]
print (Student)
print('After item() call', Student.items())
print ("Iterating over Values")
for key, value in Student.items():
    print(f"{key} : {value}")
print ("Using the .get() Method")
print("name" , Student.get("name" , "Not Found"))

print ("If the Key exist")
if "name" in Student:
    print("The Key exist which is", Student["name"])
print ("Nested Dictionary")
student = {
    "Ali" : {"Age" : 22,"Height" : 5.8, "Marks" : [88 ,88 ,98]},
    "Shahroz": {"Age": 24, "Height": 5.6, "Marks": [90, 80, 99]}

}
print (student)
print("Accesing data from Nested Dictionary")
print("Ali age is" , student["Ali"] ["Age"])
print("Ali's Age:", student ["Ali"]["Age"])
def student_grade(student , student_name):
    if student_name in student:
        return sum(student [student_name]["Marks"])/ len (student [student_name]["Marks"] )
    return (f"student {student_name}")
print (student_grade (student ,"Ali"))
print (student_grade (student ,"Shahroz"))

