def suma2():
    a = int(input("Ingresar un número: "))
    b = int(input("Ingresar otro número: "))
    print("El resultado es:", a + b)


def suma4():
    a = int(input("Ingresar un número: "))
    b = int(input("Ingresar un segundo número: "))
    c = int(input("Ingresar un tercer número: "))
    d = int(input("Ingresar un cuarto número: "))
    print("El resultado es:", a + b + c + d)


def rectangulo():
    base = int(input("Ingresar un lado: "))
    altura = int(input("Ingresar otro lado: "))
    print("La superficie del rectángulo es:", base * altura)


def cuadrado():
    lado = float(input("Ingresar el lado: "))
    print("La superficie del cuadrado es:", lado * lado)


def a_segundos():
   
    horas = int(input("Ingresar las horas: "))
    minutos = int(input("Ingresar los minutos: "))
    segundos = int(input("Ingresar los segundos: "))
    total = horas * 3600 + minutos * 60 + segundos
    print("El resultado en segundos es:", total)


def triangulo():
    DOS = 2
    base = float(input("Ingresar la base: "))
    altura = float(input("Ingresar la altura: "))
    print("La superficie del triángulo es:", base * altura / DOS)


def promedio():
    CANTIDAD = 6
    suma = 0
    for i in range(CANTIDAD):
        suma += float(input("Ingresar un número: "))
    print("El promedio es:", suma / CANTIDAD)


def porcentaje():
    
    parcial = int(input("Ingresar la cantidad parcial: "))
    total = int(input("Ingresar la cantidad total: "))
    print("El porcentaje es:", parcial / total * 100)


def fecha():
    n = int(input("Ingresar fecha (DDMMAAAA): "))
    dia = n // 1000000
    mes = n % 1000000 // 10000
    anio = n % 10000
    print("Día:", dia, "Mes:", mes, "Año:", anio)


def nota_final():
    parciales = float(input("Nota de exámenes parciales: "))
    practicos = float(input("Nota de trabajos prácticos: "))
    integrador = float(input("Nota del examen integrador: "))
    final = parciales * 0.3 + practicos * 0.2 + integrador * 0.5
    print("Su nota final es:", final)


def salario():
    BASE = 5500
    POR_AUTO = 200
    PORCENTAJE = 0.05
    autos = int(input("Cantidad de autos vendidos: "))
    valor = float(input("Valor de venta de la unidad: "))
    total = BASE + autos * POR_AUTO + autos * valor * PORCENTAJE
    print("Su salario total es de:", total)