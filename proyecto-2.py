'''
            Proyecto 2
    Análisis y Diseño de Algoritmos
        
Creado por:
    Maria Jose Castro               181202
    Juan Fernando De Leon Quezada   17822
    Josue Sagastume                 18173

'''

SYMBOLTABLE = ["0", "1", "2", "3", "4"]
 
def move2front(strng, symboltable):
    sequence, pad = [], symboltable[::]
    consto_total = 0
    for char in strng:
        print("\n\nLista de Configuracion: ", symboltable)
        print("Configuracion de la Lista (Previo a Solicitud): ", pad)
        print("Solicitud: ", char)
        indx = pad.index(char) # Encuentra el indice de la solicitud en la lista de configracion
        sequence.append(indx) # Lo agrega a la secuencia
        consto_unitario = indx + 1
        consto_total += consto_unitario 
        pad = [pad.pop(indx)] + pad # Modifica la lista de configuracion
        print("Configuracion de la Lista  (Luego a Solicitud): ", pad)
        print("Costo Unitario: ", consto_unitario)
        print("Secuencia: ", sequence)
    print("\nCosto total: ", consto_total)
    return sequence
 
if __name__ == '__main__':
    # a)
    secuencia_de_solicitudes = "01234012340123401234"
    print("\nSecuancia de solicitudes: ", secuencia_de_solicitudes)
    encode = move2front(secuencia_de_solicitudes, SYMBOLTABLE)
    print("\nLa secuencia de solicitudes ", secuencia_de_solicitudes, " devuelve la secuencia ", encode, "\n")

    # b)
    secuencia_de_solicitudes = "43210123432101234"
    print("\nSecuancia de solicitudes: ", secuencia_de_solicitudes)
    encode = move2front(secuencia_de_solicitudes, SYMBOLTABLE)
    print("\nLa secuencia de solicitudes ", secuencia_de_solicitudes, " devuelve la secuencia ", encode, "\n")

    # c) # Mejor de los casos
    secuencia_de_solicitudes = "00000000000000000000"
    print("\nSecuancia de solicitudes: ", secuencia_de_solicitudes)
    encode = move2front(secuencia_de_solicitudes, SYMBOLTABLE)
    print("\nLa secuencia de solicitudes ", secuencia_de_solicitudes, " devuelve la secuencia ", encode, "\n")

    # d) Peor de los casos
    secuencia_de_solicitudes = "43210432104321043210"
    print("\nSecuancia de solicitudes: ", secuencia_de_solicitudes)
    encode = move2front(secuencia_de_solicitudes, SYMBOLTABLE)
    print("\nLa secuencia de solicitudes ", secuencia_de_solicitudes, " devuelve la secuencia ", encode, "\n")

    # e) 
    secuencia_de_solicitudes = "22222222222222222222"
    print("\nSecuancia de solicitudes: ", secuencia_de_solicitudes)
    encode = move2front(secuencia_de_solicitudes, SYMBOLTABLE)
    print("\nLa secuencia de solicitudes ", secuencia_de_solicitudes, " devuelve la secuencia ", encode, "\n")

    # e.2) 
    secuencia_de_solicitudes = "33333333333333333333"
    print("\nSecuancia de solicitudes: ", secuencia_de_solicitudes)
    encode = move2front(secuencia_de_solicitudes, SYMBOLTABLE)
    print("\nLa secuencia de solicitudes ", secuencia_de_solicitudes, " devuelve la secuencia ", encode, "\n")