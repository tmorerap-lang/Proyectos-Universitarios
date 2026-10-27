# 👕 Asistente Inteligente de Vestimenta

## 📌 Descripción

El **Asistente Inteligente de Vestimenta** es un proyecto académico desarrollado en Python que recomienda qué ropa utilizar según las condiciones climáticas ingresadas por el usuario.

El programa analiza la temperatura, la probabilidad de lluvia y el tipo de día para ofrecer recomendaciones de vestimenta. También solicita la humedad ambiental y muestra los valores climáticos mediante barras visuales en la consola.

## 🎯 Objetivos

- Aplicar la programación para resolver una situación cotidiana.
- Utilizar estructuras condicionales para generar recomendaciones automáticas.
- Representar visualmente algunos datos climáticos en la consola.
- Practicar el uso de funciones, variables y entrada de datos en Python.

## ⚙️ ¿Cómo funciona?

El programa solicita al usuario cuatro datos:

- **Temperatura:** valor ingresado en grados Celsius.
- **Probabilidad de lluvia:** porcentaje de posibilidad de lluvia.
- **Humedad ambiental:** porcentaje de humedad.
- **Tipo de día:** soleado, lluvioso, nublado o parcialmente nublado.

A partir de estos datos, el sistema aplica reglas condicionales para seleccionar una recomendación de vestimenta.

### 🌤️ Recomendaciones según el clima

| Condición | Recomendación |
|---|---|
| Soleado y temperatura de 30 °C o más | Ropa muy ligera |
| Soleado y temperatura de 22 °C o más | Ropa ligera o casual fresca |
| Lluvioso y probabilidad de lluvia de 70 % o más | Impermeable y botas de lluvia |
| Lluvioso y probabilidad de lluvia de 40 % o más | Chaqueta impermeable ligera |
| Nublado y temperatura inferior a 15 °C | Ropa abrigada |
| Nublado y temperatura inferior a 22 °C | Sudadera o chaqueta ligera |
| Parcialmente nublado y temperatura superior a 25 °C | Ropa fresca y una chaqueta por si acaso |

Las recomendaciones dependen de las condiciones establecidas en el código. Para los demás rangos, el programa utiliza las reglas adicionales definidas en la función `recomendar_ropa()`.

## 📊 Representación visual de los datos

El programa incluye la función `mostrar_barra()`, que representa los valores climáticos mediante caracteres en la terminal.

Se muestran barras para:

- Temperatura.
- Probabilidad de lluvia.
- Humedad ambiental.

En el caso de la temperatura, el valor se multiplica por tres para darle una escala visual.

## 🛠️ Tecnologías y conceptos utilizados

- **Python 3:** lenguaje utilizado para desarrollar el programa.
- **Funciones:** organización de la lógica en bloques reutilizables.
- **Condicionales `if`, `elif` y `else`:** evaluación de las condiciones climáticas.
- **Entrada de datos con `input()`:** captura de información del usuario.
- **Conversión de tipos con `int()`:** procesamiento de los valores numéricos.
- **Manejo de excepciones con `try` y `except`:** respuesta ante entradas que producen errores.
- **Cadenas de texto y ciclos de repetición de caracteres:** generación de las barras visuales.

## ▶️ Cómo ejecutar el proyecto

1. Instala Python 3 si todavía no lo tienes.
2. Descarga o clona este repositorio.
3. Abre la carpeta `vestimenta-inteligente`.
4. Ejecuta el archivo principal desde una terminal:

```bash
python3 vestimenta_inteligente.py
```

5. Ingresa los datos solicitados y consulta la recomendación.

*Si el archivo tiene otro nombre, reemplaza `vestimenta_inteligente.py` por el nombre correspondiente.*

## 🧪 Ejemplo de uso

**Datos ingresados:**

- Temperatura: 32 °C.
- Probabilidad de lluvia: 10 %.
- Humedad: 45 %.
- Tipo de día: Soleado.

**Resultado esperado:**

El programa muestra las barras visuales de las condiciones climáticas y recomienda:

> Ropa muy ligera (camiseta y pantalón corto).

## 📚 Aprendizajes

Este proyecto permite practicar los fundamentos de Python, la creación de funciones, la toma de decisiones mediante estructuras condicionales y la representación sencilla de información en consola.

También demuestra cómo un conjunto de reglas programadas puede utilizarse para desarrollar un asistente que ofrece recomendaciones personalizadas a partir de datos proporcionados por el usuario.

## ⚠️ Alcance del proyecto

Este asistente utiliza reglas definidas previamente en el código. No consulta servicios meteorológicos externos ni utiliza un modelo de inteligencia artificial entrenado. Aunque solicita la humedad ambiental, este valor se utiliza actualmente para la representación visual y no interviene en las reglas de recomendación.

## 👨‍💻 Autor

**Tomás Morera**  
Estudiante de Ciencias de la Computación  
Universidad Sergio Arboleda.

🔗 [Mi perfil de GitHub](https://github.com/)

---

*Proyecto académico desarrollado en Python como parte de mi aprendizaje en programación y resolución de problemas.*
