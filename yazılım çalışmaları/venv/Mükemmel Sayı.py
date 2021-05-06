print("""
*******************************
Mükemmel Sayı Bulma Programı
*******************************
""")
Mükemmel_Sayı = int(input("Bir Sayı Giriniz:"))
i = 1
toplam = 0
while (i < Mükemmel_Sayı):
    if(Mükemmel_Sayı % i == 0):
        toplam += i
    i += 1
if(toplam == Mükemmel_Sayı):
    print("Seçtiğiniz Sayı Mükemmel Sayıdır.")
else:
    print("Seçtiğiniz Sayı Mükemmel Bir Sayı Değildir.")
