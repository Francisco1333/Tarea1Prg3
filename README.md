# Informe de Resultados

| Estructura | Tiempo Promedio de Búsqueda | Memoria | Complejidad Teórica |
| 
| Tabla Hash | 0.001098 ms | Alta | O(1) |
| Arreglo Ordenado | 0.013979 ms | Media | O(log n) |

## Concluison 
En la tabla se muestra claramente una superioridad de tabla hash al ser menos tiempo de busqueda ya que va directo al dato ,
mientras un arreglo que primero ordena los datos de menor a mayor para luego hacer una busqueda binario ,
siendo esto mas tardado por los pasos que lleva consigo entre ordenes y descarte en complejida teorica el Arreglo ordenado tiende a tardar mas tiempo dependiendo la cantidad de datos usando una notacion Big o Logaritmica ,
aunque su tiempo crece de manera lenta ya que al duplicar datos solo crece un paso mas ya que parte y descarta por mitades 
, la Tabla Hash no ve la cantidad de datos siempre sera igual de eficiente por eso es el estandar mundial
