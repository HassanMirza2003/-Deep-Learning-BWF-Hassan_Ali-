import time

# start the timer
start_time = time.time()

fruits = {"banana" , "Apple" , "Guava"}
print(fruits)

for d in fruits:
    print(d)

print(len(fruits))
print(type(fruits))

#using constructor 
animals = set(("Horse" , "Cow" , "Sheep")) #this will also Will not allow repition of data
print(animals)

union = animals.union(fruits)
print(union)

difference = animals.difference(fruits)
print(difference)

intersection = animals.intersection(fruits)
print(intersection)

SymmDiffernce = animals.symmetric_difference(fruits)
print(SymmDiffernce)


end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")
