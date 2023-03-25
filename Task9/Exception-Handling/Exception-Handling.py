while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print("The sum is:", result)
        break
    except ValueError:
        print("Error: Please enter a valid integer.")

filenames = ['cats.txt', 'dog.txt']
for filename in filenames:
    try:
        with open(filename) as file:
            print(f"\nContents of {filename}:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
