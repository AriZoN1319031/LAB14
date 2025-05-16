class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Кафе-мороженое'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # список сортов мороженого

    def show_flavors(self):
        print("Доступные сорта мороженого:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Пример создания и вызова
ice_cream_stand = IceCreamStand("Мороженое на углу")
ice_cream_stand.flavors = ["Ваниль", "Шоколад", "Клубника"]
ice_cream_stand.show_flavors()
