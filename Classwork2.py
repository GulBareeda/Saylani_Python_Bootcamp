'''
file = open("log.txt", "a")

while True:
    msg = input(f"Message: ")
    if msg == "FAAAHHH":
        break
    file.write("\n")

file.close() 

read_file = open("log.txt", "r")
print(read_file.read())
read_file.close()
'''
