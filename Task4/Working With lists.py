# Define a list of favorite pizzas
favorite_pizzas = ['pepperoni', 'mushroom', 'vegetable']
print("My favorite pizzas are:")
for pizza in favorite_pizzas:
    print(pizza)

print("\nI like the following pizzas:")
for pizza in favorite_pizzas:
    print("I like " + pizza + " pizza.")

print("\nPizza is one of my favorite foods.")
print("I love all kinds of pizza, but my favorite pizzas are pepperoni, mushroom, and vegetable.")
print("I really love pizza!")

# Define a list of animals with a common characteristic
animals = ['dog', 'cat', 'rabbit']
print("These animals have a common characteristic:")
for animal in animals:
    print(animal)

print("\nThese animals are great pets:")
for animal in animals:
    print("A " + animal + " would make a great pet.")

print("\nAll of these animals are domesticated and popular pets.")
print("Any of these animals would make a great pet!")

# Counting to Twenty
for number in range(1, 21):
    print(number)

# One Million
numbers = list(range(1, 1000001))
for number in numbers:
    print(number)

# Summing a Million
numbers = list(range(1, 1000001))
print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
print("Sum of numbers:", sum(numbers))

# Odd Numbers
odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

# Threes
multiples_of_3 = list(range(3, 31, 3))
for number in multiples_of_3:
    print(number)

# Cubes
cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

# Cube Comprehension
cubes = [number**3 for number in range(1, 11)]
print(cubes)

# Example list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The first three items in the list are: ")
print(my_list[:3])
print("Three items from the middle of the list are: ")
print(my_list[4:7])
print("The last three items in the list are: ")
print(my_list[-3:])

# list of favorite pizzas
my_pizzas = ["Margherita", "Pepperoni", "Hawaiian"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("Veggie")
friend_pizzas.append("Meat Lovers")
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


fruits = ["apple", "banana", "mango", "orange", "pineapple"]

vegetables = ["carrot", "potato", "spinach", "tomato", "zucchini"]

print("Fruits:")
for fruit in fruits:
    print(fruit)

print("\nVegetables:")
for vegetable in vegetables:
    print(vegetable)





