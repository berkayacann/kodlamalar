toplam = 0

while True:
    sayı = input("Bir Sayı Giriniz:")
    if (sayı == "q"):
        break
    sayı = int(sayı)
    toplam += sayı
    else:
    print("Geçerli Bir Sayı Giriniz veya Çıkmak İçin 'q' ya basınız...")
print("Girdiğiniz Toplam Sayılar",toplam)


