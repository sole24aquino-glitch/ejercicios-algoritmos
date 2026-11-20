def mostrar_linea():
    n = int(input("Ingrese n (1 a 10): "))
    m = int(input("Ingrese m (1 a 10): "))
    if 1 <= n <= 10 and 1 <= m <= 10:
        nombre = f"tabla-{n}.txt"
        try:
            with open(nombre, "r") as archivo:
                lineas = archivo.readlines()
                print(lineas[m - 1].strip())
        except FileNotFoundError:
            print(f"El fichero {nombre} no existe.")
    else:
        print("Ambos números deben estar entre 1 y 10.")

mostrar_linea()