def create_json_titulos():
    title = input("titulo: ")
    author = input("nombre: ")

    titulos = {
        "title": title,
        "author": autor
    }
    return titulos


def create_json_update():
    print(" Opciones")
    print("1. Modificar todos los libros")
    print("2. Modificar un libro")
    opcion = input("Ingrese un libro: ")
    if opcion == "1":
        title = input("titulo: ")
        author = input("autor: ")

        titulos = {
            "title": title,
            "author": author,

        }
        return titulos
    elif opcion == "2":
        opciones = input("Ingrese las opciones")
        datos = input("Ingrese los datos a actualizados")
        titulos = {opciones: datos}
        return titulos
    else:
        print("Dato ingresado no validos")
