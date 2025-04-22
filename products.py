products = [("Хлеб", 40), ("Молоко", 60), ("Яблоки", 100)]

for i in products:
    if i[1] < 80:
        print(f'Товар:{i[0]}')
    else:
        print(f'Товар:{i[0]}, Цена:{i[1]}')
        
