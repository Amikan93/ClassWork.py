counter = 0

while counter < 5:
    print("Counter: ", counter)
    counter += 1

#Прерывание цикла с помощью оператора break
while True:
    user_input = input("Введите 'q', чтобы выйти из цикла: ")
    if user_input.lower() == "q":
       break

#Пропуск итерации цикла с помощью оператора continue
counter = 0
while counter < 10:
    counter += 1
    if counter % 2 == 0:
        continue
    print("Нечетное число: ", counter)

#Вложенные циклы 
outer_counter = 0
while outer_counter < 3:
    inner_counter = 0
    while inner_counter < 3:
        print("Внешний счетчик: ", outer_counter, "Внутренний счетчик: ", inner_counter )
        inner_counter += 1
    outer_counter += 1