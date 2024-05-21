import os

def mostrar_menu():
    os.system ('cls')
    print("\nBienvenido al Consultorio Veterinario Los Milagros")
    print("1. Entrada de animal")
    print("2. Salida de animal")
    print("3. Consultar animales")
    print("4. Salir")

def entrada_animal(animales):
    nombre = input("Ingrese el nombre del animal: ")
    especie = input("Ingrese la especie del animal: ")
    motivo = input("Ingrese el motivo de la consulta: ")
    animales[nombre] = {
        "especie": especie,
        "motivo": motivo
    }
    print(f"{nombre} ha sido registrado en el consultorio.")

def salida_animal(animales):
    nombre = input("Ingrese el nombre del animal que va a salir: ")
    if nombre in animales:
        del animales[nombre]
        print(f"{nombre} ha salido del consultorio.")
    else:
        print(f"{nombre} no se encuentra en el consultorio.")

def consultar_animales(animales):
    if animales:
        print("Animales en el consultorio:")
        for nombre, detalles in animales.items():
            print(f"Nombre: {nombre}, Especie: {detalles['especie']}, Motivo: {detalles['motivo']}")
    else:
        print("No hay animales en el consultorio.")



def main():
    animales = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            entrada_animal(animales)
        elif opcion == "2":
            salida_animal(animales)
        elif opcion == "3":
            consultar_animales(animales)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()