data = [
    [5, 10, 15],
    [20, 25, 30],
    [1, 2, 3]
]

row_num = 1

for row in data:
    row_sum = 0
    
    for value in row:
        row_sum = row_sum + value
        
    print("row", row_num, "sum =", row_sum)
    row_num = row_num + 1

data = [
    [5, 10, 15],
    [20, 25, 30],
    [1, 2, 3]
]


for i in range(len(data)):
    
    print("row", i + 1, "sum =", sum(data[i]))

# The outer loop handles the rows (1 through 5)
for row in range(1, 26):
    
    for col in range(1,6):
        print(row * col, end=" ")
        break
        print()


numbers = [1, 3, 5, 3, 7, 1, 9, 5, 2]
duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        
        if numbers[i] == numbers[j]:
            
            if numbers[i] not in duplicates:
                duplicates.append(numbers[i])

print("Duplicates =", duplicates)