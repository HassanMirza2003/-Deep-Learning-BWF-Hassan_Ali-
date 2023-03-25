filename = 'Dummytext.txt'

# Reading the entire file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)

# Looping over the file object
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

filename = 'python.txt'

with open(filename) as file_object:
    for line in file_object:
        # Replace 'Python' with 'C'
        modified_line = line.replace('Python', 'C')
        print(modified_line.strip())

filename = 'guest.txt'
name = input("Please enter your name: ")
# Write the name to the file
with open(filename, 'w') as file_object:
    file_object.write(name)

filename = 'guest_book.txt'
while True:
    name = input("Please enter your name (enter 'q' to quit): ")
    if name == 'q':
        break
    print(f"Welcome, {name}!")
    with open(filename, 'a') as file_object:
        file_object.write(name + '\n')



