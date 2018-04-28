print("Menu")

print("""1-suma
2-Resta
3-Multiplicacion
4-Divicion
5-Comparar
6-IVA
7-Multiplicacion indel""")

    var= int(input())

if var==1:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1+numero2
    print("su suma =  ", Resultado )

if var==2:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1-numero2
    print("su resta =  ", Resultado )

if var==3:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1*numero2
    print("su multiplicacion = ", Resultado )

if var==4:
    numero1= int(input("Ingrese un numero "))
    numero2= int(input("Ingrese otro numero "))
    Resultado= numero1/numero2
    print("la division = " ", Resultado )

if var==5:
    a= int(input("Ingrese numero 1 "))
b= int(input("Ingrese numero 2 "))
c= int(input("ingrese numero 3 "))

if(a==b and a==c):
    print("Son iguales")
elif a>b and a>c:
    print("El numero 1 es mayor")
elif b>a and b>c:
    print("El numero 2 es mayor")
else:
    print("El numero 3 es mayor")

if a==b and a!=c:
    print("El numero 1 y 2 son iguales pero son diferentes del numero 3")
elif b==c and b!=a:
    print("El numero 2 y 3 son iguales pero son diferentes del numero 1 ")
elif a==C and c!=b:
    print("El numero 1 y 3 son iguales pero son diferentes del numero 2")

if var==6:
    Cantidad= float(input("Dame una cantidad"))
    IVA= float( input("Dame el IVA"))
    Resultado= Cantidad*IVA;
    print("Tu cantidad es: ", Cantidad, "y tu IVA es ", IVA,
            "Tu cantidad total es: ", Resultado)

if var==7:
    print("Que tabla quieres?")
    a=int(input())
    var= int(input("Hasta que numero"))
    for var in range(1, var+1):
        print(var, "x= ",a, var*a)

if var==7:
    print("Pulsa enter.")
input(".......")
