class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")
    
    def set_number_served(self, number):
        self.number_served = number
    
    def increment_number_served(self, number):
        self.number_served += number


rest = Restaurant("Tehzeeb" , "Pakistani")
rest.describe_restaurant()
rest.open_restaurant()

rest1 = Restaurant("Italian Pizza" , "Italian")
rest1.describe_restaurant()
rest1.open_restaurant()

rest2 = Restaurant("Ranchers" , "American")
rest2.describe_restaurant()
rest2.open_restaurant()

restaurant = Restaurant("Howdy", "American")
print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 100
print(f"Number of customers served: {restaurant.number_served}")

restaurant.set_number_served(200)
print(f"Number of customers served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Number of customers served: {restaurant.number_served}")


class User:
    def __init__(self , first , last) -> None:
        self.firstname= first
        self.lastname = last
        self.login_attempts = 0

    def describe_user(self) :
        print(f"first name is {self.firstname} and last name is {self.lastname}")

    def greetUser(self):
        print(f"Hi {self.firstname} {self.lastname}")

    def increment_login_attempts(self):
        self.login_attempts +=1

    def reset_login_attempts(self):
        self.login_attempts=0

user = User("Hassan" ,"Ali")
user.describe_user()
user.greetUser()
user.increment_login_attempts()
print(f"Total Login Attempts by User 1 : {user.login_attempts}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    def add_flavor(self, flavor):
        self.flavors.append(flavor)
    
    def display_flavors(self):
        print("Available flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice = IceCreamStand("Safillo" , "Turkish")
ice.describe_restaurant()
ice.open_restaurant()
ice.add_flavor("Vanilla")
ice.add_flavor("Chocolate")
ice.display_flavors()

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []
    
    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin = Admin("Hassan", "Ali")
admin.privileges = ["can add post", "can delete post", "can ban user"]
admin.show_privileges()

sh = Admin("ALi" , "mirza")



