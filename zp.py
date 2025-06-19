days = 7
holidays = 5
hours_OTS = 6 + 3
def zp(days,holidays,hours_OTS=9):
    obich = days * 8.2 - hours_OTS
    
    doplata = days * 2
    
    holihours = holidays * 8.2
    
    okl = round(obich * 200)
    double = round((doplata + holihours) * 400)
    print(f'по окладу = {okl}')
    
    summa = okl + double
    procent = summa / 100 
    print(procent)
    prem = (procent * 20)
    vrednost = round(procent * 12)
    pers_nadbavka = round(procent * 6)
    
    print(f'по двойной = {double}')
    
    print(summa)
    
    without_nalog = okl + double
    zp = summa  + prem + vrednost + pers_nadbavka
    
    print(f'аванс = {zp}')

# all_hours = obich + doplata + holihours
# print(all_hours)

days += 9
holidays +=5
zp(days,holidays)
