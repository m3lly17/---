m=int(input())
if m>10**7:
    print('m не должно превышать 10^7')
elif m<1:
    print('m не должно быть меньше единицы')
else:
    h = m//60
    if h>23:
        s=h%24
        print(s, m%60)
           
    
