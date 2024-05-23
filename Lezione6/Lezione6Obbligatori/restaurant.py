class Restaurant:
    def __init__(self, name: str, cuisin_type: str) -> None:
        self.name = name
        self.cuisin_type = cuisin_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant: {self.name}\nCuisine type: {self.cuisin_type}")
    
    def open_restaurant(self):
        print(f"{self.name} is open")

    def set_number_served(self, number: int):
        self.number_served = number
    
    def increment_number_served(self, number: int):
        self.number_served += number



