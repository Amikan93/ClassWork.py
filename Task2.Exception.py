def main():
    try:
        #Код, который может вызвать исключение
        result = 10/0 #Попытка деления на ноль
    except ZeroDivisionError:
        #Обработка исключения ZeroDivisionError
        print("Ошибка деления на ноль!")
    except Exception as e:
        #Обработка всех остальных исключений
        print("Произошла ошибка:", str(e))
    else:
        #Код, который выполняется, если исключений не было
        print("Результат:", result)
    finally:
        #Код, который выполяняется в любом случае
        print("Конец программы")
        
if __name__ == "__main__":
    main()