import tkinter as tk
from tkinter import messagebox

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f"Ресторан: {self.restaurant_name}\nТип кухни: {self.cuisine_type}"

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, location='', working_hours=''):
        super().__init__(restaurant_name, cuisine_type='Кафе-мороженое')
        self.location = location
        self.working_hours = working_hours
        self.flavors = []

    def add_flavor(self, flavor):
        if flavor and flavor not in self.flavors:
            self.flavors.append(flavor)
            return True
        return False

    def get_flavors_text(self):
        if self.flavors:
            return "\n".join(self.flavors)
        else:
            return "Список сортов пуст"

# Создаем окно
root = tk.Tk()
root.title("Кафе Мороженое")

ice_cream_cafe = IceCreamStand("Мороженка", "Центр", "10:00-22:00")

# Верхняя подпись с названием
label_title = tk.Label(root, text=ice_cream_cafe.describe_restaurant(), font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Текстовое поле с сортами мороженого
flavors_text = tk.Text(root, height=10, width=30, state='disabled')
flavors_text.pack(pady=10)

def update_flavors_display():
    flavors_text.config(state='normal')
    flavors_text.delete(1.0, tk.END)
    flavors_text.insert(tk.END, ice_cream_cafe.get_flavors_text())
    flavors_text.config(state='disabled')

update_flavors_display()

# Поле ввода для нового сорта
entry_flavor = tk.Entry(root, width=30)
entry_flavor.pack(pady=5)

def add_flavor():
    flavor = entry_flavor.get().strip()
    if ice_cream_cafe.add_flavor(flavor):
        update_flavors_display()
        entry_flavor.delete(0, tk.END)
    else:
        messagebox.showwarning("Ошибка", "Такой сорт уже есть или поле пустое!")

btn_add = tk.Button(root, text="Добавить сорт", command=add_flavor)
btn_add.pack(pady=5)

root.mainloop()
