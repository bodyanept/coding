def open_file():
    f = open('file.txt', 'r')
    try:
        with open('file.txt', 'r') as f:
            print('Файл открыт!')
    except FileNotFoundError:
        print('Файл не найден')


def new_file():
    with open('factorial.txt', 'w') as factorial:
        def f(n):
            if n == 1: # Условие выхода
                return 1
            else:
                return n * f(n-1) 
        factorial.write(str(f(11)))
        print(f(11))
        
new_file()
