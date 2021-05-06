print("""
**********************************
Ziraat Bankasına Hoşgeldiniz....
**********************************
""")

sys_parola = 1111
giriş_hakkı = 3
giriş_durumu = 1
while True:
    parola = int(input("Şifrenizi Giriniz:"))
    if(giriş_hakkı != 0 and parola != sys_parola):
        print("Şifre Hatalı...")
        giriş_hakkı -= 1
    elif(giriş_hakkı != 0 and parola == sys_parola):
        print("Başarıyla Giriş Yapıldı...")
        giriş_durumu += 1
        break
    else:
        print("Kartınız Bloke Edilmiştir...")
        break
if(giriş_durumu ==2):
    print("""
    *********************************
    İşlem Seçiniz
    1- Bakiye Sorgulama
    2- Para Yatırma
    3- Para Çekme
    İşlemi kapatmak için "iptal" yazınız...
    
    *********************************
    """)
    bakiye = 1000

    while True:
        işlem = input("İşlemi Seçiniz:")
        if(işlem == "iptal"):
            print("Yine Bekleriz...")
            break
        elif(işlem == "1"):
            print("Bakiyeniz {} tl'dir.".format(bakiye))
        elif(işlem == "2"):
            tutar = int(input("Yatırmak İstediğiniz Miktarı Giriniz..."))
            bakiye += tutar
        elif(işlem == "3"):
            tutar = int(input("Çekmek İstediğiniz Miktarı Giriniz..."))
            if(bakiye - tutar < 0):
                print("Bakiyeniz Yetersiz...")
                continue
            bakiye -= tutar
    else:
        print("Geçersiz İşlem Seçtiniz...")


