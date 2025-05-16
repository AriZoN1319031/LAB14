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
    def __init__(self, restaurant_name, location='', working_hours=''):
        super().__init__(restaurant_name, cuisine_type='Кафе-мороженое')
        self.location = location
        self.working_hours = working_hours
        self.flavors = []
        self.ice_cream_types = {
            "палочка": [],
            "мягкое": [],
            "пломбир": []
        }

    def show_flavors(self):
        if self.flavors:
            print("Доступные сорта мороженого:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        else:
            print("Список сортов мороженого пуст.")

    def add_flavor(self, flavor):
        if flavor not in self.flavors:
            self.flavors.append(flavor)
            print(f"Сорт '{flavor}' добавлен.")
        else:
            print(f"Сорт '{flavor}' уже есть.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт '{flavor}' удалён.")
        else:
            print(f"Сорта '{flavor}' нет в списке.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт '{flavor}' есть в наличии.")
        else:
            print(f"Сорта '{flavor}' нет в наличии.")

    def add_ice_cream_type(self, ice_cream_type, flavor):
        if ice_cream_type in self.ice_cream_types:
            if flavor not in self.ice_cream_types[ice_cream_type]:
                self.ice_cream_types[ice_cream_type].append(flavor)
                print(f"Добавлен сорт '{flavor}' к типу '{ice_cream_type}'.")
            else:
                print(f"Сорт '{flavor}' уже есть в типе '{ice_cream_type}'.")
        else:
            print(f"Тип мороженого '{ice_cream_type}' не найден.")

    def remove_ice_cream_type_flavor(self, ice_cream_type, flavor):
        if ice_cream_type in self.ice_cream_types:
            if flavor in self.ice_cream_types[ice_cream_type]:
                self.ice_cream_types[ice_cream_type].remove(flavor)
                print(f"Удалён сорт '{flavor}' из типа '{ice_cream_type}'.")
            else:
                print(f"Сорта '{flavor}' нет в типе '{ice_cream_type}'.")
        else:
            print(f"Тип мороженого '{ice_cream_type}' не найден.")

    def show_ice_cream_types(self):
        print("Типы мороженого и их сорта:")
        for ice_cream_type, flavors in self.ice_cream_types.items():
            print(f"{ice_cream_type.capitalize()}: {', '.join(flavors) if flavors else 'пусто'}")

# Пример использования
ice_cream_cafe = IceCreamStand("Мороженка", "Центр", "10:00-22:00")

ice_cream_cafe.add_flavor("Шоколадное")
ice_cream_cafe.add_flavor("Ванильное")
ice_cream_cafe.show_flavors()

ice_cream_cafe.check_flavor("Клубничное")

ice_cream_cafe.add_ice_cream_type("палочка", "Карамельное")
ice_cream_cafe.add_ice_cream_type("мягкое", "Фисташковое")
ice_cream_cafe.show_ice_cream_types()

ice_cream_cafe.remove_flavor("Ванильное")
ice_cream_cafe.show_flavors()


