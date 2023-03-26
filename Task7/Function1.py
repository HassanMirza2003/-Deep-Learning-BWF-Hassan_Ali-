def make_sandwich(*items):
    print(f"Making a sandwich with the following items: {', '.join(items)}")

make_sandwich("lettuce", "tomato", "mayo") # Sandwich with three items
make_sandwich("ham", "cheese") # Sandwich with two items
make_sandwich("peanut butter", "jelly", "bread") # Sandwich with three different items

def make_car(manufacturer, model, **options):
    car = {'manufacturer': manufacturer, 'model': model}
    car.update(options)
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

