
import time
##Se definen los arreglos para el numero de pisos del edificio
## se define el arreglo de pisos que se van a ejecutar inicialmente
pisos1 = []
pisos2 = []
arregloDePisos = []

def llenarPisos():
    for n in range(1, 30, 1):
        pisos1.append(n)
        pisos2.append(n)

#compruebo si el piso actual está en el arreglo de pisos
def pisoEnArreglo(piso, arreglo):
    cont = 0
    pisoCorrecto = False
    while pisoCorrecto == False:
        #recorre el arreglo de pisos llamados 
        for _ in arreglo:
            #si el piso actual es uno del arreglo interrumpe el ciclo for
            if piso == arreglo[cont]:
                pisoCorrecto = True
                break
            cont += 1
        #si el piso no se encuentra en el arreglo, interrumpe el ciclo while pero retorna False para usarlo desde otra función
        if pisoCorrecto == False:
            break
    return pisoCorrecto

def eliminarPiso(piso, arreglo):
    arreglo.remove(piso)

#recibe un arreglo y valida si el usuario va a ingresar más pisos o no
def ingresarPiso(arreglo):
    print(arreglo)
    abierto = True
    while abierto:
        print('pedir piso? s/n')
        if input() =='s':
            #agrega el input tipo int al arreglo
            arreglo.append(int(input()))
        else:
            #cierra el ascensor
            abierto = False


    

#metodo para mover el ascensor, pide los dos arreglos: el de pisos totales y el de pisos pedidos
def moverAscensor(pisoActual, ascensor, pisosPedidos):
    if len(pisosPedidos) == 0:
        ingresarPiso(pisosPedidos)
        
    while len(pisosPedidos) != 0:
        time.sleep(0.5)
        print('piso actual: ', ascensor[pisoActual-1])
        pisoPedido = pisosPedidos[0]
        while pisoEnArreglo(pisoActual, pisosPedidos):
            eliminarPiso(ascensor[pisoActual-1], pisosPedidos)
            print('elevador se detiene en ', ascensor[pisoActual-1])
            ingresarPiso(pisosPedidos)
            break
        if ascensor[pisoActual-1] < pisoPedido:
            print('subiendo elevador')
            pisoActual += 1
        if ascensor[pisoActual-1] > pisoPedido:
            print('bajando el asensor')
            pisoActual -= 1
            

llenarPisos()
moverAscensor(4, pisos, arregloDePisos)