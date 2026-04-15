#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
#1
salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))

if years > 9:
    bonus = salary * 0.05
    print("Bonus amount:", bonus)
else:
    print("No bonus")

#Write a program to check whether a person is eligible for voting or not. 
# (accept age from user) if age is greater than 17 eligible otherwise not eligible
#2
age = int(input("Enter your age: "))

if age > 18:
    print("Eligible for voting")
else:
    print("Not eligible")

#Write a program to check whether a number entered by user is even or odd.
#3
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#Write a program to check whether a number is divisible by 7 or not. Show Answer  
#4
num = int(input("Enter a number: "))

if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

#Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
#5  
num = int(input("Enter a number: "))

if num % 7 == 0:
    print("Hello")
else:
    print("Bye")  

#Write a program to display the last digit of a number.

num = int(input("Enter a number: "))

last_digit = num % 10
print("Last digit is:", last_digit)

#Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))

if length == breadth:
    print("Square")
else:
    print("Rectangle")


#Take two int values from user and print greatest among them.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Greatest number is:", num1)
else:
    print("Greatest number is:", num2)



#A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity = int(input("Enter quantity: "))
price = quantity * 100

if price > 1000:
    discount = price * 0.10
    total = price - discount
else:
    total = price

print("Total cost:", total)

'''A school has following rules for grading system:
a. Below 25 - F

b. 25 to 45 - E

c. 45 to 50 - D

d. 50 to 60 - C

e. 60 to 80 - B

f. Above 80 - A

Ask user to enter marks and print the corresponding grade.'''

print("----Annual School Result ----")

student_name = input("Enter your name : ")
student_rollno = input("Enter your rollno :")

math = float (input("Enter your mathametics number : "))
urdu = float (input("Enter your urdu number : "))
eng = float (input("Enter your english number : "))
sci = float (input("Enter your science number : "))
comp = float (input("Enter your computerscience number : "))

total = math + urdu + eng + sci + comp

percentage = (total / 500) * 100

print ("Student Name : ", student_name)
print ("Student Rollnumber : ", student_rollno)
print ("student Total Marks : ", total)
print ("Student percentage : ", percentage)

if math >= 90:
    print("Grade : A+")
elif urdu >= 70:
    print("Grade : B+")
elif eng >= 60:
    print("Grade : C+")
elif math >= 50:
    print("Grade : D")
elif comp >= 40:
    print("Grade : F")

else:
    print("Not Promoted")


'''A student will not be allowed to sit in exam if his/her attendence is less than 75%.

Take following input from user

Number of classes held

Number of classes attended.

And print

percentage of class attended

Is student is allowed to sit in exam or not.'''


held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))

percentage = (attended / held) * 100

print("Attendance percentage:", percentage)

if percentage >= 75:
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")



#Modify the above question to allow student to sit if he/she has medical cause. 
#Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

held = int(input("Enter number of classes held: "))
attended = int(input("Enter number of classes attended: "))

percentage = (attended / held) * 100
print("Attendance percentage:", percentage)

medical = input("Do you have medical cause? (Y/N): ")

if percentage >= 75:
    print("Allowed to sit in exam")
elif medical == 'Y':
    print("Allowed to sit in exam (Medical reason)")
else:
    print("Not allowed to sit in exam")

#Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but 
# if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")   


#Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and 
#then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR"

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
marital_status = input("Enter marital status (Y/N): ").upper()

if gender == 'F':
    print("She will work only in urban areas.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("He may work anywhere.")
    elif 40 < age <= 60:
        print("He will work in urban areas only.")
    else:
        print("ERROR")
else:
    print("Invalid gender input.")



units = int(input("Enter number of units: "))

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10

print("Total bill amount is Rs.", bill)


#Write a program to calculate the electricity bill (accept number of unit from user) 
# according to the following criteria : Unit Priceuptp 100 units no charge Next 200 units Rs 5 per unit 
# After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750

units = int(input("Enter number of units: "))

if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10

print("Total bill amount is Rs.", bill)



#Take input of age of 3 people by user and determine oldest and youngest among them.
age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))

oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)

print("Oldest age is:", oldest)
print("Youngest age is:", youngest)