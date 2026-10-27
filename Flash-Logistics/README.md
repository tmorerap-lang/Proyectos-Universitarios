🚚 FLASH LOGISTICS — Sistema de asistencia vehicular
📌 Descripción
FLASH LOGISTICS es un proyecto académico desarrollado en Python para representar un sistema básico de asistencia vehicular. Permite registrar solicitudes de clientes, administrar rutas y repuestos, consultar una matriz de cobertura, organizar solicitudes por prioridad y mantener un historial limitado de las solicitudes consultadas.

El programa funciona mediante menús en la terminal y utiliza estructuras de datos implementadas en el propio código.
🎯 Objetivos
- Practicar la implementación de estructuras de datos lineales.
- Aplicar recorridos, búsquedas, inserciones, modificaciones y eliminaciones.
- Organizar solicitudes según un valor de prioridad.
- Representar información de cobertura mediante una matriz.
- Comprender el funcionamiento de un historial LRU.
🛠️ Tecnologías
- Lenguaje: Python 3
- Interfaz: terminal/consola
- Conceptos: clases, objetos, funciones, condicionales, ciclos, listas enlazadas, matrices y manejo básico de excepciones.
▶️ Cómo ejecutar
1. Guarda el código en un archivo llamado flash_logistics.py.
2. Abre una terminal en la carpeta donde guardaste el archivo.
3. Ejecuta:
python3 flash_logistics.py
El menú principal permite entrar a cada módulo. Para cerrar el programa, selecciona la opción 7. Salir.
🧭 Menú principal
Opción	Módulo	Para qué sirve
1	Gestionar solicitudes	Registrar, consultar, buscar, editar, cambiar el estado, eliminar y contar solicitudes.
2	Gestionar rutas	Agregar, mostrar, recorrer, buscar y eliminar paradas.
3	Gestionar inventario	Registrar y consultar repuestos, editar datos, cambiar cantidades y eliminar registros.
4	Consultar cobertura	Mostrar la matriz de disponibilidad y buscar una alternativa de apoyo cercana.
5	Organizar solicitudes	Demostrar la fusión y partición de listas por prioridad.
6	Historial de solicitudes	Consultar y administrar el buffer LRU de solicitudes consultadas.
7	Salir	Finalizar el programa.


🧱 Estructuras de datos
1. Solicitudes — lista simplemente enlazada
Las solicitudes se guardan en nodos. Cada nodo contiene el identificador, cliente, vehículo, zona, falla, urgencia, estado y una referencia al siguiente nodo.

La clase Solicitudes mantiene la referencia inicio, que apunta al primer nodo. Para recorrer la lista, el programa avanza usando actual = actual.siguiente hasta llegar a None.

Operaciones principales:
- registrar(): solicita los datos y agrega la solicitud al final. Evita registrar un ID que ya exista.
- mostrar(): recorre e imprime todas las solicitudes.
- buscar(id_solicitud, mostrar=True): recorre la lista y devuelve el nodo encontrado o None.
- editar(): permite actualizar cliente, vehículo, zona y falla. Si se pulsa ENTER, conserva el dato actual.
- cambiar_estado(): muestra el estado actual y permite escribir el nuevo estado.
- eliminar(): desconecta el nodo que coincide con el ID.
- contar(): cuenta los nodos recorriendo la lista.
Cómo explicarlo: una lista simplemente enlazada permite avanzar de un nodo al siguiente, pero no retroceder directamente.
2. Rutas — lista circular
Cada NodoRuta almacena el nombre de una parada y una referencia siguiente. En una lista circular, el último nodo vuelve a apuntar al primero.

Cuando se agrega la primera parada, nuevo.siguiente = nuevo; así, el nodo se enlaza consigo mismo. Al agregar más paradas, el último nodo apunta al nuevo y el nuevo vuelve a apuntar a inicio.

Operaciones principales: agregar, mostrar, recorrer, buscar, eliminar y contar paradas.

Cómo explicarlo: se usa una lista circular porque una ruta puede recorrerse continuamente. Los recorridos terminan cuando el puntero vuelve a inicio; por eso se usa while True con una condición de salida.
3. Inventario — lista doblemente enlazada
Cada NodoRepuesto contiene código, nombre, bodega, cantidad y dos referencias:
- anterior: nodo previo.
- siguiente: nodo siguiente.
La clase Inventario mantiene inicio y ultimo. Esto permite recorrer los repuestos desde el primero hacia adelante o desde el último hacia atrás.

Operaciones principales: registrar, mostrar, mostrar hacia atrás, buscar, editar, actualizar cantidad, eliminar y contar.

Al eliminar un nodo, el programa reconecta los vecinos. Si el nodo es el primero, actualiza inicio; si es el último, actualiza ultimo.

Cómo explicarlo: a diferencia de la lista simple, la lista doble permite moverse en ambas direcciones, porque cada nodo conoce a su anterior y a su siguiente.
📊 Punto 1 — Matriz de cobertura
La variable cobertura_auxilios contiene valores de disponibilidad para tres bodegas y cuatro zonas:
- Filas: Bodega Norte, Bodega Centro y Bodega Sur.
- Columnas: Zona 1, Zona 2, Zona 3 y Zona 4.
generar_reporte_consolidado() crea una tabla con los totales de cada bodega, los totales de cada zona y el total general. mostrar_cuadro_disponibilidad() presenta la tabla en la terminal.

buscar_bases_limitrofes_y_mejor_apoyo() solicita una bodega y una zona, revisa las posiciones vecinas válidas (arriba, abajo, izquierda y derecha) y selecciona la de mayor valor.

Cómo explicarlo: la matriz permite consultar la disponibilidad en la intersección entre una bodega y una zona. La búsqueda compara únicamente las celdas vecinas de la posición seleccionada.

Importante: los datos de la matriz están escritos directamente en el código; no se modifican desde el menú en esta versión.
🔀 Punto 2 — Organización de solicitudes
Este módulo usa una estructura enlazada independiente, ListaOrganizacion, cuyos nodos guardan ID, zona, repuesto y prioridad.

En los ejemplos, un número menor representa una prioridad numéricamente menor. La función fusionar(lista_a, lista_b) compara las prioridades de las dos listas y construye una nueva lista en orden ascendente. Para que el resultado se mantenga ordenado, las dos listas de entrada deben estar previamente ordenadas.

La función particionar(lista, pivote) recorre una lista y crea dos listas nuevas:
- menores: elementos cuya prioridad es menor que el pivote.
- mayores: elementos cuya prioridad es igual o superior al pivote.
El menú usa datos de ejemplo para mostrar el comportamiento de las operaciones.

Cómo explicarlo: fusionar combina dos secuencias ordenadas comparando sus elementos; particionar divide los elementos según una condición. En esta implementación se copian los datos a nodos nuevos, no se mueven los nodos originales.
🕘 Punto 3 — Historial LRU
LRU significa Least Recently Used, es decir, “menos recientemente utilizado”. En este programa se usa una lista doble como un buffer limitado de solicitudes que el usuario ha consultado.

La clase ListaSolicitudesLRU tiene una capacidad máxima. En el menú principal se crea con capacidad 3:
- raiz es el inicio y representa la solicitud más recientemente usada.
- ultimo es el final y representa la menos recientemente usada.
- tamano indica cuántos registros hay almacenados.
Funcionamiento:
1. Cuando se busca una solicitud desde el menú de solicitudes y se encuentra, se agrega al buffer.
2. Si ya estaba en el buffer, se actualizan algunos datos y se mueve al inicio.
3. Si el buffer supera su capacidad, se elimina el nodo del final.
4. Se puede recorrer desde recientes a antiguas o al revés.
5. buscar_iesimo() puede empezar desde el inicio o desde el final, según la posición solicitada.
6. También se puede editar, cambiar el estado o eliminar un registro del buffer.
Cómo explicarlo: el historial conserva las consultas recientes. Si está lleno y se incorpora otra solicitud, se elimina la que lleva más tiempo sin ser utilizada.

Importante: este historial es un buffer en memoria, no una base de datos permanente. Se pierde al cerrar el programa. Además, registra solicitudes consultadas desde la opción de búsqueda del menú de solicitudes; no registra automáticamente todas las solicitudes creadas.
🔗 Cómo se conectan los módulos
menu_principal() crea las estructuras principales y mantiene un ciclo que muestra las opciones hasta que el usuario decide salir. Cada opción llama al menú del módulo correspondiente.

La lista de solicitudes y el historial LRU sí están conectados: al buscar una solicitud y encontrarla, el menú envía el objeto al historial. Las rutas, el inventario, la matriz y el módulo de organización funcionan como módulos del mismo programa, pero sus datos no están automáticamente conectados entre sí en esta versión.
🧪 Pruebas manuales recomendadas
1. Solicitudes: registra dos solicitudes, muestra la lista, busca una por ID, edita un dato y elimina una.
2. Rutas: agrega tres paradas, muestra el recorrido, busca una y elimina otra.
3. Inventario: registra dos repuestos, muestra el inventario en ambos sentidos, actualiza una cantidad y elimina un repuesto.
4. Matriz: muestra el cuadro de disponibilidad y consulta una bodega y zona.
5. Organización: ejecuta la fusión y la partición con los ejemplos incluidos.
6. LRU: busca cuatro solicitudes distintas. Como la capacidad es tres, la más antigua debe salir del buffer cuando se agrega la cuarta.
7. Entradas inválidas: escribe texto donde se espera un número para comprobar las validaciones disponibles.
⚠️ Alcance y mejoras posibles
Esta versión es un proyecto académico de consola. Algunas mejoras futuras podrían ser:
- Validar que los estados de las solicitudes pertenezcan a opciones definidas.
- Validar rangos y valores negativos en las cantidades del inventario.
- Conectar las solicitudes con inventario y cobertura para que compartan información.
- Guardar los datos en archivos o una base de datos para conservarlos al cerrar el programa.
- Añadir pruebas automatizadas.
- Mejorar la validación de zonas, bodegas y prioridades.
📚 Resumen para una presentación
FLASH LOGISTICS es un sistema de consola en Python que reúne varias estructuras de datos para resolver tareas relacionadas con la asistencia vehicular. Usa una lista simple para solicitudes, una lista circular para rutas, una lista doble para inventario, una matriz para disponibilidad, listas enlazadas para practicar fusión y partición, y una lista doble con política LRU para mantener un historial limitado de consultas. El menú principal integra el acceso a estos módulos.
