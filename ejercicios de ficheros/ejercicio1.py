def guardar_tabla():
    num = int(input("Ingrese un número entre 1 y 10: "))
    if 1 <= num <= 10:
        nombre = f"tabla-{num}.txt"
        with open(nombre, "w") as archivo:
            for i in range(1, 11):
              archivo.write(f"{num} x {i} = {num * i}\n")
        print(f"Tabla guardada en {nombre}")
    else:
        print("El número debe estar entre 1 y 10.")


guardar_tabla()