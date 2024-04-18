#Jordan Krytowski
#17/04/2024

print('Hello World!')


#################
# 2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.
# Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?” 

name: str = 'Eric' 
message: str = (f"Hello {name}, would you like to learn some Python today?")
print(message)


################
# 2-4. Name Cases: Use a variable to represent a person’s name,
# and then print that person’s name in lowercase, uppercase, and title case.

name: str = 'marIo'
print(name.lower())
print(name.upper())
print(name.title())


###############
# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author.
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”



print(f'Albert Einstein once said, "A person who never made a mistake never tried anything new."')


##############
# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time,
# represent the famous person’s name using a variable called famous_person.
# Then compose your message and represent it with a new variable called message. Print your message. 

author: str = "Albert Einstein"
quote: str = "A person who never made a mistake never tried anything new."
message: str = (f'{author} once said, "{quote}"')
print(message)


##############
# 2-8. File Extensions: Python has a removesuffix() method that works exactly like removeprefix().
# Assign the value 'python_notes.txt' to a variable called filename.
# Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename: str = 'python_notes.txt'
print(filename.removesuffix(".txt"))


###############
# 3-1. Names: Store the names of a few of your friends in a list called names.
# Print each person’s name by accessing each element in the list, one at a time.

names: list = ['Andrea', 'Alessandro', 'Opon']
print(names[0])
print(names[1])
print(names[2])


##############
# 3-2. Greetings: Start with the list you used in Exercise 3-1,
# but instead of just printing each person’s name, print a message to them.
# The text of each message should be the same, but each message should be personalized with the person’s name.


message: str = "come stai?"
print(f"{names[0]}{message}")
print(f"{names[1]}{message}")
print(f"{names[2]}{message}")


###########
# 3-3. Your Own List: Think of your favorite mode of transportation,
# such as a motorcycle or a car, and make a list that stores several examples.
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”


motorcycle: list = ["Honda", "Kawasaki", "Ducati"]
print(f"I would like to own a {motorcycle[0]} motorcycle.")
print(f"I would like to own a {motorcycle[1]} motorcycle.")
print(f"I would like to own a {motorcycle[2]} motorcycle.")


###########
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner,
# who would you invite? Make a list that includes at least three people you’d like to invite to dinner.
# Then use your list to print a message to each person, inviting them to dinner.

guests: list = ["Albert Einstein", "Julius Cesar", "Tom Cruise"]
invitation: str = " would you like to join us for dinner after work?"
print(f"{guests[0]}{invitation}")
print(f"{guests[1]}{invitation}")
print(f"{guests[2]}{invitation}")


#############
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
#  so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#• Start with your program from Exercise 3-4. Add a print() call at the end of your program,
#  stating the name of the guest who can’t make it.
#• Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#• Print a second set of invitation messages, one for each person who is still in your list.

print(f"{guests[0]} can't make it.")
guests[0] = "Robert Oppenheimer"
print(f"{guests[0]}{invitation}")
print(f"{guests[1]}{invitation}")
print(f"{guests[2]}{invitation}")


###########
# 3-6. More Guests: You just found a bigger dinner table, so now more space is available.
#  Think of three more guests to invite to dinner.
#• Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program,
# informing people that you found a bigger table.
#• Use insert() to add one new guest to the beginning of your list.
#• Use insert() to add one new guest to the middle of your list.
#• Use append() to add one new guest to the end of your list.
#• Print a new set of {invitation} messages, one for each person in your list.

update: str = ", i want to inform you that i've found a bigger table so there are going to be more guests with us."
print(f"{guests[0]}{update}")
print(f"{guests[1]}{update}")
print(f"{guests[2]}{update}")
guests.insert(0, "Francesco Totti")
guests.insert(2, "Lionel Messi")
guests.append("Michael Jordan")
print(f"{guests[0]}{invitation}")
print(f"{guests[1]}{invitation}")
print(f"{guests[2]}{invitation}")
print(f"{guests[3]}{invitation}")
print(f"{guests[4]}{invitation}")
print(f"{guests[5]}{invitation}")


############
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner,
#  and now you have space for only two guests.
#• Start with your program from Exercise 3-6.
#  Add a new line that prints a message saying that you can invite only two people for dinner.
#• Use pop() to remove guests from your list one at a time until only two names remain in your list.
#  Each time you pop a name from your list, print a message to that person 
#  letting them know you’re sorry you can’t invite them to dinner.
#• Print a message to each of the two people still on your list, letting them know they’re still invited.
#• Use del to remove the last two names from your list, so you have an empty list.
#  Print your list to make sure you actually have an empty list at the end of your program.

print("My new dinner table won’t arrive in time for the dinner, and now I have space for only two guests.")
cancellation: str = " I'm sorry to inform you that i can't invite you anymore for dinner."
print(f"{guests[-1]}{cancellation}")
guests.pop(-1)
print(f"{guests[-1]}{cancellation}")
guests.pop(-1)
print(f"{guests[-1]}{cancellation}")
guests.pop(-1)
print(f"{guests[-1]}{cancellation}")
guests.pop(-1)
confirmation: str = " I want to inform you that you are still invited."
print(f"{guests[0]}{confirmation}")
print(f"{guests[1]}{confirmation}")
del guests[0:2]
print(guests)


#############
# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the actual list.
# • Show that your list is still in its original order by printing it.
# • Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# • Show that your list is still in its original order by printing it again.
# • Use reverse()  to change the order of your list. Print the list to show that its order has changed.
# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse-alphabetical order.
# Print the list to show that its order has changed.

locations: list = ["Dubai", "Riga", "Tallin", "Bucarest", "Copenaghen"]
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)


############
#3-9. Dinner Guests: Working with one of the programs from Exercises 3,
#  use len() to print a message indicating the number of people you’re inviting to dinner.

message: str = (f"I'm inviting to dinner {len(guests)} people.")
print(message)


##############
#3-10. Every Function: Think of things you could store in a list.For example, you could make a list of
#  mountains, rivers, countries, cities, languages, or anything else you’d like.
#  Write a program that creates a list containing these items and then uses
#  each function introduced in this chapter at least once.

languages: list = ["Polish", "Italian", "Spanish", "Russian"]
print(languages)
languages[0] = "Portuguese"
languages.insert(0, "English")
languages.append("French")
print(languages)
print(sorted(languages, reverse=True))
languages.reverse()
print(languages)
languages.pop(-1)
print(languages)
languages.sort()
print(languages)
del languages[0]
print(languages)


#############
#6-1. Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

friend: dict = {"first_name": 'Mario', "last_name": 'Rossi', "age": 20, "city": 'Rome'}
print(friend["first_name"])
print(friend["last_name"])
print(friend["age"])
print(friend["city"])


##########
#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
#  Think of five names, and use them as keys in your dictionary.
#  Think of a favorite number for each person, and store each as a value in your dictionary.
#  Print each person’s name and their favorite number.
#  For even more fun, poll a few friends and get some actual data for your program.

fav_numbers: dict = {"Mario": 5, "Giulia": 7, "Sofia": 9, "Marco": 12, "Luigi": 21}
print(f"Mario: {(fav_numbers['Mario'])}\nGiulia: {(fav_numbers['Giulia'])}\nSofia: {(fav_numbers['Sofia'])}\nMarco: {(fav_numbers['Marco'])}\nLuigi: {(fav_numbers['Luigi'])}\n")


# ###############
# # 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# # However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters.
#  Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon
# and then its meaning, or print the word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary: dict = {"Variable": 'A name attached to a particular object',
                 "Dictionary": 'Dictionaries are used to store data values in key:value pairs',
                 "List": 'Lists are used to store multiple items in a single variable.',
                 "Set": 'A set is a collection which is unordered, unchangeable*, and unindexed.',
                 "Tuple": 'A tuple is a collection which is ordered and unchangeable.'}

print(f"\n--------\nVariable\n{glossary['Variable']}")
print(f"\n--------\nDictionary\n{glossary['Dictionary']}")
print(f"\n--------\nList\n{glossary['List']}")
print(f"\n--------\nSet\n{glossary['Set']}")
print(f"\n--------\nTuple\n{glossary['Tuple']}")


##################
# #6-7. People: Start with the program you wrote for Exercise 6-1.
#  Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
#  Loop through your list of people. As you loop through the list, print everything you know about each person.

mom: dict = {"first_name": 'Maria', "last_name": 'Verdi', "age": 40 , "city": 'Florence'}
dad: dict = {"first_name": 'Marco', "last_name": 'Bianchi', "age": 41 , "city": 'Neaples'}
people: list = [friend, mom, dad]
for i in people:
    print(f"{(i['first_name'])} {(i['last_name'])} {(i['age'])} {(i['city'])}")


################
# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet.
#  In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets.
#  Next, loop through your list and as you do, print everything you know about each pet. 

fuffy: dict = {"kind": 'dog', "owner": friend}
john: dict = {"kind": 'parrot', "owner": mom}
isbiorn: dict = {"kind": 'dog', "owner": dad}

pets: dict = [fuffy, john, isbiorn]
print(pets)

for i in pets:
    for key in i.keys():
        if type((i[key])) is dict:
            print(key)
            for k in (i[key]):
                print(f"{k}: {(i[key][k])}")
        else:
            print(f"{key}: {i[key]}")
    print("\n")


################
# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary,
#  and store one to three favorite places for each person. To make this exercise a bit more interesting,
#  ask some friends to name a few of their favorite places. Loop through the dictionary,
#  and print each person’s name and their favorite places.


##################
# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 so each person can have more than one favorite number.
#  Then print each person’s name along with their favorite numbers.


##################
# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.
#  Create a dictionary of information about each city and include the country that the city is in,
#  its approximate population, and one fact about that city. The keys for each city’s dictionary should be
#  something like country, population, and fact. Print the name of each city and all of the information you have stored about it.


####################
# 6-12. Extensions: We’re now working with examples that are complex enough that they can be extended in any number of ways.
#  Use one of the example programs from this chapter, and extend it by adding new keys and values,
#  changing the context of the program, or improving the formatting of the output.

