#Part -1 Python Basics (Variables)
#Print Your Name with your Father name and Date of birth using suitable escape sequence charactor
print(" Name: ", "Gul Bareeda", "\n F.name: ", "M.Nasir Khan", "\n DOB:", "01.09.2004")


#Write your small bio using variables and print it using print function
Bio = '''\n\nI’m Gul Bareeda a motivated third-year Bachelor of Science in Computer Science (BSCS) student with 
a solid academic record (CGPA: 3.0) and a strong foundation in Python programming, software development, 
and problem-solving. I am passionate about learning new technologies, and applying best coding practices.
And I am originally from Hyderabad.'''
print(Bio)



'''Write a program in which use all the operators we can use in Python'''
print("\n\n=== Using use one from each type ===")
print("\n= Arithematic Operator =")

Monthly = float(input("Enter your Monthly Salary: "))
Yearly = Monthly * 12 #Arithematic Operator
print(f"Its mean your yearly total salary is: {Yearly}")

print("\n= Comparison (Relational) Operators =")
value1 = 26
value2 = 78
if value1 != value2: #comparsion Operator
    print("This is not equal to each other")
else:
    print("This is an equal value.")

print("\n= Assignment Operators =")
a = 32
b = 12 
b += a #Assignement Operator
print(b)

print("\n= Logical Operators =")

name = "Ali"
pesron = "Ahmed"

if name and pesron: #Logical Operator
    print("Correct")
else:
    print("Incorrect")

'''Completes the following steps of small task:
Mention Marks of English , Islamiat and Maths out of 100 in 3 different variables
Mention Variable of Total Marks and assign 300 to it
Calculate Percentage'''

print("\n\n=== Result Program ===")

math = float(input("Enter mathametics number: "))
eng = float(input("Enter english number: "))
isl = float(input("Enter islamiyat number: "))

total = math + eng + isl 
percentage = (total / 300) * 100

print ("Total Marks : ", total)
print ("Percentage : ", percentage)