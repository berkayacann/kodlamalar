a = int(input("ilk sayıyı giriniz:"))
b = int(input("ikinci sayıyı giriniz:"))
c = int(input("üçüncü sayıyı giriniz:"))

if ( a > b and a > c):
    print("a")

elif ( b > a and b > c):
    print("b")
else:
    print("c")