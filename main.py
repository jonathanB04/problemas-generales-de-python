import os

def main():
    # Obtener la lista de archivos en el directorio actual
    files = os.listdir()

    while True:
        print("\n\n 😄==== Menú ====😄")
        for i, filename in enumerate(files, start=1):
            # Mostrar opciones numeradas según los archivos en el directorio
            print(f"{i}. Ejecutar función de {filename}")

        print("q. Salir")
        choice = input("Elige una opción: ")
        print("\n")

        if choice.isdigit() and 1 <= int(choice) <= len(files):
            try:
                # Obtener el nombre del módulo sin la extensión .py
                module_name = files[int(choice) - 1].rstrip(".py")
                # Importar dinámicamente el módulo
                module = __import__(module_name)
                # Llamar a la función sum_numbers() del módulo
                module.sum_numbers()
            except ImportError:
                print(f"No se pudo importar {module_name}. Verifica que el módulo existe y tiene la función 'sum_numbers'.")
            except AttributeError:
                print(f"El módulo {module_name} no tiene la función 'sum_numbers'.")
            except Exception as e:
                print(f"Error al ejecutar {module_name}: {e}")
        elif choice == "q":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
