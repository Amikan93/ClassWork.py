
#Пример с размером строки
import datetime
import json


def string_max_size() -> int:
    import sys
    
    return sys.maxsize


#Переносы строк
def line_breaks() -> None:
    text = "one\ntwo\nthree"
    print(text)

    return None

#Контатенация строк
def concatenation() -> None:

    s1 = "Hello" + " world"
    s2 = " world"

    print(s1+s2)

    name = "John"
    age = 30

    print("Name: " + name + ", age: " +str(age))
    return None


# Сравнение строк
def string_compare() -> None:
    s1 = "1a"
    s2 = "aa"
    s3 = "Aa"
    s4 = "ba"

    print("aa" < "Aa") #сравнение регистров
    print("aa" > "ba") #сравнение букв по алфавиному порядку
    print("aa" < "az") #первые буквы одинаковые, сравниваются следующие две
    print(s1 > s2) #сравнение цифры с буквой
    print(s3 == s4) #сравнение строк

    s1 = "Intel"
    s2 = "intel"

    print(s1==s2) #Регистр имеет значение

    print(s1.lower() == s2.lower()) #Приведение к нижнему регистру

    return None


#Удалить строку
def remove_string() -> None:
    s = "test"

    print(s, s.replace("test", " "))

    s = "test"
    s = " "

    print(s)

    return None


#Обращение по индексу
def index_string() -> None:

    s = "abcdef"
    print(s[0]) #первая буква
    print(s[1]) #вторая буква 
    print(s[2]) #третья буква

    print(s[-1]) #последняя буква

    return None

#Форматрование строк 
def custom_format_string() -> None:
    name = "Alex"
    print("Hello, %s" %name)

    print("%d %s, %d %s" % (6, "bananas", 10, "lemons"))

    print("{}".format(100))

    print("{0}, {1},{2}".format("one", "two", "three"))

    print(f"Hello, {name}!")
    a = 5
    b = 10

    print(f"Five plus ten is {a + b} and not {2 * (a + b)}.")

    return None

#Методы для работы со строками
def string_methods() -> None:

    text = ("Wikipedia is a Python library that makes "
            "it easy to access and parse data form Wikipedia")
    
    print(text.find("Wikipedia")) #возвращает индекс первого вхождения 
    print(text.rfind("Wikipedia")) #возвращает индекс последнего вхождения 
    print(text.count("Wikipedia")) #возвращает количество вхождений 

    print(
        text.replace("from Wikipedia", "from https://www.wikipedia.org/")
    ) #заменяет строку
    print(text.split(" ")) # разделяет строку

    split_text = text.split(" ") #разделяет строку 
    print(split_text)
    print("_".join(split_text)) #объединяет строку

    text = " test "
    print(text.strip()) #удаляет пробелы
    print(text.lstrip()) #удаляет пробелы в начале
    print(text.rstrip()) #удаляет пробелы в конце

    text = "python is a product of the python Software Foundation"

    print(text.capitalize()) # приводит первый симвл к верхнему регистру

    return None

#Преобразование строк
    def string_to_types() -> None:
        import json
        from datetime import datetime

    print(int("10")) #преобразование строки в целое
    print(int("0x12F", base=16)) #преобразование строки строки в список строк

    print("one two three four".split()) #преобразование строки строки в список строк

    print("Байты".encode("utf-8")) #преобразование строки в байты

    #преобразование строки в байты
    print(datetime.strptime("Jan 1 2020 1:33PM", "%b %d %Y %I:%M%p"))

    print(float("1.5")) #преобразавние строки в вещественное число

    #преобразование сроки в словарь 
    print(
        json.loads('{"Russia": "Moscow", "France": "Paris"}')
    ) # преобразование строки в словарь

    print(json.dumps("hello")) # Конвертация объектов Python в объект json

    return None

def best_practices() -> None:
    import re

    text = "django"

    print(list(text)) # преобразование строки в список
    print([c for c in "text"]) # преобразование строки в список

    # Как повернуть строку 

    #Преобразование строки в список
    for c in text: 
        print(c)

    #Как из строки выделить числа
    str = "h3110 23 cat 444.4 rabbit 11 2 dog"
    print([int(s) for s in str.split() if s.isdigit()])
    print(re.findall(r"\d+", str))

    # Как перевернуть строку
    print("test"[::-1])
    print("".join(reversed("test")))

    # Как удалить последний символ в строке
    print("Some text1" [:-1])

    # Как убрать пробелы из строки
    print(" Some text2 ".strip())
    print(" So me t e x t ".replace(" ", ""))

    return None

#Примеры использования кавычек: 
def quatation_marks() -> None:

    print('string') #одинарные кавычки
    print("string") #двойные кавычки
    print('''string''') #тройные кавычки
    print("""string""") #тройные кавычки

    print('book "war and peace"') #разный тип кавычек
    print("book 'war and peace'") #разный тип кавычек
    print('book "war and peace"') #экранирование кавычек одного типа
    print("book 'war and peace'") #экранирование кавычек одного типа

    return None

def main() -> None:

    quatation_marks()

    line_breaks()

    concatenation()

    string_compare()

    remove_string()

    index_string()

    custom_format_string() 

    string_methods()

    best_practices()


if __name__== "__main__":
    main()