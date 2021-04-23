# Análisis y Diseño de Algoritmos

## Creado por:

- #### [Maria Jose Castro 181202](https://github.com/iconicmajo)

- #### [Juan Fernando De Leon Quezada 17822](https://github.com/juanferdeleon)

- #### [Josue Sagastume 18173](https://github.com/JosueS22)

### Instrucciones:

Investigue sobre el algoritmo MTF y realice un programa en Python en el que se calculen los costos de acceso totales del algoritmo MTF (Move to Front) sobre las siguientes secuencias de solicitudes:

1. Calcular el costo de acceso utilizando el algoritmo MTF para
   1. Lista de configuración: 0, 1, 2, 3, 4
   2. Secuencia de solicitudes: 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4

Imprima la lista de configuración, la solicitud, su costo y la configuración de la lista aplicando MTF por cada solicitud en la secuencia y, al final, imprima el costo total de los accesos.

2. Calcular el costo de acceso utilizando el algoritmo MTF para
   1. Lista de configuración: 0, 1, 2, 3, 4
   2. Secuencia de solicitudes: 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4

Imprima la lista de configuración, la solicitud, su costo y la configuración de la lista aplicando MTF por cada solicitud en la secuencia y, al final, imprima el costo total de los accesos.

3. ¿Para qué secuencia de 20 solicitudes se obtiene el mínimo costo total de acceso utilizando el algoritmo MTF para la configuración 0, 1, 2, 3, 4? ¿Cuál sería ese costo total de acceso?

4. ¿Para qué secuencia de 20 solicitudes se obtiene el peor de los casos utilizando el algoritmo MTF para la configuración 0, 1, 2, 3, 4? ¿Cuál sería ese costo total de acceso?

5. Calcular el costo de acceso utilizando el algoritmo MTF para
   1. Lista de configuración: 0, 1, 2, 3, 4
   2. Secuencia de solicitudes: 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2

Imprima la lista de configuración, la solicitud, su costo y la configuración de la lista aplicando MTF por cada secuencia de solicitudes y al final el costo total de acceso, Si se hiciera la secuencia de solicitudes 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 , ¿cuál es el costo total de acceso? ¿Se observa algún patrón cuando hay una repetición de 16 elementos en la secuencia?

6. Se plantea un algoritmo mejorado de MTF: IMTF por Rakesh Mohanty y Sasmita Tripathy, basado en el concepto de mirada hacia adelante (look-ahead), en el cual, después de acceder al elemento de la posición 𝑖 en la lista de configuración, se mueve el elemento al frente de la lista si y sólo si este elemento está en los próximos 𝑖−1 elementos del elemento accedido en la solicitud de secuencia. En caso contrario, el elemento accedido no se mueve al frente de la lista de configuración. Imprima la lista de configuración, la solicitud, su costo y la configuración de la lista aplicando IMTF por cada solicitud en la secuencia. Al final, imprima el costo total de acceso usando IMTF para el mejor y el peor de los casos de MTF.
