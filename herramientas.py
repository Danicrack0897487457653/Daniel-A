def generar_byte_caracter(caracter):
    # Convierte el carácter a su representación en byte
    byte = bin(ord(caracter)).replace("0b", "")
    # Asegura que el byte tenga 8 bits
    byte = byte.zfill(8)
    return byte

def generar_byte_palabra(palabra):
    # Genera la representación en byte de cada carácter en la palabra
    bytes_palabra = [generar_byte_caracter(caracter) for caracter in palabra]
    # Une los bytes con espacios entre ellos
    byte_palabra = " ".join(bytes_palabra)
    return byte_palabra

def generar_ascii(byte):
    # Convierte la representación en byte a su valor ASCII
    caracter = chr(int(byte, 2))
    return caracter

def menu():
    print("Menú:")
    print("1. Generar la representación en byte de un carácter.")
    print("2. Generar la representación en byte de una palabra.")
    print("3. Generar la representación ASCII de un byte.")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            caracter = input("Ingrese el carácter: ")
            byte_caracter = generar_byte_caracter(caracter)
            print("Representación en byte:", byte_caracter)
        elif opcion == "2":
            palabra = input("Ingrese la palabra: ")
            byte_palabra = generar_byte_palabra(palabra)
            print("Representación en byte:", byte_palabra)
        elif opcion == "3":
            byte = input("Ingrese el byte: ")
            caracter = generar_ascii(byte)
            print("Representación ASCII:", caracter)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
