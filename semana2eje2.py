x=int(input("ingresa n número entero"))
ifx<0:
    x=0
    printo(´Negaticvo cambiado a cero´)
elifx==0:
    print(´cero´)
elifx==2:
    print(´dos´)
else:
    print(´ninguna opcion´)
print("ok") if type(x) == int else print ("-")
