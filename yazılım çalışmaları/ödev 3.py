print("""
***************************
Ders Geçme Notu Hesaplama
**************************
""")
vize = int(input("vize notunuzu giriniz:"))
final = int(input("final notunuzu giriniz:"))

Toplam_Not = (vize * 30 / 100) +  (final * 40 / 100)

if (Toplam_Not >= 90):
    print("AA")
elif (Toplam_Not >= 85):
    print("BA")
elif (Toplam_Not >= 80):
    print("BB")
elif (Toplam_Not >= 75):
    print("CB")
elif (Toplam_Not >= 70):
    print("CC")
elif (Toplam_Not >= 65):
    print("DC")
elif (Toplam_Not >= 60):
    print("DD")
elif (Toplam_Not >= 55):
    print("FD")
else:
    print("FF")