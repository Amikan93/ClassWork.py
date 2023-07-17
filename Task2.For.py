#Пример испльзования цикла for с числового диапазона
for i in range(5):
    print("Число: ", i)

#Пример использования цикла for со списком 
fruits = ["яблоко", "банан", "груша"]
for fruit in fruits:
    print("Фрукт: ", fruit)

#Пример использования цикла for с кортежем
colors = ("красный", "зеленый", "синий")
for color in colors:
    print("Цвет: ", color)

#Пример использовния цикла for с множеством
numbers = {1, 2, 3, 4, 5}
for number in numbers:
    print("Число: ", number)

#Пример использования цикла for со словарем
person = {"имя": "Алекс", "возраст": 25, "город": "Москва"}
for key, value in person.items():
    print(key + ":", value)

#Пример использования цикла for с функцией range() - это плохой пример
#не используйте это
letters = ["a", "b", "c", "d", "e"]
for index in range(len(letters)):
    print("Пункт массива = ", letters[index], "имеет индекс", index)

#Пример использования цикла for с функцей enumerate()
#верный питонячий
letters = ["a", "b", "c", "d", "e"]
for index, letter in enumerate(letters):
    print("Буква - ", letter, "имеет индекс",  index)

#Пример использования цикла for с функцией enumerate()
person = {"имя": "Алекс", "возраст": 25, "город": "Москва"}
for index, value in enumerate(person):
    print("Пункт словаря -", value, "имеет индекс", index)

#Пример использования цикла for с функцией enumerate()
person = {"имя": "Алекс", "возраст": 25, "город": "Москва"}
for value in enumerate(person):
    print(
        "Пункт словаря -", value, "ключ", f"'{value[1]}'", "значение", person[value[1]]
    )

#Пример list comprehension
print([x for x in enumerate(person)])

print([x [0] for x in enumerate(person)])
print([x [1] for x in enumerate(person)])
print([person[x[1]] for x in enumerate(person)])