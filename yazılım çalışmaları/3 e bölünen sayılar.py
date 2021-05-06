print("""************************
3'e Bölünebilen Sayılar
************************
""")
for i in range (1,101):
    if (i % 3 != 0):
     continue
    print(i)