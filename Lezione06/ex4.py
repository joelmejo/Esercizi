# Exercise 4 (Folder 9 ex_4.py)
# 1. Write a new class called Food, it should have name, price and
# description as attributes.
# 2. Instantiate at least three different foods you know and like.
# 3. Create a new class called Menu, it should have a list (of Foods) as attribute.
# __init__ should take a list of Foods as optional parameters (default=[])
# 4. Create a addFood() and removeFood() for the Menu
# 5. Create a few new Food instances. Add each to the Menu using the respective
# Method.
# 6. Add a method printPrices() that list all items on the Menu with their
# prices.
# 7. Add a Menu method getAveragePrice() that returns the average Food
# price of the Menu

class Food:
    def __init__(self, name: str, price: float, description: str) -> None:
        self._name = name
        self._price = price
        self._description = description
    
    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_description(self) -> str:
        return self._description


food1 = Food("Pizza", 10.99, "A classic Italian dish")
food2 = Food("Burger", 8.49, "Juicy beef patty with cheese and vegetables")
food3 = Food("Salad", 6.99, "Fresh mixed greens with assorted toppings")

foods: list = [food1, food2, food3]

class Menu:
    def __init__(self, foods_list: list= []) -> None:
        self._foods_list = foods

    def get_food_list(self) -> list:
        return self._foods_list

    def add_food(self, food: Food) -> None:
        self._foods_list.append(food)

    def remove_food(self, i: int) -> None:
        self._foods_list.pop(i)
    
    def print_prices(self) -> None:
        for food in self._foods_list:
            print(f"{food.get_name()}: {food.get_price()}")

    def getAveragePrice(self) -> float:
        total_price = sum(food.get_price() for food in self._foods_list)  
        return total_price / len(self._foods_list)
    
        
menu1: Menu = Menu(foods)

food4 = Food("Sushi", 15.99, "Assorted seafood on seasoned rice")
food5 = Food("Pasta", 12.99, "Traditional Italian pasta dish with tomato sauce")
food6 = Food("Taco", 7.99, "Mexican street food with seasoned meat and toppings")

menu1.add_food(food4)
menu1.add_food(food5)
menu1.add_food(food6)
menu1.remove_food(-1)

menu1.print_prices()
print(menu1.getAveragePrice())


        