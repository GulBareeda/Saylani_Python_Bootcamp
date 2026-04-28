#1. Alternate elements of list
numbers = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

print("Alternate elements are:")
for i in range(0, n, 2):
    print(numbers[i], end=" ")

#2. Reverse list (without reverse())

numbers = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

reversed_list = []

for i in range(n - 1, -1, -1):
    reversed_list.append(numbers[i])

print("Reversed list:", reversed_list)

#3. Find largest number (without max())

numbers = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

#4. Left rotate list by 1

numbers = []
n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

first = numbers[0]

for i in range(n - 1):
    numbers[i] = numbers[i + 1]

numbers[n - 1] = first

print("List after rotation:", numbers)

#5. Delete a word from string

text = input("Enter a sentence: ")
word = input("Enter word to delete: ")

updated_text = text.replace(word, "")

print("Updated sentence:", updated_text)

#6. Convert date format

date = input("Enter date (mm/dd/yyyy): ")

month, day, year = date.split("/")

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

print(months[int(month) - 1], day + ",", year)


#8. Sum of each row in matrix

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element [{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]
    print(f"Sum of row {i + 1} = {row_sum}")