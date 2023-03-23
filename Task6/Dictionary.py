person = {
    "first_name" : "Hassan",
    "last_name" : "Ali",
    "age" : 19 , 
    "city" : "Rawalpindi"
}

print([person])

# create a dictionary to store people's favorite numbers
favorite_numbers = {'Alice': 42, 'Bob': 7, 'Charlie': 23, 'David': 12, 'Eve': 69}
print(favorite_numbers)

#  dictionary of major rivers and the countries they run through
rivers = {'Nile': 'Egypt', 'Amazon': 'Brazil', 'Yangtze': 'China'}

for key, value in rivers.items():
    print(f"The {key} runs through {value}.")

# create the dictionary of favorite languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'edward', 'michael', 'laura']
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, what's your favorite programming language? Please take our poll!")

#Dictionary Methods
# define the dictionary
People = {"Name": "John", "Age": 30}
People.update({"city" : "rawalpindi"})
print(People.get("city"))
People.pop("Age")
print(People)
print(People.values())
print(People.keys())
print(People.items())
People.clear()
print(People)

