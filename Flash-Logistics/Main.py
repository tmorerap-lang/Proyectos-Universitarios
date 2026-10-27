# ============================================================
# FLASH LOGISTICS - SISTEMA DE ASISTENCIA VEHICULAR
# ============================================================


# ============================================================
# ESTRUCTURAS PRINCIPALES DEL PROYECTO
# ============================================================
# Solicitudes -> Lista simple
# Rutas       -> Lista circular
# Inventario  -> Lista doble
#
# Además se integran los 3 puntos de la presentación:
#
# PUNTO 1 -> Matriz de cobertura
# PUNTO 2 -> Organización de solicitudes
# PUNTO 3 -> Historial de solicitudes mediante LRU
# ============================================================


# ============================================================
# SOLICITUDES
# LISTA SIMPLE
# ============================================================

class NodoSolicitud:

    def __init__(self, id_solicitud, cliente, vehiculo,
                 zona, falla, urgencia):

        self.id_solicitud = id_solicitud
        self.cliente = cliente
        self.vehiculo = vehiculo
        self.zona = zona
        self.falla = falla
        self.urgencia = urgencia
        self.estado = "Pendiente"
        self.siguiente = None


class Solicitudes:

    def __init__(self):
        self.inicio = None

    # --------------------------------------------------------
    # REGISTRAR SOLICITUD
    # --------------------------------------------------------

    def registrar(self):

        print("\n--- REGISTRAR SOLICITUD ---")

        id_solicitud = input("ID de la solicitud: ")

        if self.buscar(id_solicitud, mostrar=False):
            print("Ya existe una solicitud con ese ID.")
            return

        cliente = input("Nombre del cliente: ")
        vehiculo = input("Vehículo: ")
        zona = input("Zona: ")
        falla = input("Falla del vehículo: ")

        print("\nNivel de urgencia:")
        print("1. Alta")
        print("2. Media")
        print("3. Baja")

        urgencia = input("Seleccione: ")

        while urgencia not in ["1", "2", "3"]:
            print("Opción inválida.")
            urgencia = input("Seleccione: ")

        if urgencia == "1":
            urgencia = "Alta"
        elif urgencia == "2":
            urgencia = "Media"
        else:
            urgencia = "Baja"

        nuevo = NodoSolicitud(
            id_solicitud,
            cliente,
            vehiculo,
            zona,
            falla,
            urgencia
        )

        if self.inicio is None:
            self.inicio = nuevo

        else:

            actual = self.inicio

            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo

        print("Solicitud registrada correctamente.")

    # --------------------------------------------------------
    # MOSTRAR SOLICITUDES
    # --------------------------------------------------------

    def mostrar(self):

        print("\n--- SOLICITUDES REGISTRADAS ---")

        if self.inicio is None:
            print("No hay solicitudes registradas.")
            return

        actual = self.inicio

        while actual is not None:

            print("\nID:", actual.id_solicitud)
            print("Cliente:", actual.cliente)
            print("Vehículo:", actual.vehiculo)
            print("Zona:", actual.zona)
            print("Falla:", actual.falla)
            print("Urgencia:", actual.urgencia)
            print("Estado:", actual.estado)

            actual = actual.siguiente

    # --------------------------------------------------------
    # BUSCAR SOLICITUD
    # --------------------------------------------------------

    def buscar(self, id_solicitud, mostrar=True):

        actual = self.inicio

        while actual is not None:

            if actual.id_solicitud == id_solicitud:

                if mostrar:

                    print("\nSolicitud encontrada:")
                    print("ID:", actual.id_solicitud)
                    print("Cliente:", actual.cliente)
                    print("Vehículo:", actual.vehiculo)
                    print("Zona:", actual.zona)
                    print("Falla:", actual.falla)
                    print("Urgencia:", actual.urgencia)
                    print("Estado:", actual.estado)

                return actual

            actual = actual.siguiente

        if mostrar:
            print("Solicitud no encontrada.")

        return None

    # --------------------------------------------------------
    # EDITAR SOLICITUD
    # --------------------------------------------------------

    def editar(self):

        print("\n--- EDITAR SOLICITUD ---")

        id_solicitud = input("ID de la solicitud: ")

        solicitud = self.buscar(id_solicitud, mostrar=False)

        if solicitud is None:
            print("Solicitud no encontrada.")
            return

        print("Presione ENTER para conservar el dato actual.")

        cliente = input("Cliente [" + solicitud.cliente + "]: ")
        vehiculo = input("Vehículo [" + solicitud.vehiculo + "]: ")
        zona = input("Zona [" + solicitud.zona + "]: ")
        falla = input("Falla [" + solicitud.falla + "]: ")

        if cliente != "":
            solicitud.cliente = cliente

        if vehiculo != "":
            solicitud.vehiculo = vehiculo

        if zona != "":
            solicitud.zona = zona

        if falla != "":
            solicitud.falla = falla

        print("Solicitud actualizada correctamente.")

    # --------------------------------------------------------
    # CAMBIAR ESTADO
    # --------------------------------------------------------

    def cambiar_estado(self):

        print("\n--- CAMBIAR ESTADO ---")

        id_solicitud = input("ID de la solicitud: ")

        solicitud = self.buscar(id_solicitud, mostrar=False)

        if solicitud is None:
            print("Solicitud no encontrada.")
            return

        print("\nEstado actual:", solicitud.estado)

        nuevo_estado = input(
            "Nuevo estado: "
        )

        estado_anterior = solicitud.estado

        solicitud.estado = nuevo_estado

        print("\nEstado actualizado.")
        print("Estado anterior:", estado_anterior)
        print("Estado actual:", solicitud.estado)

    # --------------------------------------------------------
    # ELIMINAR SOLICITUD
    # --------------------------------------------------------

    def eliminar(self):

        print("\n--- ELIMINAR SOLICITUD ---")

        id_solicitud = input("ID de la solicitud: ")

        actual = self.inicio
        anterior = None

        while actual is not None:

            if actual.id_solicitud == id_solicitud:

                if anterior is None:
                    self.inicio = actual.siguiente

                else:
                    anterior.siguiente = actual.siguiente

                print("Solicitud eliminada correctamente.")
                return

            anterior = actual
            actual = actual.siguiente

        print("Solicitud no encontrada.")

    # --------------------------------------------------------
    # CONTAR SOLICITUDES
    # --------------------------------------------------------

    def contar(self):

        contador = 0
        actual = self.inicio

        while actual is not None:

            contador += 1
            actual = actual.siguiente

        print("Cantidad de solicitudes:", contador)


# ============================================================
# RUTAS
# LISTA CIRCULAR
# ============================================================

class NodoRuta:

    def __init__(self, parada):

        self.parada = parada
        self.siguiente = None


class Rutas:

    def __init__(self):

        self.inicio = None

    # --------------------------------------------------------
    # AGREGAR PARADA
    # --------------------------------------------------------

    def agregar_parada(self):

        parada = input("Nombre de la parada/zona: ")

        nuevo = NodoRuta(parada)

        if self.inicio is None:

            self.inicio = nuevo
            nuevo.siguiente = nuevo

        else:

            actual = self.inicio

            while actual.siguiente != self.inicio:
                actual = actual.siguiente

            actual.siguiente = nuevo
            nuevo.siguiente = self.inicio

        print("Parada agregada correctamente.")

    # --------------------------------------------------------
    # MOSTRAR RUTA
    # --------------------------------------------------------

    def mostrar(self):

        print("\n--- RUTA COMPLETA ---")

        if self.inicio is None:
            print("No hay paradas registradas.")
            return

        actual = self.inicio

        while True:

            print("->", actual.parada)

            actual = actual.siguiente

            if actual == self.inicio:
                break

    # --------------------------------------------------------
    # RECORRER RUTA
    # --------------------------------------------------------

    def recorrer(self):

        print("\n--- RECORRIENDO RUTA ---")

        if self.inicio is None:
            print("No hay ruta registrada.")
            return

        actual = self.inicio

        while True:

            print("Vehículo pasando por:", actual.parada)

            actual = actual.siguiente

            if actual == self.inicio:
                break

    # --------------------------------------------------------
    # BUSCAR PARADA
    # --------------------------------------------------------

    def buscar(self):

        nombre = input("Parada a buscar: ")

        if self.inicio is None:
            print("No hay paradas.")
            return

        actual = self.inicio

        while True:

            if actual.parada.lower() == nombre.lower():

                print("Parada encontrada.")
                return

            actual = actual.siguiente

            if actual == self.inicio:
                break

        print("Parada no encontrada.")

    # --------------------------------------------------------
    # ELIMINAR PARADA
    # --------------------------------------------------------

    def eliminar(self):

        nombre = input("Parada a eliminar: ")

        if self.inicio is None:
            print("No hay paradas.")
            return

        actual = self.inicio
        anterior = None

        while True:

            if actual.parada.lower() == nombre.lower():

                if actual == self.inicio:

                    if actual.siguiente == self.inicio:

                        self.inicio = None

                    else:

                        ultimo = self.inicio

                        while ultimo.siguiente != self.inicio:
                            ultimo = ultimo.siguiente

                        self.inicio = actual.siguiente
                        ultimo.siguiente = self.inicio

                else:

                    anterior.siguiente = actual.siguiente

                print("Parada eliminada.")
                return

            anterior = actual
            actual = actual.siguiente

            if actual == self.inicio:
                break

        print("Parada no encontrada.")

    # --------------------------------------------------------
    # CONTAR PARADAS
    # --------------------------------------------------------

    def contar(self):

        if self.inicio is None:
            print("Cantidad de paradas: 0")
            return

        contador = 0
        actual = self.inicio

        while True:

            contador += 1
            actual = actual.siguiente

            if actual == self.inicio:
                break

        print("Cantidad de paradas:", contador)


# ============================================================
# INVENTARIO
# LISTA DOBLE
# ============================================================

class NodoRepuesto:

    def __init__(self, codigo, nombre, bodega, cantidad):

        self.codigo = codigo
        self.nombre = nombre
        self.bodega = bodega
        self.cantidad = cantidad

        self.anterior = None
        self.siguiente = None


class Inventario:

    def __init__(self):

        self.inicio = None
        self.ultimo = None

    # --------------------------------------------------------
    # REGISTRAR REPUESTO
    # --------------------------------------------------------

    def registrar(self):

        print("\n--- REGISTRAR REPUESTO ---")

        codigo = input("Código: ")

        if self.buscar(codigo, mostrar=False):
            print("Ya existe ese código.")
            return

        nombre = input("Nombre del repuesto: ")
        bodega = input("Bodega: ")

        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("Cantidad inválida.")
            return

        nuevo = NodoRepuesto(
            codigo,
            nombre,
            bodega,
            cantidad
        )

        if self.inicio is None:

            self.inicio = nuevo
            self.ultimo = nuevo

        else:

            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

        print("Repuesto registrado correctamente.")

    # --------------------------------------------------------
    # MOSTRAR INVENTARIO
    # --------------------------------------------------------

    def mostrar(self):

        print("\n--- INVENTARIO ---")

        if self.inicio is None:
            print("Inventario vacío.")
            return

        actual = self.inicio

        while actual is not None:

            print("\nCódigo:", actual.codigo)
            print("Repuesto:", actual.nombre)
            print("Bodega:", actual.bodega)
            print("Cantidad:", actual.cantidad)

            actual = actual.siguiente

    # --------------------------------------------------------
    # MOSTRAR HACIA ATRÁS
    # --------------------------------------------------------

    def mostrar_atras(self):

        print("\n--- INVENTARIO HACIA ATRÁS ---")

        if self.ultimo is None:
            print("Inventario vacío.")
            return

        actual = self.ultimo

        while actual is not None:

            print(
                actual.codigo,
                "-",
                actual.nombre,
                "-",
                actual.bodega,
                "- Cantidad:",
                actual.cantidad
            )

            actual = actual.anterior

    # --------------------------------------------------------
    # BUSCAR REPUESTO
    # --------------------------------------------------------

    def buscar(self, codigo, mostrar=True):

        actual = self.inicio

        while actual is not None:

            if actual.codigo == codigo:

                if mostrar:

                    print("\nRepuesto encontrado.")
                    print("Código:", actual.codigo)
                    print("Nombre:", actual.nombre)
                    print("Bodega:", actual.bodega)
                    print("Cantidad:", actual.cantidad)

                return actual

            actual = actual.siguiente

        if mostrar:
            print("Repuesto no encontrado.")

        return None

    # --------------------------------------------------------
    # EDITAR REPUESTO
    # --------------------------------------------------------

    def editar(self):

        codigo = input("Código del repuesto: ")

        repuesto = self.buscar(codigo, mostrar=False)

        if repuesto is None:
            print("Repuesto no encontrado.")
            return

        nombre = input("Nombre [" + repuesto.nombre + "]: ")
        bodega = input("Bodega [" + repuesto.bodega + "]: ")

        if nombre != "":
            repuesto.nombre = nombre

        if bodega != "":
            repuesto.bodega = bodega

        print("Repuesto actualizado.")

    # --------------------------------------------------------
    # ACTUALIZAR CANTIDAD
    # --------------------------------------------------------

    def actualizar_cantidad(self):

        codigo = input("Código del repuesto: ")

        repuesto = self.buscar(codigo, mostrar=False)

        if repuesto is None:
            print("Repuesto no encontrado.")
            return

        try:
            nueva_cantidad = int(
                input("Nueva cantidad: ")
            )
        except ValueError:
            print("Cantidad inválida.")
            return

        repuesto.cantidad = nueva_cantidad

        print("Cantidad actualizada.")

    # --------------------------------------------------------
    # ELIMINAR REPUESTO
    # --------------------------------------------------------

    def eliminar(self):

        codigo = input("Código del repuesto: ")

        actual = self.inicio

        while actual is not None:

            if actual.codigo == codigo:

                if actual.anterior is not None:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente

                if actual.siguiente is not None:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.ultimo = actual.anterior

                print("Repuesto eliminado.")
                return

            actual = actual.siguiente

        print("Repuesto no encontrado.")

    # --------------------------------------------------------
    # CONTAR REPUESTOS
    # --------------------------------------------------------

    def contar(self):

        contador = 0
        actual = self.inicio

        while actual is not None:

            contador += 1
            actual = actual.siguiente

        print("Cantidad de repuestos:", contador)


# ============================================================
# PUNTO 1 - MATRIZ DE COBERTURA
# ============================================================
# Aquí se representa la disponibilidad de las tres bodegas
# para las diferentes zonas de la ciudad.
# ============================================================

NOMBRES_ALMACENES = [
    "Bodega Norte",
    "Bodega Centro",
    "Bodega Sur"
]

NOMBRES_SECTORES = [
    "Zona 1",
    "Zona 2",
    "Zona 3",
    "Zona 4"
]

cobertura_auxilios = [

    [15, 8, 20, 5],

    [10, 12, 0, 14],

    [7, 18, 9, 22]
]


# ------------------------------------------------------------
# GENERAR REPORTE CONSOLIDADO
# ------------------------------------------------------------

def generar_reporte_consolidado():

    reporte = []

    for fila in cobertura_auxilios:

        nueva_fila = fila.copy()

        total = sum(fila)

        nueva_fila.append(total)

        reporte.append(nueva_fila)

    # Totales de cada zona

    totales_zonas = []

    for columna in range(len(NOMBRES_SECTORES)):

        total = 0

        for fila in cobertura_auxilios:

            total += fila[columna]

        totales_zonas.append(total)

    total_general = sum(totales_zonas)

    totales_zonas.append(total_general)

    reporte.append(totales_zonas)

    return reporte


# ------------------------------------------------------------
# MOSTRAR CUADRO DE DISPONIBILIDAD
# ------------------------------------------------------------

def mostrar_cuadro_disponibilidad():

    reporte = generar_reporte_consolidado()

    print("\n================================================")
    print("       CUADRO DE DISPONIBILIDAD")
    print("================================================")

    print(
        f"{'Bodega':<20}"
        f"{'Z1':<8}"
        f"{'Z2':<8}"
        f"{'Z3':<8}"
        f"{'Z4':<8}"
        f"{'TOTAL':<8}"
    )

    print("-" * 60)

    for i in range(len(NOMBRES_ALMACENES)):

        print(
            f"{NOMBRES_ALMACENES[i]:<20}"
            f"{reporte[i][0]:<8}"
            f"{reporte[i][1]:<8}"
            f"{reporte[i][2]:<8}"
            f"{reporte[i][3]:<8}"
            f"{reporte[i][4]:<8}"
        )

    print("-" * 60)

    print(
        f"{'TOTAL':<20}"
        f"{reporte[3][0]:<8}"
        f"{reporte[3][1]:<8}"
        f"{reporte[3][2]:<8}"
        f"{reporte[3][3]:<8}"
        f"{reporte[3][4]:<8}"
    )


# ------------------------------------------------------------
# BUSCAR BASE DE APOYO CERCANA
# ------------------------------------------------------------

def buscar_bases_limitrofes_y_mejor_apoyo():

    print("\n--- BUSCAR BASE DE APOYO ---")

    print("\nBodegas:")

    for i in range(len(NOMBRES_ALMACENES)):
        print(i + 1, ".", NOMBRES_ALMACENES[i])

    try:
        almacen_idx = int(
            input("Seleccione la bodega: ")
        ) - 1
    except ValueError:
        print("Opción inválida.")
        return

    if almacen_idx < 0 or almacen_idx >= len(NOMBRES_ALMACENES):
        print("Bodega inválida.")
        return

    print("\nZonas:")

    for i in range(len(NOMBRES_SECTORES)):
        print(i + 1, ".", NOMBRES_SECTORES[i])

    try:
        sector_idx = int(
            input("Seleccione la zona: ")
        ) - 1
    except ValueError:
        print("Opción inválida.")
        return

    if sector_idx < 0 or sector_idx >= len(NOMBRES_SECTORES):
        print("Zona inválida.")
        return

    print(
        "\nUbicación seleccionada:",
        NOMBRES_ALMACENES[almacen_idx],
        "-",
        NOMBRES_SECTORES[sector_idx]
    )

    vecinos = []

    # Arriba

    if almacen_idx > 0:

        vecinos.append(
            (
                cobertura_auxilios[almacen_idx - 1][sector_idx],
                almacen_idx - 1,
                sector_idx
            )
        )

    # Abajo

    if almacen_idx < len(cobertura_auxilios) - 1:

        vecinos.append(
            (
                cobertura_auxilios[almacen_idx + 1][sector_idx],
                almacen_idx + 1,
                sector_idx
            )
        )

    # Izquierda

    if sector_idx > 0:

        vecinos.append(
            (
                cobertura_auxilios[almacen_idx][sector_idx - 1],
                almacen_idx,
                sector_idx - 1
            )
        )

    # Derecha

    if sector_idx < len(NOMBRES_SECTORES) - 1:

        vecinos.append(
            (
                cobertura_auxilios[almacen_idx][sector_idx + 1],
                almacen_idx,
                sector_idx + 1
            )
        )

    if len(vecinos) == 0:

        print("No hay bases cercanas.")
        return

    mejor = max(vecinos)

    disponibilidad = mejor[0]
    bodega = mejor[1]
    zona = mejor[2]

    print("\nMEJOR APOYO ENCONTRADO")
    print("Bodega:", NOMBRES_ALMACENES[bodega])
    print("Zona:", NOMBRES_SECTORES[zona])
    print("Disponibilidad:", disponibilidad)


# ------------------------------------------------------------
# MENÚ DEL PUNTO 1
# ------------------------------------------------------------

def menu_cobertura():

    while True:

        print("\n================================")
        print("       CONSULTAR COBERTURA")
        print("================================")

        print("1. Ver cuadro de disponibilidad")
        print("2. Consultar base de apoyo cercana")
        print("3. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            mostrar_cuadro_disponibilidad()

        elif opcion == "2":

            buscar_bases_limitrofes_y_mejor_apoyo()

        elif opcion == "3":

            break

        else:

            print("Opción inválida.")


# ============================================================
# PUNTO 2 - ORGANIZACIÓN DE SOLICITUDES
# ============================================================
# En este punto se utilizan listas enlazadas para:
#
# 1. Fusionar dos listas ordenadas por prioridad.
# 2. Particionar una lista usando un pivote.
#
# La prioridad 1 representa la mayor urgencia.
# ============================================================


class NodoOrganizacion:

    def __init__(
        self,
        id_solicitud,
        zona,
        repuesto,
        prioridad
    ):

        self.id_solicitud = id_solicitud
        self.zona = zona
        self.repuesto = repuesto
        self.prioridad = prioridad
        self.next = None


class ListaOrganizacion:

    def __init__(self):

        self.head = None

    # --------------------------------------------------------
    # INSERTAR
    # --------------------------------------------------------

    def insertar(
        self,
        id_solicitud,
        zona,
        repuesto,
        prioridad
    ):

        nuevo = NodoOrganizacion(
            id_solicitud,
            zona,
            repuesto,
            prioridad
        )

        if self.head is None:

            self.head = nuevo

        else:

            actual = self.head

            while actual.next is not None:
                actual = actual.next

            actual.next = nuevo

    # --------------------------------------------------------
    # MOSTRAR
    # --------------------------------------------------------

    def mostrar(self, titulo="SOLICITUDES"):

        print("\n---", titulo, "---")

        if self.head is None:

            print("Lista vacía.")
            return

        actual = self.head

        while actual is not None:

            print(
                "ID:", actual.id_solicitud,
                "| Zona:", actual.zona,
                "| Repuesto:", actual.repuesto,
                "| Prioridad:", actual.prioridad
            )

            actual = actual.next


# ------------------------------------------------------------
# FUSIONAR DOS LISTAS
# ------------------------------------------------------------

def fusionar(lista_a, lista_b):

    resultado = ListaOrganizacion()

    a = lista_a.head
    b = lista_b.head

    while a is not None and b is not None:

        if a.prioridad <= b.prioridad:

            resultado.insertar(
                a.id_solicitud,
                a.zona,
                a.repuesto,
                a.prioridad
            )

            a = a.next

        else:

            resultado.insertar(
                b.id_solicitud,
                b.zona,
                b.repuesto,
                b.prioridad
            )

            b = b.next

    while a is not None:

        resultado.insertar(
            a.id_solicitud,
            a.zona,
            a.repuesto,
            a.prioridad
        )

        a = a.next

    while b is not None:

        resultado.insertar(
            b.id_solicitud,
            b.zona,
            b.repuesto,
            b.prioridad
        )

        b = b.next

    return resultado


# ------------------------------------------------------------
# PARTICIONAR LISTA
# ------------------------------------------------------------

def particionar(lista, pivote):

    menores = ListaOrganizacion()
    mayores = ListaOrganizacion()

    actual = lista.head

    while actual is not None:

        if actual.prioridad < pivote:

            menores.insertar(
                actual.id_solicitud,
                actual.zona,
                actual.repuesto,
                actual.prioridad
            )

        else:

            mayores.insertar(
                actual.id_solicitud,
                actual.zona,
                actual.repuesto,
                actual.prioridad
            )

        actual = actual.next

    return menores, mayores


# ------------------------------------------------------------
# MENÚ DEL PUNTO 2
# ------------------------------------------------------------

def menu_organizacion():

    while True:

        print("\n================================")
        print("       ORGANIZAR SOLICITUDES")
        print("================================")

        print("1. Fusionar solicitudes")
        print("2. Particionar solicitudes")
        print("3. Ver ejemplo completo")
        print("4. Volver")

        opcion = input("Seleccione: ")

        # ----------------------------------------------------
        # FUSIÓN
        # ----------------------------------------------------

        if opcion == "1":

            lista_manana = ListaOrganizacion()

            lista_manana.insertar(
                1, "Norte", "Filtro", 1
            )

            lista_manana.insertar(
                3, "Centro", "Bujía", 3
            )

            lista_manana.insertar(
                5, "Sur", "Aceite", 5
            )

            lista_tarde = ListaOrganizacion()

            lista_tarde.insertar(
                2, "Occidente", "Llanta", 2
            )

            lista_tarde.insertar(
                4, "Norte", "Batería", 4
            )

            lista_tarde.insertar(
                6, "Sur", "Freno", 6
            )

            lista_manana.mostrar("SOLICITUDES DE LA MAÑANA")

            lista_tarde.mostrar("SOLICITUDES DE LA TARDE")

            resultado = fusionar(
                lista_manana,
                lista_tarde
            )

            resultado.mostrar(
                "LISTA FUSIONADA POR PRIORIDAD"
            )

        # ----------------------------------------------------
        # PARTICIÓN
        # ----------------------------------------------------

        elif opcion == "2":

            lista = ListaOrganizacion()

            lista.insertar(
                10, "Norte", "Filtro", 5
            )

            lista.insertar(
                11, "Sur", "Aceite", 2
            )

            lista.insertar(
                12, "Centro", "Bujía", 4
            )

            lista.insertar(
                13, "Norte", "Freno", 1
            )

            lista.insertar(
                14, "Sur", "Llanta", 3
            )

            pivote = 3

            lista.mostrar(
                "LISTA ORIGINAL"
            )

            menores, mayores = particionar(
                lista,
                pivote
            )

            menores.mostrar(
                "PRIORIDAD MENOR QUE 3"
            )

            mayores.mostrar(
                "PRIORIDAD MAYOR O IGUAL A 3"
            )

        # ----------------------------------------------------
        # EJEMPLO COMPLETO
        # ----------------------------------------------------

        elif opcion == "3":

            print("\n--- EJEMPLO DEL PUNTO 2 ---")

            print("\nFUSIÓN:")

            print(
                "Lista A: prioridades 1, 3, 5"
            )

            print(
                "Lista B: prioridades 2, 4, 6"
            )

            print(
                "Resultado: 1, 2, 3, 4, 5, 6"
            )

            print("\nPARTICIÓN:")

            print(
                "Lista: 5, 2, 4, 1, 3"
            )

            print(
                "Pivote: 3"
            )

            print(
                "Menores: 2, 1"
            )

            print(
                "Mayores o iguales: 5, 4, 3"
            )

        elif opcion == "4":

            break

        else:

            print("Opción inválida.")


# ============================================================
# PUNTO 3 - HISTORIAL DE SOLICITUDES (LRU)
# ============================================================
# LRU = Least Recently Used
#
# Este módulo funciona como un buffer de las últimas N
# solicitudes CONSULTADAS por el usuario.
#
# HEAD (raiz) = solicitud más recientemente utilizada.
# TAIL (ultimo) = solicitud menos recientemente utilizada.
#
# Al consultar una solicitud que ya está en el buffer:
# se mueve al inicio modificando únicamente prev/next.
#
# Si el buffer supera su capacidad N:
# se elimina el nodo ubicado en tail.
#
# La lista doble permite recorrer desde ambos extremos.
# ============================================================


class NodoLRU:

    def __init__(
        self,
        id_solicitud,
        cliente,
        telefono,
        ubicacion,
        falla,
        urgencia,
        estado="Pendiente"
    ):

        self.id_solicitud = id_solicitud
        self.cliente = cliente
        self.telefono = telefono
        self.ubicacion = ubicacion
        self.falla = falla
        self.urgencia = urgencia
        self.estado = estado

        # Lista doblemente enlazada
        self.anterior = None
        self.siguiente = None


class ListaSolicitudesLRU:

    def __init__(self, capacidad=4):

        self.raiz = None       # HEAD: más reciente
        self.ultimo = None     # TAIL: menos reciente
        self.capacidad = capacidad
        self.tamano = 0

    # --------------------------------------------------------
    # AGREGAR SOLICITUD CONSULTADA AL BUFFER
    # --------------------------------------------------------

    def agregar_solicitud(self, solicitud):

        if solicitud is None:
            return

        # Si ya está en el buffer, se actualizan sus datos y se
        # mueve al inicio. No se crea un nodo nuevo.
        existente = self.buscar(
            solicitud.id_solicitud,
            mostrar=False,
            mover=False
        )

        if existente is not None:

            existente.cliente = solicitud.cliente
            existente.ubicacion = solicitud.zona
            existente.falla = solicitud.falla
            existente.urgencia = solicitud.urgencia
            existente.estado = solicitud.estado

            self.mover_al_inicio(existente)
            return


        nuevo = NodoLRU(
            solicitud.id_solicitud,
            solicitud.cliente,
            "",
            solicitud.zona,
            solicitud.falla,
            solicitud.urgencia,
            solicitud.estado
        )

        self.agregar_nodo_inicio(nuevo)
        self.tamano += 1

        # Si supera N, sale el menos recientemente usado.
        self.controlar_capacidad()

    # --------------------------------------------------------
    # INSERTAR UN NODO AL HEAD
    # --------------------------------------------------------

    def agregar_nodo_inicio(self, nodo):

        nodo.anterior = None
        nodo.siguiente = self.raiz

        if self.raiz is not None:
            self.raiz.anterior = nodo

        else:
            # Primer nodo: también es tail.
            self.ultimo = nodo

        self.raiz = nodo

    # --------------------------------------------------------
    # CONTROLAR CAPACIDAD DEL BUFFER
    # --------------------------------------------------------

    def controlar_capacidad(self):

        while self.tamano > self.capacidad:

            eliminado = self.ultimo

            if eliminado is None:
                return

            self.ultimo = eliminado.anterior

            if self.ultimo is not None:
                self.ultimo.siguiente = None

            else:
                self.raiz = None

            eliminado.anterior = None
            eliminado.siguiente = None
            self.tamano -= 1

            print(
                "Buffer lleno. Se eliminó la solicitud menos reciente:",
                eliminado.id_solicitud
            )

    # --------------------------------------------------------
    # MOSTRAR RECIENTES A ANTIGUAS
    # --------------------------------------------------------

    def mostrar(self):

        print("\n--- BUFFER LRU: MÁS RECIENTES ---")

        if self.raiz is None:
            print("Buffer vacío.")
            return

        actual = self.raiz
        posicion = 0

        while actual is not None:

            print(
                "\nPosición:", posicion,
                "| ID:", actual.id_solicitud
            )
            print("Cliente:", actual.cliente)
            print("Ubicación:", actual.ubicacion)
            print("Falla:", actual.falla)
            print("Urgencia:", actual.urgencia)
            print("Estado:", actual.estado)

            actual = actual.siguiente
            posicion += 1

        print("\nCapacidad máxima:", self.capacidad)
        print("Solicitudes almacenadas:", self.tamano)

    # --------------------------------------------------------
    # MOSTRAR ANTIGUAS A RECIENTES
    # --------------------------------------------------------

    def mostrar_reversa(self):

        print("\n--- BUFFER LRU: MÁS ANTIGUAS ---")

        if self.ultimo is None:
            print("Buffer vacío.")
            return

        actual = self.ultimo

        while actual is not None:

            print(
                "ID:", actual.id_solicitud,
                "| Cliente:", actual.cliente,
                "| Estado:", actual.estado
            )

            actual = actual.anterior

    # --------------------------------------------------------
    # BUSCAR POR ID
    # --------------------------------------------------------

    def buscar(
        self,
        id_solicitud,
        mostrar=True,
        mover=True
    ):

        actual = self.raiz

        while actual is not None:

            if actual.id_solicitud == id_solicitud:

                if mostrar:
                    self.mostrar_nodo(actual)

                if mover:
                    self.mover_al_inicio(actual)

                return actual

            actual = actual.siguiente

        if mostrar:
            print("Solicitud no encontrada en el buffer.")

        return None

    # --------------------------------------------------------
    # BUSCAR ELEMENTO I-ÉSIMO DE FORMA BIDIRECCIONAL
    # --------------------------------------------------------

    def buscar_iesimo(self, posicion, mostrar=True, mover=True):

        if posicion < 0 or posicion >= self.tamano:

            if mostrar:
                print("Posición inválida.")

            return None

        # Si está en la primera mitad, conviene comenzar en HEAD.
        if posicion <= (self.tamano - 1) // 2:

            actual = self.raiz
            pasos = posicion
            direccion = "HEAD -> TAIL"

            for _ in range(pasos):
                actual = actual.siguiente

        # Si está en la segunda mitad, conviene comenzar en TAIL.
        else:

            actual = self.ultimo
            pasos = self.tamano - 1 - posicion
            direccion = "TAIL -> HEAD"

            for _ in range(pasos):
                actual = actual.anterior

        if mostrar:

            print(
                "\nElemento encontrado en posición",
                posicion
            )
            print("Recorrido utilizado:", direccion)
            self.mostrar_nodo(actual)

        if mover:
            self.mover_al_inicio(actual)

        return actual

    # --------------------------------------------------------
    # MOSTRAR DATOS DE UN NODO
    # --------------------------------------------------------

    def mostrar_nodo(self, nodo):

        print("\nSolicitud encontrada.")
        print("ID:", nodo.id_solicitud)
        print("Cliente:", nodo.cliente)
        print("Ubicación:", nodo.ubicacion)
        print("Falla:", nodo.falla)
        print("Urgencia:", nodo.urgencia)
        print("Estado:", nodo.estado)

    # --------------------------------------------------------
    # MOVER AL HEAD - O(1) CON REFERENCIA AL NODO
    # --------------------------------------------------------

    def mover_al_inicio(self, nodo):

        if nodo is None or nodo == self.raiz:
            return

        # Desconectar el nodo de su posición actual.
        if nodo.anterior is not None:
            nodo.anterior.siguiente = nodo.siguiente

        if nodo.siguiente is not None:
            nodo.siguiente.anterior = nodo.anterior

        else:
            # Era el tail.
            self.ultimo = nodo.anterior

        # Reconectarlo como nuevo head.
        nodo.anterior = None
        nodo.siguiente = self.raiz

        if self.raiz is not None:
            self.raiz.anterior = nodo

        self.raiz = nodo

    # --------------------------------------------------------
    # EDITAR
    # --------------------------------------------------------

    def editar(self):

        print("\n--- EDITAR REGISTRO DEL BUFFER ---")

        id_solicitud = input("ID: ")

        nodo = self.buscar(
            id_solicitud,
            mostrar=False,
            mover=False
        )

        if nodo is None:
            print("Solicitud no encontrada en el buffer.")
            return

        print("Presione ENTER para conservar el valor actual.")

        cliente = input("Cliente [" + nodo.cliente + "]: ")
        ubicacion = input("Ubicación [" + nodo.ubicacion + "]: ")
        falla = input("Falla [" + nodo.falla + "]: ")

        if cliente != "":
            nodo.cliente = cliente

        if ubicacion != "":
            nodo.ubicacion = ubicacion

        if falla != "":
            nodo.falla = falla

        print("Solicitud actualizada.")

    # --------------------------------------------------------
    # CAMBIAR ESTADO
    # --------------------------------------------------------

    def cambiar_estado(self):

        print("\n--- CAMBIAR ESTADO ---")

        id_solicitud = input("ID: ")

        nodo = self.buscar(
            id_solicitud,
            mostrar=False,
            mover=False
        )

        if nodo is None:
            print("Solicitud no encontrada en el buffer.")
            return

        print("\nEstado actual:", nodo.estado)
        print("1. Pendiente")
        print("2. En camino")
        print("3. Atendido")
        print("4. Cancelado")

        opcion = input("Seleccione: ")

        estados = {
            "1": "Pendiente",
            "2": "En camino",
            "3": "Atendido",
            "4": "Cancelado"
        }

        if opcion not in estados:
            print("Opción inválida.")
            return

        nodo.estado = estados[opcion]
        print("Estado actualizado a:", nodo.estado)

    # --------------------------------------------------------
    # ELIMINAR
    # --------------------------------------------------------

    def eliminar(self):

        print("\n--- ELIMINAR DEL BUFFER ---")

        id_solicitud = input("ID: ")

        nodo = self.buscar(
            id_solicitud,
            mostrar=False,
            mover=False
        )

        if nodo is None:
            print("Solicitud no encontrada en el buffer.")
            return

        if nodo.anterior is not None:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.raiz = nodo.siguiente

        if nodo.siguiente is not None:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.ultimo = nodo.anterior

        nodo.anterior = None
        nodo.siguiente = None
        self.tamano -= 1

        print("Solicitud eliminada del buffer.")

    # --------------------------------------------------------
    # CONTAR
    # --------------------------------------------------------

    def contar(self):

        print(
            "Solicitudes almacenadas en el buffer:",
            self.tamano,
            "/",
            self.capacidad
        )


# ------------------------------------------------------------
# MENÚ DEL PUNTO 3
# ------------------------------------------------------------

def menu_historial(historial):

    while True:

        print("\n================================")
        print("       BUFFER / HISTORIAL LRU")
        print("================================")

        print("Capacidad máxima:", historial.capacidad)
        print("Solicitudes almacenadas:", historial.tamano)
        print("\n1. Ver solicitudes recientes")
        print("2. Ver solicitudes antiguas")
        print("3. Buscar solicitud por ID")
        print("4. Buscar elemento i-ésimo")
        print("5. Editar solicitud")
        print("6. Eliminar solicitud")
        print("7. Cambiar estado")
        print("8. Contar solicitudes")
        print("9. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":
            historial.mostrar()

        elif opcion == "2":
            historial.mostrar_reversa()

        elif opcion == "3":

            id_solicitud = input("ID de solicitud: ")
            historial.buscar(id_solicitud)

        elif opcion == "4":

            try:
                posicion = int(
                    input(
                        "Posición i-ésima (comenzando desde 0): "
                    )
                )
            except ValueError:
                print("Posición inválida.")
                continue

            historial.buscar_iesimo(posicion)

        elif opcion == "5":
            historial.editar()

        elif opcion == "6":
            historial.eliminar()

        elif opcion == "7":
            historial.cambiar_estado()

        elif opcion == "8":
            historial.contar()

        elif opcion == "9":
            break

        else:
            print("Opción inválida.")


# ============================================================
# MENÚ DE SOLICITUDES
# ============================================================

def menu_solicitudes(solicitudes, historial):

    while True:

        print("\n================================")
        print("       GESTIONAR SOLICITUDES")
        print("================================")

        print("1. Registrar solicitud")
        print("2. Ver solicitudes")
        print("3. Buscar solicitud")
        print("4. Editar solicitud")
        print("5. Cambiar estado")
        print("6. Eliminar solicitud")
        print("7. Contar solicitudes")
        print("8. Historial de solicitudes recientes")
        print("9. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            solicitudes.registrar()

        elif opcion == "2":

            solicitudes.mostrar()

        elif opcion == "3":

            id_solicitud = input(
                "ID de solicitud: "
            )

            solicitud = solicitudes.buscar(id_solicitud)

            if solicitud is not None:
                historial.agregar_solicitud(solicitud)

        elif opcion == "4":

            solicitudes.editar()

        elif opcion == "5":

            solicitudes.cambiar_estado()

        elif opcion == "6":

            solicitudes.eliminar()

        elif opcion == "7":

            solicitudes.contar()

        elif opcion == "8":

            menu_historial(historial)

        elif opcion == "9":

            break

        else:

            print("Opción inválida.")


# ============================================================
# MENÚ DE RUTAS
# ============================================================

def menu_rutas(rutas):

    while True:

        print("\n================================")
        print("          GESTIONAR RUTAS")
        print("================================")

        print("1. Agregar parada")
        print("2. Ver ruta completa")
        print("3. Recorrer ruta")
        print("4. Buscar parada")
        print("5. Eliminar parada")
        print("6. Contar paradas")
        print("7. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            rutas.agregar_parada()

        elif opcion == "2":

            rutas.mostrar()

        elif opcion == "3":

            rutas.recorrer()

        elif opcion == "4":

            rutas.buscar()

        elif opcion == "5":

            rutas.eliminar()

        elif opcion == "6":

            rutas.contar()

        elif opcion == "7":

            break

        else:

            print("Opción inválida.")


# ============================================================
# MENÚ DE INVENTARIO
# ============================================================

def menu_inventario(inventario):

    while True:

        print("\n================================")
        print("       GESTIONAR INVENTARIO")
        print("================================")

        print("1. Registrar repuesto")
        print("2. Ver inventario")
        print("3. Ver inventario hacia atrás")
        print("4. Buscar repuesto")
        print("5. Editar repuesto")
        print("6. Actualizar cantidad")
        print("7. Eliminar repuesto")
        print("8. Contar repuestos")
        print("9. Volver")

        opcion = input("Seleccione: ")

        if opcion == "1":

            inventario.registrar()

        elif opcion == "2":

            inventario.mostrar()

        elif opcion == "3":

            inventario.mostrar_atras()

        elif opcion == "4":

            codigo = input(
                "Código del repuesto: "
            )

            inventario.buscar(codigo)

        elif opcion == "5":

            inventario.editar()

        elif opcion == "6":

            inventario.actualizar_cantidad()

        elif opcion == "7":

            inventario.eliminar()

        elif opcion == "8":

            inventario.contar()

        elif opcion == "9":

            break

        else:

            print("Opción inválida.")


# ============================================================
# MENÚ PRINCIPAL
# ============================================================

def menu_principal():

    # Crear las estructuras principales

    solicitudes = Solicitudes()
    rutas = Rutas()
    inventario = Inventario()

    # Buffer LRU persistente durante toda la ejecución.
    # Se conservan las últimas 3 solicitudes consultadas.
    historial = ListaSolicitudesLRU(3)

    while True:

        print("\n")
        print("================================================")
        print("       FLASH LOGISTICS")
        print("       SISTEMA DE ASISTENCIA VEHICULAR")
        print("================================================")

        print("1. Gestionar solicitudes")
        print("2. Gestionar rutas")
        print("3. Gestionar inventario")
        print("4. Consultar cobertura")
        print("5. Organizar solicitudes")
        print("6. Historial de solicitudes")
        print("7. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            menu_solicitudes(solicitudes, historial)

        elif opcion == "2":

            menu_rutas(rutas)

        elif opcion == "3":

            menu_inventario(inventario)

        elif opcion == "4":

            menu_cobertura()

        elif opcion == "5":

            menu_organizacion()

        elif opcion == "6":

            menu_historial(historial)

        elif opcion == "7":

            print(
                "\nGracias por utilizar FLASH LOGISTICS."
            )

            break

        else:

            print("Opción inválida.")


# ============================================================
# EJECUTAR PROGRAMA
# ============================================================

menu_principal()
