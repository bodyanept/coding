import random

import time



x = [random.randint(0, 100000) for _ in range(10000)]


start_time = time.time()
def selection_sort(x):
    n = len(x)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if x[j] < x[min]:
                min = j
        x[i], x[min] = x[min], x[i]    
    return x
end_time = time.time()
elapsed_time = end_time - start_time

# print(f'До: {x}')
# print(f'После сортровки методом selection: {selection_sort(x)}')
print(f"Функция selection_sort выполнилась за {elapsed_time} секунд(ы)")
start_time = time.time()
def buble_sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n - i - 1):
            if x[j] > x[j+1]:
                x[j], x[j + 1] = x[j + 1], x[j]    
    return x
end_time = time.time()
elapsed_time = end_time - start_time

    
# print(f'До: {x}')
# print(f'После сортровки методом bubble: {buble_sort(x)}')
print(f"Функция buble_sort выполнилась за {elapsed_time} секунд(ы)")

start_time = time.time()
def timsort(x):
    return sorted(x)
end_time = time.time()
elapsed_time = end_time - start_time
    
# print(f'До: {x}')
# print(f'После сортровки методом timsort: {timsort(x)}')
print(f"Функция timsort выполнилась за {elapsed_time} секунд(ы)")


