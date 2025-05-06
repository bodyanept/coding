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
