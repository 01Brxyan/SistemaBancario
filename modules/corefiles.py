import modules.operaciones as operaciones

def menu():
    while True:
        print("   Menu   ")
        print("1. Crear Cuenta")
        print("2. Depositar Dinero")
        print("3. Solicitar Credito")
        print("4. Retirar Dinero")
        print("5. Pago Cuota Credito")
        print("6. Cancelar Cuenta")
        print("7. Ver Información de Cuenta")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_cliente = input("ID Cliente: ")
            nombre = input("Nombre: ")
            saldo = float(input("Saldo inicial: "))
            if operaciones.crear_cuenta(id_cliente, nombre, saldo):
                print("Cuenta creada")
            else:
                print("El cliente ya existe")

        elif opcion == "2":
            id_cliente = input("ID Cliente: ")
            monto = float(input("Monto a depositar: "))
            if operaciones.depositar(id_cliente, monto):
                print("Depósito exitoso")
            else:
                print("Error en el depósito")

        elif opcion == "3":
            id_cliente = input("ID Cliente: ")
            monto = float(input("Monto del crédito: "))
            cuotas = int(input("Número de cuotas: "))
            if operaciones.solicitar_credito(id_cliente, monto, cuotas):
                print("Crédito aprobado")
            else:
                print("No se pudo otorgar el crédito")

        elif opcion == "4":
            id_cliente = input("ID Cliente: ")
            monto = float(input("Monto a retirar: "))
            if operaciones.retirar(id_cliente, monto):
                print("Retiro exitoso")
            else:
                print("Error en el retiro")

        elif opcion == "5":
            id_cliente = input("ID Cliente: ")
            monto = float(input("Monto del pago: "))
            if operaciones.pagar_cuota(id_cliente, monto):
                print("Pago realizado")
            else:
                print("Error en el pago")

        elif opcion == "6":
            id_cliente = input("ID Cliente: ")
            if operaciones.cancelar_cuenta(id_cliente):
                print("Cuenta cancelada")
            else:
                print("No se pudo cancelar la cuenta")

        elif opcion == "7":
            id_cliente = input("ID Cliente: ")
            info = operaciones.ver_info(id_cliente)
            if info:
                print(info)
            else:
                print("Cliente no encontrado")

        elif opcion == "8":
            break

        else:
            print("Opción inválida")
