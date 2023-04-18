from examen_libros import *
from titulo import *
while True:
    print("Opciones")
    print("1. Ver todos los libros")
    print("3. Insertar un libro")
    print("4. Actualizar un libro")
    print("5. eliminar un libro")
    print("6. Salir del sistema")
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        read_titulos()
    elif opcion == "2":
        id = int(input("Ingres el ID a insertar: "))
        read_publicacion(id)
    elif opcion == "3":
        titulo = create_json_titulos()
        create_titulos(titulo)
    elif opcion == "4":
        id = int(input("Ingres el ID a actualizar: "))
        titulo = create_json_update()
        update_titulos(id, titulo)
