# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
from restaurant import Restaurant
from user import User
from admin import Admin
from privileges import Privileges
from random import sample, randint
    
restaurant = Restaurant("Pizzeria", "Italian")
print(restaurant.name)
print(restaurant.cuisin_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class,
# and call describe_restaurant() for each instance.
print("\n")
restaurant1 = Restaurant("Pizzeria", "Italian")
restaurant2 = Restaurant("Sushi", "Japanese")
restaurant3 = Restaurant("Burger King", "American")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several
# other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a
# summary of the user’s information. Make another method called greet_user() that prints a personalized greeting
# to the user. Create several instances representing different users, and call both methods for each user.
print("\n")


user1 = User("John", "Doe", 25)
user2 = User("Jane", "Doe", 23)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

# 9-4. Number Served: Start with your program from Exercise 9-1. Add an attribute called number_served with a default
# value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served,
# and then change this value and print it again. Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and print the value again. Add a method called
# increment_number_served() that lets you increment the number of customers who’ve been served.
# Call this method with any number you like that could represent how many customers were served in, say, a day of business.
print("\n")
print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(50)
print(restaurant.number_served)

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3.
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1.
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts() several times. Print the value of
# login_attempts to make sure it was incremented properly, and then call reset_login_attempts().
# Print login_attempts again to make sure it was reset to 0.
print("\n")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempts)
user1.reset_login_attempts()
print(user1.login_attempts)

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand
# that inherits from the Restaurant class you wrote in Exercise 9-1  or Exercise 9-4. Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.
print("\n")
class IceCreamStand(Restaurant):
    def __init__(self, name: str, cuisin_type: str, flavors: list[str]) -> None:
        super().__init__(name, cuisin_type)
        self.flavors = flavors
    
    def display_flavors(self):
        print(self.flavors)

stand = IceCreamStand("Gelateria", "Italian", ["Vanilla", "Chocolate", "Strawberry"])
stand.display_flavors()

# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class
# you wrote in Exercise 9-3 or Exercise 9-5. Add an attribute, privileges, that stores a list of strings like
# "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that
# lists the administrator’s set of privileges. Create an instance of Admin, and call your method.
print("\n")


admin = Admin("John", "Doe", 25, ["can add post", "can delete post", "can ban user"])
# admin.show_privileges()

# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges,
# that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class.
# Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method
# to show its privileges.
print("\n")


privileges = Privileges(["can add post", "can delete post", "can ban user"])
admin = Admin("John", "Doe", 25, privileges)
admin.privileges.show_privileges()


# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class
# called upgrade_battery(). This method should check the battery size and set the capacity to 65 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after
# upgrading the battery. You should see an increase in the car’s range.
print("\n")
class Battery:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
    
    def get_capacity(self):
        return self.capacity
    
    def upgrade_battery(self):
        if self.capacity < 65:
            self.capacity = 65

class Car:
    def __init__(self, battery: Battery) -> None:
        self.battery = battery
        self.consumption = 1.2
    
    def get_range(self):
        return self.battery.get_capacity() / self.consumption

battery = Battery(50)
car = Car(battery)
print(car.get_range())
car.battery.upgrade_battery()
print(car.get_range())

# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. Make a separate file that imports
# Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement
# is working properly.
print("\n")
restaurant6 = Restaurant("Pizzeria", "Italian")
restaurant6.describe_restaurant()
restaurant6.open_restaurant()
restaurant6.set_number_served(20)
restaurant6.increment_number_served(50)
print(restaurant6.number_served)


# 9-11. Imported Admin: Start with your work from Exercise 9-8. Store the classes User, Privileges, and Admin in one module.
# Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
print("\n")
admin = Admin("John", "Doe", 25, privileges)
admin.privileges.show_privileges()

# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module.
# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

'''
test.py
'''

# 9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6.
# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.
# Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.
print("\n")
class Die:
    def __init__(self, sides: int = 6) -> None:
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

die6 = Die()
for i in range(10):
    die6.roll_die()

# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters. Randomly select 4 numbers
# or letters from the list and print a message saying that any ticket matching these 4 numbers or letters wins a prize.
print("\n")
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e"]
winning_ticket = sample(lottery, 4)
print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")

# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.
print("\n")
my_ticket: list= sample(lottery, 4)
print(my_ticket)
winning_ticket = []
counter: int = 0
while my_ticket != winning_ticket:
    winning_ticket = sample(lottery, 4)
    counter += 1
    print(winning_ticket)
    print(counter)
    if my_ticket == winning_ticket:
        print(f"My loop had to run {counter} times to give me a winning ticket.")
    winning_ticket.clear()