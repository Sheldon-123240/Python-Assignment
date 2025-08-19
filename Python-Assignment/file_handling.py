#File read and write challenge
file = open("input.txt", "w")
file.write("Sheldon is a good boy.\n")

file = open("input.txt", "a")
file.write("Sheldon is single.\n")

file = open("input.txt", "a")
file.write("Sheldon lives in Lower Kabete.\n")

file = open("input.txt", "a")
file.write("Sheldon loves you.\n")

file = open("input.txt", "a")
file.write("Sheldon is bright.")

file = open("input.txt", "r")
content = file.read()
print(content)

#Error handling lab
try:
    file = open("input.txt", "r")
    content = file.read()
    print(content)
except filenotfounderror  :
    print("File not found or does not exist.Please check file path.") 
