# 4-1. Pizzas: Think of at least three kinds of your favorite pizza.
# Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza.
# For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza.
# The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

pizzas: list = ["Margherita", "Quattro formaggi", "Diavola"]
for i in pizzas:
    print(i)

for i in pizzas:
    print(f"I like pizza {i}.")

print(f"I love the basil smell of the {pizzas[0]}.")
print(f"I used to eat {pizzas[1]} pizza when i was a kid.")
print(f"Lately i started to love the spicy flavour of the {pizzas[2]}.")
print("I really love pizza!")

# 4-2. Animals: Think of at least three different animals that have a common characteristic.
#  Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common.
#  You could print a sentence, such as Any of these animals would make a great pet!

animals: list = ["dog", "cat", "rabbit"]

for i in animals:
    print(f"A {i} would make a great pet")

print("Any of these animals would make a great pet!")


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for x in range(1, 20 + 1):
    print(x)


# 4-4. One Million: Make a list of the numbers from one to one million,
#  and then use a for loop to print the numbers. (If the output is taking too long,
#  stop it by pressing CTRL-C or by closing the output window.)

# for x in range(1, 1000001):
#     print(x)


# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max()
#  to make sure your list actually starts at one and ends at one million.
#  Also, use the sum() function to see how quickly Python can add a million numbers.

mill_numbers: list = []

for x in range(1, 1000000 + 1):
    mill_numbers.append(x)

print(min(mill_numbers))
print(max(mill_numbers))
print(sum(mill_numbers))


# 4-6. Odd Numbers: Use the third argument of the range() function
#  to make a list of the odd numbers from 1 to 20.
#  Use a for loop to print each number.

for x in range(1, 20 + 1, 2):
    print(x)


# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30.
#  Use a for loop to print the numbers in your list.

for x in range(3, 30 + 1, 3):
    print(x)


# 4-8. Cubes: A number raised to the third power is called a cube.
#  For example, the cube of 2 is written as 2**3 in Python.
#  Make a list of the first 10 cubes 
# (that is, the cube of each integer from 1 through 10),
#  and use a for loop to print out the value of each cube.

for x in range(1, 10 + 1):
    print(x**3)


# 4-9. Cube Comprehension
# Use a list comprehension to generate a list of the first 10 cubes.

cubes: list = []
for x in range(1, 10 + 1):
    cubes.append(x**3)


# 4-10. Slices: Using one of the programs you wrote in this chapter,
#  add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:.
#  Then use a slice to print the first three items from that program’s list.
# • Print the message Three items from the middle of the list are:.
#  Then use a slice to print three items from the middle of the list.
# • Print the message The last three items in the list are:.
#  Then use a slice to print the last three items in the list.

print(f"The first three items in the list are: {cubes[0:3]}")
print(f"Three items from the middle of the list are: {cubes[3:6]}")
print(f"The last three items in the list are: {cubes[7:10]}")

# 4-11. My Pizzas, Your Pizzas:
#  Start with your program from Exercise 4-1.
#  Make a copy of the list of pizzas, and call it friend_pizzas.
#  Then, do the following:
# • Add a new pizza to the original list.
# • Add a different pizza to the list friend_pizzas.
# • Prove that you have two separate lists.
#  Print the message My favorite pizzas are:,
#  and then use a for loop to print the first list.
#  Print the message My friend’s favorite pizzas are:,
#  and then use a for loop to print the second list.
#  Make sure each new pizza is stored in the appropriate list.

friend_pizzas: list = pizzas.copy()
pizzas.append("Marinara")
friend_pizzas.append("Quattro stagioni")

print("\nMy favorite pizzas are:")
for i in pizzas:
    print(i)

print("\nMy friend’s favorite pizzas are:")
for i in friend_pizzas:
    print(i)


# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space.
#  Choose a version of foods.py, and write two for loops to print each list of foods.
print()

for i in pizzas:
    print(i)

for i in friend_pizzas:
    print(i)


# 4-14. PEP 8: Look through the original PEP 8 style guide at https://peps.python.org/pep-0008/ 
# You won’t use much of it now, but it might be interesting to skim through it.


# 4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8.


# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

car = 'fiat'
print("\nIs car == 'fiat'? I predict True.")
print(car == 'fiat')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

x: int = 10

print("\nIs x > 10? I predict True.")
print(x >= 10)
print("\nIs x >= 10? I predict False.")
print(x > 10)

print("\nIs x < 11? I predict True.")
print(x < 11)
print("\nIs x < 10? I predict False.")
print(x < 10)

statement: str = 'Hello World!'

print("\nIs statement == 'Hello World!'? I predict True.")
print(statement == 'Hello World!')
print("\nIs statement == 'HelloWorld!'? I predict False.")
print(statement == 'HelloWorld!')

print("\nIs pizzas == pizzas.copy()? I predict True.")
print(pizzas == pizzas.copy())
print("\nIs pizzas == friend_pizzas? I predict False.")
print(pizzas == friend_pizzas)


# 5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10.
#  If you want to try more comparisons, write more tests and add them
# to conditional_tests.py. Have at least one True and one False result for each of
# the following:
# • Tests for equality and inequality with strings

word: str = 'Hello!'

print("\nIs word == 'Hello!'? I predict True.")
print(word == 'Hello!')
print("\nIs word == 'hello!'? I predict False.")
print(word == 'hello!')

# • Tests using the lower() method

print("\nIs word == 'hello!'? I predict True.")
print(word.lower() == 'hello!')
print("\nIs word == 'Hello!'? I predict False.")
print(word.lower() == 'Hello!')

# • Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword

word_2: str = 'hello'

print("\nIs word == 'hello!' and word_2 == 'hello'? I predict True.")
print(word == 'hello!' and word_2 == 'hello')
print("\nIs word == 'hello' and word_2 == 'hello!'? I predict False.")
print(word == 'hello' and word_2 == 'hello!')

# • Test whether an item is in a list

words: list = [word, word_2]

print("\nIs 'hello' in words[]? I predict True.")
if 'hello' in words:
    print(True)
else:
    print(False)

print("\nIs 'hello!' in words[]? I predict False.")
if 'hello!' in words:
    print(True)
else:
    print(False)

# • Test whether an item is not in a list

print("\nIs not 'hi' in words[]? I predict True.")
if 'hi' in words:
    print(False)
else:
    print(True)

print("\nIs not 'hello' in words[]? I predict False.")
if 'hello' in words:
    print(False)
else:
    print(True)


# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game.
#  Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green.
#  If it is, print a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that fails.
#  (The version that fails will have no output.)

alien_color: str = 'green'
if alien_color == 'green':
    print("\nYou have just earned 5 points.")

if alien_color == 'yellow':
    print("You have just earned 5 points.")


# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned 10 points.
# • Write one version of this program that runs the if block and another that runs the else block.

if alien_color == 'green':
    print("\nYou have just earned 5 points for shooting the alien.")
else:
    print("You have just earned 10 points.")

if alien_color == 'yellow':
    print("You have just earned 5 points for shooting the alien.")
else:
    print("You have just earned 10 points.")



# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

if alien_color == 'green':
    print("\nYou have just earned 5 points.")
elif alien_color == 'yellow':
    print("You have just earned 10 points.")
else:
    print("You have just earned 15 points.")

alien_color = 'yellow'

if alien_color == 'green':
    print("\nYou have just earned 5 points.")
elif alien_color == 'yellow':
    print("You have just earned 10 points.")
else:
    print("You have just earned 15 points.")

alien_color = 'red'

if alien_color == 'green':
    print("\nYou have just earned 5 points.")
elif alien_color == 'yellow':
    print("You have just earned 10 points.")
else:
    print("You have just earned 15 points.")


# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life.
#  Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is a baby.
# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.

print()

age: int = 40

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
#  independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit is in your list.
#  If the fruit is in your list, the if block should print a statement, such as You really like Apples!

print()

favorite_fruits: list = ['orange', 'peach', 'apple']

if 'apple' in favorite_fruits:
    print("You really like Apples!")

if 'kiwi' in favorite_fruits:
    print("You really like Kiwis!")

if 'orange' in favorite_fruits:
    print("You really like Oranges!")

if 'peach' in favorite_fruits:
    print("You really like Peaches!")

if 'banana' in favorite_fruits:
    print("You really like Bananas!")


# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.
#  Imagine you are writing code that will print a greeting to each user after they log in to a website.
#  Loop through the list, and print a greeting to each user.
# • If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again.
print()

usernames: list = ['admin', 'Kyle', 'Giulia', 'Mario', 'Caleb']

for i in usernames:
    if i == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {i}, thank you for logging in again.")


# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.
print()

if len(usernames) == 0:
    print("We need to find some users!")

usernames.clear()

if len(usernames) == 0:
    print("We need to find some users!")


# 5-10. Checking Usernames: Do the following to create a program that simulates how websites
#  ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or two of the new usernames
#  are also in the current_users list.
# • Loop through the new_users list to see if each new username has already been used.
#  If it has, print a message that the person will need to enter a new username.
#  If a username has not been used, print a message saying that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
#  (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
print()

current_users: list = ['Callum', 'John', 'Mike', 'Giulia', 'Mario']
new_users: list = ['George', 'Kyle', 'Caleb', 'Giulia', 'Mario']

# This solution works just if the lenght of both lists is the same
""" 
for i in range(len(new_users)):
    if new_users[i].lower() in current_users[i].lower():
        print(f"The username {new_users[i]} is already in use.")
    else:
        print(f"The username {new_users[i]} is available.")
"""

# This solution print everytime if a user is or is not a user in current_users
""" 
for i in range(len(new_users)):
    for e in range(len(current_users)):
        if new_users[i].lower() in current_users[e].lower():
            print(f"The username {new_users[i]} is already in use.")
        else:
            print(f"The username {new_users[i]} is available.")
"""

lower_current: list = [user.lower() for user in current_users]
lower_new: list = [user.lower() for user in new_users]

for user in lower_new:
    if user in lower_current:
        print(f"The username {user} is already in use.")
    else:
        print(f"The username {user} is available.")


# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd.
#  Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
#  Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.
print()

ordinal: list = []

for x in range(1, 9 + 1):
    ordinal.append(x)

for x in ordinal:
    if x == 1:
        print(str(x)+'st')
    elif x == 2:
        print(str(x)+'nd')
    elif x == 3:
        print(str(x)+'rd')
    if x > 3:
        print(str(x)+'th')