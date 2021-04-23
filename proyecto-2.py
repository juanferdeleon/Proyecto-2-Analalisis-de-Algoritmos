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
    for char in strng:
        print("\n\nLista de Configuracion: ", symboltable)
        print("Configuracion de la Lista (Previo a Solicitud): ", pad)
        print("Solicitud: ", char)
        indx = pad.index(char) # Encuentra el indice de la solicitud en la lista de configracion
        sequence.append(indx) # Lo agrega a la secuencia
        pad = [pad.pop(indx)] + pad # Modifica la lista de configuracion
        print("Configuracion de la Lista  (Luego a Solicitud): ", pad)
        print("Secuencia: ", sequence)
    return sequence
 
if __name__ == '__main__':
    for s in ['01234012340123401234','43210123432101234', '22222222222222222222', '33333333333333333333']:
        print("\nSecuancia de solicitudes: ", s)
        encode = move2front(s, SYMBOLTABLE)
        print("\nLa secuencia de solicitudes ", s, " devuelve la secuencia ", encode, "\n")