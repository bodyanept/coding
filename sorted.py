x = [5, 9, 8, 1, 3, 11, 6]

def selection_sort(x):
    n = len(x)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if x[j] < x[min]:
                min = j
        x[i], x[min] = x[min], x[i]    
    return x
print(selection_sort(x))


def buble_sort(x):
    n = len(x)
    for i in range(n):
        for j in range(n - i - 1):
            if x[j] > x[j+1]:
                x[j], x[j + 1] = x[j + 1], x[j]    
    return x
buble_sorted = buble_sort(x)
    
print(f'До: {x}')
print(f'После сортровки методом bubble: {buble_sorted}')
