import json

usuarios = []


def validar_texto(mensaje):
    while True:
        texto = input(mensaje)

        if not texto.replace(" ", "").isalpha():
            print("El texto debe contener solamente letras.")
            continue
        return texto


def agregar_usuario():
    nombre = validar_texto("Ingresa tu nombre: ")
    while True:
        try:
            edad = int(input("Ingresa tu edad: "))
            if edad < 1 or edad > 120:
                print("Edad inválida.")
                continue
            break
        except ValueError:
            print("Debes ingresar un número")

    ciudad = validar_texto("Ingresa tu ciudad: ")
    print("")

    usuario = {"nombre": nombre, "edad": edad, "ciudad": ciudad}

    usuarios.append(usuario)
    guardar_usuarios()


def mostrar_usuarios():
    if not usuarios:
        print("No hay usuarios registrados")
    else:
        for usuario in usuarios:
            print("Nombre:", usuario["nombre"])
            print("Edad:", usuario["edad"])
            print("Ciudad:", usuario["ciudad"])
            print("")


def guardar_usuarios():
    with open("usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo)


def cargar_usuarios():
    global usuarios
    try:
        with open("usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        print("No existen usuarios...")


def eliminar_usuario(usuario_encontrado):
    usuarios.remove(usuario_encontrado)
    print("Usuario eliminado...")


def editar_usuario(usuario_encontrado):
    while True:
        try:
            opcion = int(
                input("¿Qué deseas editar? 1.Nombre 2.Edad 3.Ciudad: ")
            )
        except ValueError:
            print("Debes ingresar un número.")
            continue

        if opcion in (1, 2, 3):
            break
        print("Opción no válida.")

    if opcion == 1:
        nombre = validar_texto("Ingresa el nuevo nombre: ")
        usuario_encontrado["nombre"] = nombre

    elif opcion == 2:
        while True:
            try:
                edad = int(input("Ingresa la nueva edad: "))

                if edad < 1 or edad > 120:
                    print("Edad inválida.")
                    continue

                usuario_encontrado["edad"] = edad
                break

            except ValueError:
                print("Debes ingresar un número.")

    elif opcion == 3:
        ciudad = validar_texto("Ingresa la nueva ciudad: ")
        usuario_encontrado["ciudad"] = ciudad

    print("Usuario actualizado:")
    print(usuario_encontrado)


def encontrar_usuario(nombre):
    for usuario in usuarios:
        if nombre.lower() == usuario["nombre"].lower():
            return usuario
    return None


def leer_opcion_binaria(mensaje):
    """Pide 1 o 2 y repite hasta recibir una opción válida (no crashea con texto)."""
    while True:
        try:
            opcion = int(input(mensaje))
        except ValueError:
            print("Opción no válida.")
            continue
        if opcion in (1, 2):
            return opcion
        print("Opción no válida.")


def menu_usuario(usuario):
    while True:
        print("1. Editar usuario")
        print("2. Eliminar usuario")
        print("3. Volver")
        try:
            opcion = int(input("Ingresa la opción: "))
        except ValueError:
            print("Opcion no valida")
            continue

        if opcion == 1:
            confirmar_edicion = leer_opcion_binaria(
                "Deseas editar el usuario? Sí = 1 / No = 2: "
            )
            if confirmar_edicion == 1:
                editar_usuario(usuario)
                guardar_usuarios()
            else:
                print("Operación cancelada.")
                break

        elif opcion == 2:
            confirmar_eliminacion = leer_opcion_binaria(
                "Deseas eliminar el usuario? Sí = 1 / No = 2: "
            )
            if confirmar_eliminacion == 1:
                eliminar_usuario(usuario)
                guardar_usuarios()
                break
            else:
                print("Operación cancelada.")
                break

        elif opcion == 3:
            break


def buscar_usuario():
    nombre = validar_texto("Ingresa el nombre que deseas buscar: ")
    usuario_encontrado = encontrar_usuario(nombre)
    if usuario_encontrado is not None:
        menu_usuario(usuario_encontrado)
    else:
        print("Usuario no encontrado")


cargar_usuarios()  # carga automática al iniciar el programa

while True:
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Cargar usuarios")
    print("4. Buscar usuario")
    print("5. Salir")

    try:
        opcion = int(input("Elige una opción: "))
        print("")
    except ValueError:
        print("Debes ingresar un número.")
        continue

    if opcion == 1:
        agregar_usuario()
    elif opcion == 2:
        mostrar_usuarios()
    elif opcion == 3:
        cargar_usuarios()
    elif opcion == 4:
        buscar_usuario()
    elif opcion == 5:
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")