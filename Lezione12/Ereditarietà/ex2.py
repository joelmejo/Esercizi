# 2

# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare,
#    e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione di
#    ricette e i loro ingredienti.

# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.

#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti.
#        Restituisce un dizionario con la ricetta appena creata o un messaggio di errore se la ricetta esiste già.

#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata.
#        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non
#        esiste.

#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata.
#        Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la
#        ricetta non esiste.

#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un
#        altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se
#        l'ingrediente non è presente o la ricetta non esiste.

#     - list_recipes(): Elenca tutte le ricette esistenti.

#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta.
#        Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.

#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono
#        un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

class RecipeManager:
    def __init__(self) -> None:
        self.recipes: dict[str, list[str]]= {}
        
    def create_recipe(self, name: str, ingredients: list[str]):
        if name not in self.recipes.keys():
            self.recipes[name] = ingredients
            return {name: ingredients}
        else:
            return "La ricetta già esiste"
    
    def add_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.recipes:
            if ingredient not in self.recipes[recipe_name]:
                self.recipes[recipe_name].append(ingredient)
                return {recipe_name: self.recipes[recipe_name]}
            else:
                return "L'ingrediente è già presente nella ricetta"
        else:
            return "La ricetta non è presente"
    
    def remove_ingredient(self, recipe_name: str, ingredient: str):
        if recipe_name in self.recipes:
            if ingredient in self.recipes[recipe_name]:
                self.recipes[recipe_name].remove(ingredient)
                return {recipe_name: self.recipes[recipe_name]}
            else:
                return "L'ingrediente non è presente nella ricetta"
        else:
            return "La ricetta non è presente"
            
    def update_ingredient(self, recipe_name: str, old_ingredient: str, new_ingredient: str):
        if recipe_name in self.recipes:
            for ingredient in self.recipes[recipe_name]:
                if ingredient == old_ingredient:
                    ingredient.replace(old_ingredient, new_ingredient)
                    return {recipe_name: self.recipes[recipe_name]}
            else:
                return "L'ingrediente non è presente nella ricetta"
        else:
            return "La ricetta non esiste"
            
    def list_recipes(self) -> None:
        ricette: list[str]= []
        for recipe in self.recipes:
            ricette.append(recipe)
        return ricette
            
    def list_ingredients(self, recipe_name):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            return "La ricetta non esiste"
    
    def search_recipe_by_ingredient(self, ingredient):
        ricette: dict[str, list[str]]= {}
        for recipe in self.recipes:
            if ingredient in self.recipes[recipe]:
                ricette[recipe] = self.recipes[recipe]
        if ricette:
            return ricette
        else:
            return "Nessuna ricetta contiene l'ingrediente"
        