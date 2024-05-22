def millas_a_kilometros(millas):
    return millas * 1.60934

def kilometros_a_millas(kilometros):
    return kilometros / 1.60934

def m3_a_pie3(m3):
    return m3 * 35.3147

def pie3_a_m3(pie3):
    return pie3 / 35.3147

def pies_a_metros(pies):
    return pies * 0.3048

def metros_a_pies(metros):
    return metros / 0.3048

def yardas_a_metros(yardas):
    return yardas * 0.9144

def metros_a_yardas(metros):
    return metros / 0.9144

def mostrar_menu_principal():
    print("Seleccione el tipo de conversión:")
    print("1. Longitud (Millas <-> Kilómetros)")
    print("2. Volumen (m3 <-> pie3)")
    print("3. Longitud (pies, metros, yardas)")
    print("4. Salir")

def mostrar_menu_conversion(opcion):
    if opcion == 1:
        print("Seleccione la conversión de Longitud:")
        print("1. Millas a Kilómetros")
        print("2. Kilómetros a Millas")
    elif opcion == 2:
        print("Seleccione la conversión de Volumen:")
        print("1. m3 a pie3")
        print("2. pie3 a m3")
    elif opcion == 3:
        print("Seleccione la conversión de Longitud:")
        print("1. Pies a Metros")
        print("2. Metros a Pies")
        print("3. Yardas a Metros")
        print("4. Metros a Yardas")

def realizar_conversion(opcion, conversion):
    if opcion == 1:
        if conversion == 1:
            millas = float(input("Ingrese millas: "))
            print(f"{millas} millas son {millas_a_kilometros(millas):.2f} kilómetros")
        elif conversion == 2:
            kilometros = float(input("Ingrese kilómetros: "))
            print(f"{kilometros} kilómetros son {kilometros_a_millas(kilometros):.2f} millas")
    elif opcion == 2:
        if conversion == 1:
            m3 = float(input("Ingrese m3: "))
            print(f"{m3} m3 son {m3_a_pie3(m3):.2f} pie3")
        elif conversion == 2:
            pie3 = float(input("Ingrese pie3: "))
            print(f"{pie3} pie3 son {pie3_a_m3(pie3):.2f} m3")
    elif opcion == 3:
        if conversion == 1:
            pies = float(input("Ingrese pies: "))
            print(f"{pies} pies son {pies_a_metros(pies):.2f} metros")
        elif conversion == 2:
            metros = float(input("Ingrese metros: "))
            print(f"{metros} metros son {metros_a_pies(metros):.2f} pies")
        elif conversion == 3:
            yardas = float(input("Ingrese yardas: "))
            print(f"{yardas} yardas son {yardas_a_metros(yardas):.2f} metros")
        elif conversion == 4:
            metros = float(input("Ingrese metros: "))
            print(f"{metros} metros son {metros_a_yardas(metros):.2f} yardas")

def main():
    while True:
        mostrar_menu_principal()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 4:
            break
        elif opcion in [1, 2, 3]:
            mostrar_menu_conversion(opcion)
            conversion = int(input("Ingrese una opción de conversión: "))
            realizar_conversion(opcion, conversion)
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()