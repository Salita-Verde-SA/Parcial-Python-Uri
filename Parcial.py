golosinas = [
    [1, "Kitkat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&M'S", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10],
]

empleados = {
    "1100": "Jose Alonso",
    "1200": "Federico Pacheco",
    "1300": "Nelson Pereira",
    "1400": "Osvaldo Tejada",
    "1500": "Gastón Garcia",
}

clave_tecnico = ("admin", "CCCDDD", "2020")

golosinasPedidas = []

def registro(codigo, golosina):
    for Pe in golosinasPedidas:
        if Pe[0] == codigo:
            # Pedido = [0codigo,1golosina,2suma]
            Pe[2] += 1
            return
    golosinasPedidas.append([codigo, golosina, 1])

def menu():
    opcion = input(
        """
        Menu
    1-Pedir golosina
    2-Mostrar golosinas
    3-Rellenar golosinas
    4-Apagar maquina
    """
    )
    return opcion

def pedir():
    emple = input("Ingrese el legajo: ")
    if emple in empleados:
        while True:
            codigo = int(input("Ingrese el codigo de la golosina: "))
            for fila in golosinas:
                if fila[0] == codigo:
                    if fila[2] > 0:
                        fila[2] -= 1
                        registro(codigo, fila[1])
                        print(f"A elegido: {fila[1]}")
                    else:
                        print(f"La golosina {fila[1]} no se encuentra disponible")
                    return
            print(
                "Codigo de golosina no valido. Intente de nuevo o ingrese 0 para salir"
            )
            if codigo == 0:
                break
    else:
        print("Usted no es un empleado")
        
def rellenar_golosinas():
    tecnico = input("Ingrese nombre de usuario: ")
    tecnico1 = input("Ingrese nombre de contraseña: ")
    tecnico2 = input("Ingrese nombre de año de iniciacion: ")
    if (tecnico, tecnico1, tecnico2) == clave_tecnico:
        codigo = int(input("Ingrese el codigo de la golosina que desea llenar: "))
        cant = int(input("Ingrese la cantida: "))
        for fila in golosinas:
            if fila[0] == codigo:
                fila[2] += cant
                return
    else:
        print("No puede entrar a este apartado.")
        return
    
def mostrar_golosinas():
    for i in golosinas:
        print(i)

def Apagarmaquina():
    print("Historial:")
    pedidas = 0
    total_golosinas = int(pedidas)
    for fila in golosinasPedidas:
        print(f"{fila[1]}: {fila[2]} unidades pedidas")
        total_golosinas += fila[2]
    print(f"Total de golosinas pedidas: {total_golosinas}")
    exit()

while True:
    opcion = menu()
    if opcion == "1":
        pedir()
    if opcion == "2":
        mostrar_golosinas()
    if opcion == "3":
        rellenar_golosinas()
    if opcion == "4":
        Apagarmaquina()
