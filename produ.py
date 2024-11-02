productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    productos.append({'nombre': nombre, 'precio': precio})
    print(f"Producto '{nombre}' añadido con éxito.")

def ver_productos():
    if not productos:
        print("No hay productos disponibles.")
    else:
        for i, producto in enumerate(productos):
            print(f"{i + 1}: {producto['nombre']} - ${producto['precio']:.2f}")

def actualizar_producto():
    ver_productos()
    indice = int(input("Selecciona el número del producto a actualizar: ")) - 1
    if 0 <= indice < len(productos):
        nuevo_nombre = input("Introduce el nuevo nombre del producto: ")
        nuevo_precio = float(input("Introduce el nuevo precio del producto: "))
        productos[indice] = {'nombre': nuevo_nombre, 'precio': nuevo_precio}
        print("Producto actualizado con éxito.")
    else:
        print("Índice inválido.")

def eliminar_producto():
    ver_productos()
    indice = int(input("Selecciona el número del producto a eliminar: ")) - 1
    if 0 <= indice < len(productos):
        eliminado = productos.pop(indice)
        print(f"Producto '{eliminado['nombre']}' eliminado con éxito.")
    else:
        print("Índice inválido.")

def guardar_datos():
    with open('productos.txt', 'w') as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']}\n")
    print("Datos guardados con éxito.")

def cargar_datos():
    try:
        with open('productos.txt', 'r') as file:
            for linea in file:
                nombre, precio = linea.strip().split(',')
                productos.append({'nombre': nombre, 'precio': float(precio)})
        print("Datos cargados con éxito.")
    except FileNotFoundError:
        print("No se encontraron datos previos.")

def menu():
    cargar_datos()  # Cargar datos al iniciar
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
