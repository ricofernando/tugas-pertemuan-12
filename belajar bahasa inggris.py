#maks 1 miliar

huruf=['','one / satu, ','two / dua, ','three / tiga, ','four / empat, ','five / lima, ','six / enam, ','seven / tujuh, ','eight / delapan, ','nine / sembilan, ']

def nomor(n:int):
    if n<10 :
        return huruf[n]
    elif n>=1_000_000_000:
        return nomor(n//1_000_000_000)+' billion / miliar '+ nomor(n%1_000_000_000)
    elif n>=1_000_000:
        return nomor(n//1_000_000)+' million / juta ' + nomor(n%1_000_000)
    elif n>=1_000:
        return nomor(n//1000) + ' thousand / ribu ' + nomor(n%1000)
    elif n>=100:
        return nomor(n//100)+ ' hundred / ratus ' + nomor(n%100)
    elif n>=20:
        if n//10 == 2:
            return 'twenty / dua puluh ' + nomor(n%10)
        elif n//10 == 3:
            return 'thirty / tiga puluh ' + nomor(n%10)
        elif n//10 == 5:
            return 'fifty / lima puluh ' + nomor(n%10)
        else :
            return nomor(n//10)+('ty 'if (n//10)!=8 else 'y ') + nomor(n%10)
    else :
        if n==10:
            return 'ten / sepuluh '
        elif n==11:
            return 'eleven / sebelas '
        elif n==12:
            return 'twelve / dua belas '
        elif n==13:
            return 'thirteen / tiga belas'
        elif n==15:
            return 'fifteen / lima belas'
        else :
            return nomor(n%10) + 'teen / puluh'


import os
while True:
    os.system('cls')
    print('======================================================')
    print('===================SELAMAT DATANG=====================')
    print('============KAWAN - KAWANKU YANG TERCINTA=============')
    print('======================================================')
    try:
        bilangan=int(input('===============Nomor?====================\n==============>'))
        print(f'{bilangan:,} = {nomor(bilangan)}')
    except:
        print('Invalid input')

        
    print()
    
    
    while True:
        print('How about another try [yes/no] ? ',end='')
        ulang=input()
        print()
        if ulang in ('yes', 'no'):
            break
    if ulang.lower() == 'no' :
        break
