def mostrar_barra(valor, etiqueta, maximo=100):
    largo = int((valor / maximo) * 20)
    barra = "█" * largo
    print(f"{etiqueta:25}: {barra} {valor}%")


def recomendar_ropa(temp, lluvia, humedad, tipo_dia):
    tipo_dia = tipo_dia.lower()

    if tipo_dia == "soleado":
        if temp >= 30:
            return "Ropa muy ligera (camiseta y pantalón corto)"
        elif temp >= 22:
            return "Ropa ligera o casual fresca"
        else:
            return "Chaqueta ligera o ropa cómoda"

    elif tipo_dia == "lluvioso":
        if lluvia >= 70:
            return "Impermeable y botas de lluvia"
        elif lluvia >= 40:
            return "Chaqueta impermeable ligera"
        else:
            return "Ropa normal, lleva paraguas por si acaso"

    elif tipo_dia == "nublado":
        if temp < 15:
            return "Ropa abrigada (saco o bufanda)"
        elif temp < 22:
            return "Sudadera o chaqueta ligera"
        else:
            return "Ropa casual templada"

    elif tipo_dia == "parcialmente_nublado":
        if temp > 25:
            return "Ropa fresca, pero lleva una chaqueta por si acaso"
        else:
            return "Ropa cómoda y ligera"

    else:
        return "Tipo de día no reconocido. Usa Soleado, Lluvioso, Nublado o Parcialmente_nublado."


print("===============================================")
print("       👕 ASISTENTE DE VESTIMENTA INTELIGENTE")
print("===============================================")

try:
    temperatura = int(input("🌡️  Ingresa la temperatura (°C): "))
    lluvia = int(input("🌧️  Ingresa la probabilidad de lluvia (%): "))
    humedad = int(input("💧 Ingresa la humedad (%): "))
    tipo_dia = input("☀️  Ingresa el tipo de día (Soleado, Lluvioso, Nublado, Parcialmente_nublado): ")

    # Mostrar “gráficas” del clima
    print("\n📊 CONDICIONES CLIMÁTICAS:")
    mostrar_barra(temperatura * 3, "Temperatura", 100)  # Se multiplica para darle escala visual
    mostrar_barra(lluvia, "Probabilidad de Lluvia", 100)
    mostrar_barra(humedad, "Humedad Ambiental", 100)

    # Mostrar recomendación
    recomendacion = recomendar_ropa(temperatura, lluvia, humedad, tipo_dia)
    print("\n👕 RECOMENDACIÓN AUTOMÁTICA:")
    print(f"👉 {recomendacion}")

except:
    print("\n⚠️ Error: asegúrate de ingresar números válidos y escribir correctamente el tipo de día.")
