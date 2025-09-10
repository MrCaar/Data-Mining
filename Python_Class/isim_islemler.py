import math
import random

isim = input("Lütfen ismi giriniz:")

print("1-isim uzunluğu:")
print("2-ismi ters yazdırma")
print("3-ismi random yazdırma")
print("4-ismin ortasındakini yazdırma")

sayac = int(input())

if sayac == 1:
    # ismin uzunluğu
    print(len(isim))
elif sayac == 2:
    # ismi tersten yazdırma
    print(isim[::-1])
elif sayac == 3:
    # isim random yazdırma
    rnd = list(isim)
    random.shuffle(rnd)
    print("".join(rnd))
elif sayac == 4:
    # isim ortasındaki harfi yazdırma
    uzun = len(isim)
    if uzun % 2 == 0:
        ort1 = uzun // 2
        ort2 = ort1 - 1
        print(isim[ort2:ort1+1])
    elif uzun % 2 == 1:
        orta = uzun // 2
        print(isim[orta])
