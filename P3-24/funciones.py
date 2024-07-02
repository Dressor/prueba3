"""
Puede escribir aqui las funciones del codigo
Se importaran de forma automatica al 'main.py'
"""
# ------ NO BORRAR -----
def test () -> None:
    """
        Funcion para probar el archivo
    """
    import herramientas
    menu = herramientas.load_items('menu.csv')
    print(menu)

# esto es para que test solo corra si es ejecutado directamente
if __name__ == '__main__':
    test()
# ------ NO BORRAR -----

#Escribir Funciones desde aqui hacia abajo ------------
carrito_usuario = []
#ejemplo de funcion
def revisar_menu(lista_menu):

    while True:
        opcion = input("Desea agregar algo mas a su carrito de compras? (y/n): ")
        if opcion == "y":
            item = input("Seleccione la comida para agregar al carro: ")
            for elemento in lista_menu:
                if item in elemento.values():
                    carrito_usuario.append(elemento)
        if opcion == "n":
            break

def buscar_ingrediente(lista_carrito,ingrediente):
    for comida in lista_carrito:
        ing = comida["ingredientes"]
        if ingrediente in ing:
            print(comida)

def calcular_total(carrito_usuario):
    total = sum(item['precio']for item in carrito_usuario)
    return total, len(carrito_usuario)

def sugerir_propina(total):
    propina = total * 0,1
    return propina

def pagar(carrito_usuario):
    total = calcular_total(carrito_usuario)
    propina = sugerir_propina(total)
    print("La propina sugerida es: ", propina)
    opcion = input("Desea aceptar esta propina?s/n: ").lower()
    if opcion == "s":
        print(total)
    if opcion == "n":
        print("Muchas gracias por tu compra!! ")
        return


