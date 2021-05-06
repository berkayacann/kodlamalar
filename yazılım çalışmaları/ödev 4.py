print("""
****************************************
Geometrik Şekil Hesaplama İşlemi....
****************************************
Üçgen tipini hesaplamak için 1 yazın...
Dikdörtgen Tipini Hesaplamak için 2 yazın...
""")
Seçildi = int(input("Seçim Yapınız:"))

if (Seçildi == 1):
    x = int(input("Birinci Kenarı Giriniz:"))
    y = int(input("İkinci Kenarı Giriniz:"))
    z = int(input("Üçüncü Kenarı Giriniz:"))
    if (abs(y - z) < x and x < y + z) and (abs(x - z) < y and y < x + z) and (abs(x - y) < z and z < x + y):
        if (abs(x == y and x == z and y == z)):
            print("Eşkenar Üçgen")
        elif (abs(x == y and x != z and y != z) or (x == z and x != y and z != y) or (y == z and x != y and x != z)):
            print("İkizkenar Üçgen")
    else:
        print("Bu Ölçüler Üçgen Belirtmiyor...")
elif Seçildi == 2:
    a = int(input("Birinci Kenarı Giriniz:"))
    b = int(input("İkinci Kenarı Giriniz:"))
    c = int(input("Üçüncü Kenarı Giriniz:"))
    d = int(input("Dördüncü Kenarı Giriniz:"))
    if (a == b == c == d):
            print("Kare")
    elif (a == b and c == d) or (a == c and b == d) or (a == d and b == c):
            print("Dikdörtgen")
    else:
            print("Bu Şekil Sıradan Dörtgendir")