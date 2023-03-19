# Define a tuple of basic foods
basic_foods = ('pasta', 'rice', 'chicken', 'soup', 'salad')

# Print each food using a for loop
print("The restaurant offers:")
for food in basic_foods:
    print("- " + food)

# Error In Tuple
basic_foods[0] = 'pizza'

new_foods = ('steak', 'fish', 'chicken', 'soup', 'fries')
print("\nThe restaurant's revised menu is:")
for food in new_foods:
    print("- " + food)
