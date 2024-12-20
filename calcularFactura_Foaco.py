from colorama import Fore as fr


fechaFactura = ""
numeroFactura = 0
letraFactura = ""
totalFactura = 0.0
montoIva = 0.0
clienteFactura = ""
detallesFactura = []

def mostrar_lista(): 
    for i in articulos: 
        print(i)

articulos = [
    [101, "Leche", 250],
    [102, "Gaseosa", 300],
    [103, "Fideos", 150],
    [104, "Arroz", 280],
    [105, "Vino", 1200],
    [106, "Manteca", 200],
    [107, "Lavandina", 180],
    [108, "Detergente", 460],
    [109, "Jabón en Polvo", 960],
    [110, "Galletas", 600]
]

clientes = {
    "20110425417": "Rodolfo Fernandez",
    "30527419655": "Los Pollos Hnos",
    "27289425478": "Andrea Pereira",
    "33536549878": "Multimarca Repuestos",
    "20291122568": "Luis Peric"
}



def pedir_fecha ():
    global fechaFactura, numeroFactura
    print(fr.LIGHTBLUE_EX)
    fechaFactura = input("Ingrese la fecha de la Factura: ")
    numeroFactura = int(input("Ingrese el numero de la factura: "))
    print(fr.LIGHTWHITE_EX)

def pedir_cuit (): 
    global clienteFactura 
    pedirCuit = (input("Ingrese su cuit: "))

    if pedirCuit in clientes and (pedirCuit.startswith("20")or pedirCuit.startswith("27")or pedirCuit.startswith("30")or pedirCuit.startswith("33")):
        clienteFactura = clientes[pedirCuit]
        # print(clienteFactura)
    else:
        clienteFactura = "Consumidor Final"
        return pedirCuit
    
def producto_cont (): 

    global detallesFactura

    print(fr.LIGHTRED_EX,"Cod   Produc  Precio",fr.LIGHTWHITE_EX)
    mostrar_lista()

    while True:

        elejirProducto = int(input("Ingrese el codigo del producto o <0000> para terminar la compra: "))
        if elejirProducto == 0:
            break
        articulo = next((a for a in articulos if a[0] == elejirProducto), None)
        if articulo:
            cantidad_producto = int(input("Ingrese la cantidad del artículo: "))
            subtotal = cantidad_producto * articulo[2]
            detallesFactura.append([articulo[0], articulo[1], cantidad_producto, articulo[2], subtotal])
        else:
            print("Código Incorrecto, por favor ingrese nuevamente.")


def calcularTotal(): 
    return sum(a[4] for a in detallesFactura)


def calcularMontoIVa (cuit):

   
    global  montoIva, letraFactura
    
    total = calcularTotal()

    if cuit.startswith("30")or cuit.startswith("33"): 
        montoIva = total * 0.21
        letraFactura = "A"
    else: 
        montoIva = 0
        letraFactura = "B"

def calcular_totalFactura(): 
    global totalFactura 
    total = calcularTotal()
    if letraFactura == "B": 
        totalFactura = total + montoIva
    else: 
        totalFactura = total

    


def mostrar_factura ():
    print()
    print(fr.LIGHTRED_EX, "Fecha: ", fechaFactura, fr.LIGHTWHITE_EX)
    print(fr.LIGHTRED_EX,"Numero: ", numeroFactura, fr.LIGHTWHITE_EX)
    print(fr.LIGHTRED_EX, "Letra: ", letraFactura, fr.LIGHTWHITE_EX)
    print(fr.LIGHTYELLOW_EX, "Cliente: ", clienteFactura, montoIva, fr.WHITE)
    for detallesFac in detallesFactura: 
        print(f" Codigo de articulo:{fr.LIGHTYELLOW_EX} {detallesFac[0]}{fr.LIGHTWHITE_EX}, Nombre del articulo:{fr.LIGHTYELLOW_EX} {detallesFac[1]}{fr.LIGHTWHITE_EX}, Cantidad:{fr.LIGHTYELLOW_EX} {detallesFac[2]}{fr.LIGHTWHITE_EX}, Precio Unitario:{fr.LIGHTYELLOW_EX} {detallesFac[3]}{fr.LIGHTWHITE_EX}, TOTAL:{fr.LIGHTGREEN_EX} {detallesFac[4]}{fr.LIGHTWHITE_EX}")
    print(fr.LIGHTYELLOW_EX, "IVA: ", montoIva, fr.WHITE)
    print(fr.MAGENTA, "Total: ",totalFactura, fr.WHITE)


if __name__ == "__main__":
    pedir_fecha()
    cuit = pedir_cuit()
    producto_cont()
    calcularTotal()
    calcularMontoIVa(cuit)
    calcular_totalFactura()
    mostrar_factura()


# Me re costo boludo, no quiero massssss
