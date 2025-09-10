isim = [""] * (5)


for i in range(5):
    print("{}.Lütfen İsmi Giriniz".format(i+1))
    isim[i] = input()
isim.sort()

for i in range(5):
    print(isim[i])
