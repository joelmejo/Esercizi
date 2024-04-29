import printing_functions
#printing_functions.make_car()
from printing_functions import make_car
#make_car()
from printing_functions import make_car as fn
#fn()
import printing_functions as mn
#mn.make_car()
from printing_functions import *


# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone
# what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

def display_message() -> None:
    print("I'm learning about functions.")
    return None
display_message()


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title.
# The function should print a message, such as "One of my favorite books is Alice in Wonderland".
# Call the function, making sure to include a book title as an argument in the function call.
print()
def favorite_book(title: str) -> None:
    print(f"One of my favorite books is {title}.")
    return None
favorite_book("Alice in Wonderland")


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
print()
def make_shirt(size: str, message: str) -> None:
    print(f"Shirt\nSize: {size}\nMessage: {message}")

make_shirt("small", "Nike")

make_shirt(message="Adidas", size="small")

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
#  Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
print()
def make_shirt(size: str = "large", message: str = "I love Python.") -> None:
    print(f"Shirt\nSize: {size}\nMessage: {message}")

make_shirt()

make_shirt("medium")

make_shirt(message="I love Java.")


# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country.
# The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the default country.
print()
def describe_city(city: str, country: str ="Italy") -> None:
    print(f"{city} is in {country}.")
    return None
describe_city("Rome")
describe_city("Neaples")
describe_city("Warsaw", "Poland")


# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: "Santiago, Chile". Call your function with at least three city-country pairs, and print the values that are returned.
print()
def city_country(city: str, country: str) -> None:
    print(f"{city}, {country}")
    return None
city_country("Rome", "Italy")
city_country("Neaples", "Italy")
city_country("Warsaw", "Poland")


# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums. Print each return value to show that the  dictionaries are storing the album information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs,
#  add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.
print()
def make_album(artist_name: str, album_name: str, num_songs: int = None) -> dict:
    album = {'Artist': artist_name, 'Album': album_name}
    if num_songs != None:
        album['Number of songs'] = num_songs
    return album

album1 = make_album('Arctic Monkeys', 'Favourite Worst Nightmare', 12)
album2 = make_album('Taylor Swift', 'Reputation')
album3 = make_album('David Guetta', 'Just a Little More Love')

print(album1)
print(album2)
print(album3)


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title.
#  Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.
print()
choice: str= 'y'

# while choice == 'y':
#     artist: str= input('Please input an artist name\n')
#     album: str= input(f"Please input a {artist}'s album\n")
#     album4 = make_album(artist, album)
#     print("Do you want to add another artist and album? yes(y) or no(n)")
#     choice = input()
#     choice = choice.lower()


# 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.
print()
messages: list= ['I am going to be late.', 'I will call you later.', 'See you soon.']

def show_messages(messag: list) -> None:
    for i in messag:
        print(i)

show_messages(messages)


# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. Write a function called send_messages()
#  that prints each text message and moves each message to a new list called sent_messages as it’s printed.
#  After calling the function, print both of your lists to make sure the messages were moved correctly.
print()

sent_messages: list = []

def send_messages(messag: list) -> None:
    for i in messag:
        print(i)
        sent_messages.append(i)
    messag.clear()
    return None
# send_messages(messages)
# print(messages)
# print(sent_messages)


# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages.
#  After calling the function, print both of your lists to show that the original list has retained its messages.
print()
send_messages(messages.copy())
print(messages)
print(sent_messages)

# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects
# as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.
print()

def make_sandwich(*args) -> None:
    num_items = len(args)
    print(num_items)
    for arg in args:
        print(arg)
    return None

sandwich1 = make_sandwich('ham', 'lettuce', 'tomatoes')
sandwich2 = make_sandwich('shrimps', 'lettuce', 'mayonnaise')



# 8-13. User Profile:  Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.
# All the values must be passed to the function as parameters. The function then must return a string such as "Eric Crow, age 45, hair brown, weight 67"
print()

def build_profile(first_name: str, last_name: str, **kwargs):
    # my_profile = f"{first_name} {last_name}, age {kwargs["age"]}, hair {kwargs["hair"]}, weight {kwargs["weight"]}"
    my_profile = f"{first_name} {last_name}"
    for k in kwargs.keys():
        my_profile += f", {k} {kwargs[k]}"
    return my_profile

user = build_profile('Mario', 'Rossi', age= 45, hair='brown', weight=70)
print(user)

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs,
#  such as a color or an optional feature. Your function should work for a call like this one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
#  Print the dictionary that’s returned to make sure all the information was stored correctly. 
print()

# def make_car(manufacturer: str, model: str, **kwargs) -> None:
#     car: dict = {'manufacturer': manufacturer, 'model': model, **kwargs}
#     return car
car1 = make_car('Fiat', 'Panda', color='blue', tow_package=True)
print(car1)
# print(list(car1))
# print(*car1)
# print(str({**car1}))

# 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py.
#  Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.



# 8-16. Imports: Using a program you wrote that has one function in it, store that function in a separate file.
# Import the function into your main program file, and call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


# 8-17. Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling guidelines described in this section.
