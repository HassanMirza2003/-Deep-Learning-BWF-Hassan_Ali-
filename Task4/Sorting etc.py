# Define the list of places to visit
places_to_visit = ['Japan', 'Peru', 'New Zealand', 'Morocco', 'Iceland']
print("Original order:", places_to_visit)

print("Alphabetical order:", sorted(places_to_visit))

print("Original order:", places_to_visit)
print("Reverse alphabetical order:", sorted(places_to_visit, reverse=True))

print("Original order:", places_to_visit)
places_to_visit.reverse()

print("Reversed order:", places_to_visit)
places_to_visit.reverse()

print("Original order:", places_to_visit)
places_to_visit.sort()

print("Alphabetical order:", places_to_visit)
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order:", places_to_visit)

# Define the list of countries
countries = ['Spain', 'France', 'Germany', 'Italy', 'Greece']

# Print the length of the list using len()
print("Length of the list:", len(countries))
print("First item in the list:", countries[0])
print("Last item in the list:", countries[-1])
countries.append('Sweden')
print("List after appending a new country:", countries)

countries.insert(2, 'Portugal')
print("List after inserting a new country:", countries)

countries.remove('France')
print("List after removing a country:", countries)

countries.sort()
print("List after sorting in alphabetical order:", countries)

countries.reverse()
print("List after reversing Order", countries)

countries_copy = countries.copy()
print("Copy of the list", countries_copy)

countries.clear()
print("List after clearing ", countries)


