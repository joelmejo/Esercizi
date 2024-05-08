class Person:
    def __init__(self, name: str, surname: str, birth_date: str, birth_place: str, gender: str) -> None:

        self._name: str = name
        self._surname: str = surname
        self._birth_date: str = birth_date
        self._birth_place: str = birth_place
        self._gender = gender
        self._ssn: str = None
        self.compute_ssn()
        pass

    def compute_ssn(self) -> bool:
        """
        Compute the ssn
        """

        first_three_name_char = self._name[:3]
        last_three_surname_char = self._surname[-3:]
        self._ssn = first_three_name_char.upper + last_three_surname_char.upper

    def get_name(self) -> str:
        """
        This function returns a person's name
        input: none
        return: self._name: str, the function returns the person's name        
        """

        return self._name
    
    def set_name(self, name: str) -> None:
        """
        This function set the attribute name
        input: name : str, the parameter contains the user's name
        return: None
        """

        raise Exception("You cannot modify the name!")
    
    def get_ssn(self) -> str:
        """
        This function return the ssn value
        input: none
        return: self._ssn: str, the function returns the ssn value
        """

        return self._ssn
    
    def set_ssn(self, ssn: str) -> None:
        """
        This function set the ssn
        input: name : str, the parameter contains the user's ssn
        return: None
        """

        raise Exception("You cannot modify the ssn!")


person_2: Person = Person(name='Valentino', surname='Rossi')

queue: list = [person_1, person_2]

for person in queue:

    print(person._ssn)
    print(person)