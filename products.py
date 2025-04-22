products = [("Хлеб", 40, 20), ("Молоко", 60, 10), ("Яблоки", 100, 98)]

for i in products:
    if i[1] < 80:
        print(f'Товар:{i[0]}')
    else:
        print(f'Товар:{i[0]}, Цена:{i[1]}')

max_price = []
for i in products:
    max_price.append((i[0],(i[1]*i[2])))
    print(f'{i[0]} - всего на {i[1]*i[2]} рублей ')

top_price = max(max_price)
print(top_price)

sum_of_all_products = 0
def sum_price(prod):
    global sum_of_all_products
    sum_of_all_products += prod
for i in max_price:
    sum_price(i[1])

print(f'Сумма всех товаров на складе будет равна: {sum_of_all_products}')
