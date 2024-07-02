# ------ NO BORRAR -----
from funciones import *
from herramientas import *
# ------ NO BORRAR -----

user = {}
menu = ["Revisar menú",
        "Ver Carrito",
        "Buscar item en carrito por ingredientes",
        "Modificar ítem del menú",
        "Pagar",
        "Salir"]


#menu principal


while (True):
    for i, opcion in enumerate(menu):
        print(f"{i+1}:{opcion}")
    
    while True:
        accion = int(input("Que acción desea realizar hoy?: "))
        seleccion = menu[accion-1]
        break

    print(seleccion)

    if accion == 1:
        revisar_menu(var)
    if accion == 2:
        if carrito_usuario:
            print(carrito_usuario)
        else:
            print("No se han agregado elementos al carrito")

    if accion == 3:
        while True:
            ingrediente = input("Que ingrediente quieres buscar: ")
            buscar_ingrediente(var,ingrediente)
            opcion = input("Quieres buscar otro ingrediente? (s/n): ")
            if opcion == "s":
                continue
            if opcion == "n":
                break
            
    if accion == 4:
        for i, elementos in enumerate(var):
            print(f"{i+1} , {elementos}\n")
        contraseña = input("Ingrese la contraseña: ")
        if check_password(contraseña):
            id = int(input("Ingrese id: "))
            selet = input("Que desea modificar (nombre,precio,kcal,ingredientes): ")
            producto = var[id-1]
            if selet in producto.keys():
                modificacion = input("IIngresa el nuevo dato: ")
                producto[selet] = modificacion
        print(var)

    if accion == 5:
        pagar(carrito_usuario)
  

    
    if accion == 6:
        salir = input("Desea finalizar el programa? (s, para salir) (n, para volver al menú)").lower()
        if salir == "n":
                continue
        if salir == "s":
         print(input("El programa terminará, presiona cualquier tecla para salir..."))
        break
        
    
    