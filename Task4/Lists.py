Names = ['Hassan' , 'Ali' , 'Ahmed' , 'Mubeen']
print(Names)
print(Names[2])
print(Names[2].title())
print(Names[-1]) #for Accessing Last Element

print("My First Name is " +Names[0].title())

motorcycles = ['Honda' , 'Suzuki' , 'Yamaha']
print("I Would Like To Own A " +motorcycles[0] +" Motorcycle")

guests = ['Hassan' , 'Ali' ,'Ahmed']
print("I would Like To Invite Mr " +guests[0] +" To the Dinner")
print("I would Like To Invite Mr " +guests[1] +" To the Dinner")
print("I would Like To Invite Mr " +guests[2] +" To the Dinner")

print("So Sad To Hear That Mr " +guests[0] +" cant make it")
guests[0]= "Muneeb"
print("I would Like To Invite Mr " +guests[0] +" To the Dinner")
print("I would Like To Invite Mr " +guests[1] +" To the Dinner")
print("I would Like To Invite Mr " +guests[2] +" To the Dinner")

print("So There Are More people")
guests.insert(0 , 'Annas')
guests.insert(2 ,'Sufyan')
guests.append('Wasi')
print("I would Like To Invite Mr " +guests[0] +" To the Dinner")
print("I would Like To Invite Mr " +guests[1] +" To the Dinner")
print("I would Like To Invite Mr " +guests[2] +" To the Dinner")
print("I would Like To Invite Mr " +guests[3] +" To the Dinner")
print("I would Like To Invite Mr " +guests[4] +" To the Dinner")
print("I would Like To Invite Mr " +guests[5] +" To the Dinner")

print("Sorry But i can only invite Two People At the Dinner")

print("So Sorry We Could Not Invite Mr " +guests[5] +" To the Dinner")
guests.pop(5)

print("So Sorry We Could Not Invite Mr " +guests[4] +" To the Dinner")
guests.pop(4)

print("So Sorry We Could Not Invite Mr " +guests[3] +" To the Dinner")
guests.pop(3)

print("So Sorry We Could Not Invite Mr " +guests[2] +" To the Dinner")
guests.pop(2)

print("Mr "+guests[0] +" And Mr "+guests[1] +" You Both Are Invited")


print(len(guests))

#index Error
#print(guests[3])









