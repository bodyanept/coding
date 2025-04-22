products = [("Хлеб", 40, 20), ("Молоко", 60, 10), ("Яблоки", 100, 98)]

for i in products:
    if i[1] < 80:
        print(f'Товар:{i[0]}')
    else:
        print(f'Товар:{i[0]}, Цена:{i[1]}')

for i in products:
    print(f'{i[0]} - всего на {i[1]*i[2]} рублей ')
        
