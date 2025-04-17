string = ''
boolean = True
floating = 15.0
def processing(a='', b=False, c=10.0):
    try:
        if len(a) < 1:
            raise ValueError
    except ValueError:
        print('Ошибка: строка пустая')
    square_dict ={}
    number = 0
    while number <= c:
        if number == 4.0:
            print('пропуск итерации на 4')
            number += 1.0
            square_dict[int(number)]=(number **2)
            continue
        elif number == 9.0:
            print('отсчет окончен на 9')
            break
        if (number ** 2) < 20:
            print("Квадрат числа {number} меньше 20")
            number += 1.0
            square_dict[int(number)]=(number **2)
        elif (number ** 2) >= 20 and (number ** 2) <= 50:
            print("Квадрат числа {number} больше или равен 20 и меньше или равен 50 ")
            number += 1.0
            square_dict[int(number)]=(number **2)
        elif (number ** 2) > 50:
            print("Квадрат числа {number} больше 50")
            number += 1.0
            square_dict[int(number)]=(number **2)
        else:
            number += 1.0
            square_dict[int(number)]=(number **2)
	
    if b == True:
        odd_dict = {}
        for i in square_dict:
            if i % 2 == 0:
                odd_dict[i] = float(i ** 2)
        print(odd_dict)

processing()
processing(string, boolean, floating)
