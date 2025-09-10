deger = int (input())
x=deger-1
while x>1:
    if deger%x==0:
        print('{} sayisi asal degil!'.format(deger))
        break 
    else:
        x-=1
else:
    print('{} sayisi asaldir!'.format(deger))