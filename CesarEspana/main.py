def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("\nElige una operación (1-5): ")
        
        if opcion == '5':
            print("¡Hasta luego!")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Primer número: "))
                num2 = float(input("Segundo número: "))
                
                if opcion == '1':
                    print(f"Resultado: {num1 + num2}")
                elif opcion == '2':
                    print(f"Resultado: {num1 - num2}")
                elif opcion == '3':
                    print(f"Resultado: {num1 * num2}")
                elif opcion == '4':
                    if num2 != 0:
                        print(f"Resultado: {num1 / num2}")
                    else:
                        print("Error: No se puede dividir entre 0")
            except ValueError:
                print("Error: Ingresa números válidos")
        else:
            print("Opción no válida")

if __name__ == "__main__":
    calculadora()