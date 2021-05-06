"""Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez"""

print("""
********************************
Beden Kitle Endeksi Hesaplama
********************************
""")

Kilo = int(input("Kilonuzu Giriniz:"))
Boy = float(input("Boyunuzu Giriniz:"))

bki = (Kilo // Boy ** 2)

if (bki < 18.5 ):
    print("Olmanız Gerekenden Zayıfsınız...")

elif (bki >= 18.5 and bki < 25):
    print("İdeal kilonuzdasınız...")
elif (bki >= 25 and bki < 30):
    print("Olmanız gerekenden kilolusunuz...")
else:
    print("obezitesiniz...")
