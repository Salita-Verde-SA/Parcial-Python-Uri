
filas=10
columnas=5
detallesFactura=[[0 for _ in range(columnas)] for _ in range(filas)]
#Codigo articulo
detallesFactura[0][0]=101
detallesFactura[1][0]=102
detallesFactura[2][0]=103
detallesFactura[3][0]=104
detallesFactura[4][0]=105
detallesFactura[5][0]=106
detallesFactura[6][0]=107
detallesFactura[7][0]=108
detallesFactura[8][0]=109
detallesFactura[9][0]=110

#Nombre articulo (columna 2)
detallesFactura[0][1]="Leche"
detallesFactura[1][1]="Gaseosa"
detallesFactura[2][1]="Fideos"
detallesFactura[3][1]="Arroz"
detallesFactura[4][1]="Vino"
detallesFactura[5][1]="Manteca"
detallesFactura[6][1]="Lavandina"
detallesFactura[7][1]="Detergente"
detallesFactura[8][1]="Javon en Polvo"
detallesFactura[9][1]="Galletas"

#Cantidad (columna 3)
detallesFactura[0][3]=250
detallesFactura[1][3]=300
detallesFactura[2][3]=150
detallesFactura[3][3]=280
detallesFactura[4][3]=1200
detallesFactura[5][3]=200
detallesFactura[6][3]=180
detallesFactura[7][3]=460
detallesFactura[8][3]=960
detallesFactura[9][3]=600

for fila in detallesFactura:
    print(fila)
clientes = {"20110425417":"Rodolfo Fernandez",
            "30527419655":"Los Pollos Hnos", 
           "27289425478": "Andrea Pereira", 
            "33536549878":"Multimarca Repuestos",
            "20291122568":"Luis Peric " }

#Solicitud de datos
fechaFactura=input("Ingrese la fecha de factura en formato DD/MM/AA: ")
numeroFactura=int(input("Ingrese el numero de factura: "))
letraFactura=""
totalFactura=0.0
montoIva=0.0
clienteFactura=""
z= True
while z==True:
    cuil_cliente=input("Ingrese su CUIL: ")
    digitos_iniciales=("20","27","30","33")
    if cuil_cliente.startswith(digitos_iniciales):
        if cuil_cliente in clientes:
            clienteFactura=clientes[cuil_cliente]
        else:
            clienteFactura="Consumidor Final"
        z=False
    else:
        print("CUIL no registrado (INGRESE OTRO)!!! ")
def encontrar_indice(codigo,matriz):
    for i,fila in enumerate(matriz):
        for j,elemento in enumerate(fila):
            if elemento==codigo:
                return i
def verificar_codigo_en_matriz(codigo,matriz):
    for filas in matriz:
        for elementos in filas:
            if codigo==elementos:
                return True

def calcular_total(matriz):
    suma=0
    for i in range(len(matriz)):
        suma+=matriz[i][4]
        
    return suma
        
            
            
z=True
while z==True:
        codigo_art_cliente=int(input("Ingrese el codigo de el articulo a facturar \n .Si desea salir ingrese 000: "))
        if codigo_art_cliente==000:
            z=False
        else:
              if verificar_codigo_en_matriz(codigo_art_cliente,detallesFactura):
                 cantidad_art=int(input("Ingrese la cantidad de articulos: "))
                 indice_codigo=encontrar_indice(codigo_art_cliente,detallesFactura)
                 detallesFactura[indice_codigo][2]=cantidad_art
                 detallesFactura[indice_codigo][4]=cantidad_art*detallesFactura[indice_codigo][3]
              else:
                  print("CODIGO INCORRECTO!!!")
        

#IVA
total=calcular_total(detallesFactura)
sinIva=("20","27")
conIva=("30","33")
if cuil_cliente.startswith(sinIva):
    montoIva=0
if cuil_cliente.startswith(conIva):
    montoIva=total * 0.21
    

     
#Letra Factura
if cuil_cliente.startswith(sinIva) or clienteFactura=="Consumidor Final":
    letraFactura="B"
if cuil_cliente.startswith(conIva):
    letraFactura="A"

#Total Factura (el caso B es sin IVA y al A con IVA)
if letraFactura=="B":
    total=total
if letraFactura=="A":
    total+=montoIva
#Impresion de datos
print("------------------------------------------------------------------------------------------------")
print(f".FECHA: {fechaFactura}   .NUMERO: {numeroFactura}   .LETRA: {letraFactura}    .CLIENTE: {clienteFactura}")
print()
print("Codigo Articulo: CA / Nombre Articulo: NA / Cantidad: C / Precio Unitario: PU / Subtotal: S")
print("------------------------------------------------------------------------------------------------")
print(" CA |  NA  |  C  |  PU  |  S")
for fila in detallesFactura:
    print(fila)
print()
print(f"  .IVA: {montoIva} \n  .TOTAL: {total}")

