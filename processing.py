string = 'Это просто строка'
boolean = True
floating = 10.0
second_floating = 15.0
def processing(a, b, c):
    number = 0
    while number <= c:
        if number == 4.0:
            print('пропуск итерации на 4')
            number += 1.0
            continue
        elif number == 9.0:
            print('отсчет окончен на 9')
            break
        if (number ** 2) > 50:
            print("Квадрат числа {number} больше 50")
            number += 1.0
        else:
	        number += 1.0

processing(string, boolean, floating)
processing(string, boolean, second_floating)
