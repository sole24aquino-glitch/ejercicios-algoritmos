def mostrar_tabla():
    num = int(input("Ingrese un número entre 1 y 10: "))
    if 1 <= num <= 10:
        nombre = f"tabla-{num}.txt"
        try:
            with open(nombre, "r") as archivo:
                print(archivo.read())
        except FileNotFoundError:
            print(f"El fichero {nombre} no existe.")
    else:
        print("El número debe estar entre 1 y 10.")

mostrar_tabla()