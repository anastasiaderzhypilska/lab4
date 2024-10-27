class Zoo:
    def __init__(self, visitors_per_year=0, name="", number_of_animals=0):
        self.__visitors_per_year = visitors_per_year  # приватне поле
        self.__name = name                             # приватне поле
        self.__number_of_animals = number_of_animals   # приватне поле
        
        # Публічні поля
        self.public_integer = 0  # числове поле
        self.public_string = ""   # стрічкове поле

    def get_visitors_per_year(self):
        return self.__visitors_per_year

    def get_name(self):
        return self.__name

    def get_number_of_animals(self):
        return self.__number_of_animals

    def set_visitors_per_year(self, visitors):
        self.__visitors_per_year = visitors

    def set_name(self, name):
        self.__name = name

    def set_number_of_animals(self, number):
        self.__number_of_animals = number

    def __str__(self):
        return f"Zoo(name={self.__name}, visitors_per_year={self.__visitors_per_year}, number_of_animals={self.__number_of_animals})"

    def __repr__(self):
        return f"Zoo({self.__visitors_per_year}, '{self.__name}', {self.__number_of_animals})"

    def __del__(self):
        print(f"Zoo {self.__name} is being deleted.")

def main():
    # Ініціалізація трьох об'єктів класу Zoo
    zoo1 = Zoo(50000, "City Zoo", 150)
    zoo2 = Zoo(30000, "Wildlife Park", 80)
    zoo3 = Zoo(60000, "Safari Zoo", 200)

    # Виведення значень всіх полів
    for zoo in (zoo1, zoo2, zoo3):
        print(zoo)

if __name__ == "__main__":
    main()
