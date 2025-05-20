import random

listo = [1,2,3,4,5,6,7,8,9]

exit_flag = False
def bogosort(lst):
    while True:
        random.shuffle(lst)
        print(lst)
        for i in range(0,len(lst)):
            if lst[i] > lst[i + 1]:
                print(lst)
                print('ошибка')
                break
            else:
                print(lst)
                exit_flag = True
                
    if exit_flag:
        break
bogosort(listo)
print(len(list))
