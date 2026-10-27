# 🚚 FLASH LOGISTICS
### Sistema de asistencia vehicular desarrollado en Python

## 📌 Descripción

**FLASH LOGISTICS** es un proyecto académico desarrollado en Python que simula un sistema de asistencia vehicular. Su objetivo es organizar y administrar solicitudes de asistencia, rutas, inventario de repuestos y camiones, utilizando diferentes estructuras de datos para gestionar la información de manera organizada.

El sistema integra los conceptos trabajados en los dos cortes de la asignatura de Estructuras de Datos Lineales, mediante una interfaz de consola con menús que permiten acceder a las distintas funcionalidades.

## 🎯 Objetivos

- Gestionar solicitudes de asistencia vehicular.
- Organizar rutas y paradas para la atención de los clientes.
- Administrar el inventario de repuestos disponibles en las bodegas.
- Representar la cobertura de asistencia mediante una matriz.
- Organizar solicitudes según su prioridad.
- Gestionar solicitudes pendientes mediante una cola FIFO.
- Administrar el orden de llegada de los camiones mediante una pila LIFO.
- Integrar las estructuras de datos en un único sistema.

## ⚙️ Funcionalidades principales

### 📋 Gestión de solicitudes
Permite registrar, consultar, buscar, editar y eliminar solicitudes de asistencia vehicular, así como actualizar su estado.

Los estados contemplados incluyen:
- Pendiente.
- En camino.
- Atendida.
- Cancelada.

### 🛣️ Gestión de rutas
Permite registrar y consultar paradas, recorrer las rutas y buscar o eliminar paradas registradas.

### 📦 Inventario de repuestos
Permite consultar y administrar los repuestos, incluyendo información como código, nombre, bodega y cantidad disponible.

### 🏢 Matriz de cobertura
Representa la cobertura de asistencia de las bodegas Norte, Centro y Sur en diferentes zonas de la ciudad. También permite consultar la cobertura y explorar ubicaciones cercanas para apoyar la asignación de recursos.

### 🚨 Organización de solicitudes
Incorpora mecanismos para organizar solicitudes por prioridad y dividirlas utilizando un elemento de referencia. Esto permite practicar algoritmos de organización y manipulación de listas.

### 📥 Cola de solicitudes
Utiliza el principio **FIFO (First In, First Out)**: la primera solicitud que entra es la primera que se atiende.

Esta estructura permite representar el orden de atención de las solicitudes pendientes.

### 🚛 Pila de camiones
Utiliza el principio **LIFO (Last In, First Out)**: el último camión que entra es el primero que sale.

Este módulo permite representar y administrar el orden de llegada de los camiones mediante una estructura de tipo pila.

### 📚 Historial de consultas
Incluye una estructura basada en el principio **LRU (Least Recently Used)** para administrar un historial limitado de consultas recientes. Las consultas más recientes se mantienen al inicio y las menos recientes pueden eliminarse cuando se supera la capacidad establecida.

## 🧠 Estructuras de datos utilizadas

| Estructura | Aplicación en el proyecto |
|---|---|
| Lista enlazada simple | Gestión de solicitudes |
| Lista doblemente enlazada | Inventario e historial |
| Lista circular | Gestión de rutas y paradas |
| Matriz | Cobertura de bodegas y zonas |
| Cola FIFO | Orden de atención de solicitudes |
| Pila LIFO | Orden de llegada de camiones |
| Algoritmos de organización | Fusión y partición de solicitudes |
| LRU | Administración de consultas recientes |

## 🛠️ Tecnologías y herramientas

- **Python 3**
- Visual Studio Code
- Google Colab

## ▶️ Cómo ejecutar el proyecto

1. Descarga o clona el repositorio.
2. Abre la carpeta `flash-logistics`.
3. Verifica que Python 3 esté instalado.
4. Ejecuta el archivo principal del proyecto desde la terminal.

```bash
python3 flash_logistics.py
```

> Si el archivo principal tiene otro nombre, reemplaza `flash_logistics.py` por el nombre correcto. Si trabajas desde Google Colab, abre el notebook correspondiente y ejecuta sus celdas en orden.

## 🧪 Pruebas recomendadas

Para comprobar el funcionamiento del sistema, se recomienda:

- Registrar y consultar varias solicitudes.
- Modificar el estado de una solicitud.
- Agregar y recorrer paradas de una ruta.
- Registrar y consultar repuestos.
- Consultar la cobertura de las bodegas por zona.
- Organizar solicitudes con diferentes prioridades.
- Agregar y retirar elementos de la cola y la pila.
- Realizar consultas para observar cómo se actualiza el historial LRU.

## 📚 Aprendizajes

El desarrollo de FLASH LOGISTICS permite aplicar conceptos de programación orientada a objetos, estructuras de datos lineales y algoritmos de organización. También permite comprender cómo diferentes estructuras pueden colaborar dentro de un mismo sistema para resolver problemas de gestión y atención de solicitudes.

## 👥 Equipo de desarrollo

Proyecto académico desarrollado en equipo como parte de la formación en Ciencias de la Computación en la Universidad Sergio Arboleda.

- **Tomás Felipe Morera Pérez** — 
- **Sara Valentina Díaz Rojas** -
- **Cristhian Santiago Pinilla Vega** -
- **Joel Santiago Sarmiento Baldayo** -

## 🎓 Institución

Universidad Sergio Arboleda  
Programa: Ciencias de la Computación.
---

*Proyecto académico desarrollado en Python como parte del aprendizaje de Estructuras de Datos Lineales.*
