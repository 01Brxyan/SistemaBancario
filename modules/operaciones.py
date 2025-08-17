banco = {}
clientes = {}

def crear_cuenta(id_cliente, nombre, saldo_inicial):
    if id_cliente not in clientes:
        clientes[id_cliente] = {"nombre": nombre, "saldo": saldo_inicial, "credito": 0, "cuotas": 0}
        banco[id_cliente] = clientes[id_cliente]
        return True
    return False

def depositar(id_cliente, monto):
    if id_cliente in clientes and monto > 0:
        clientes[id_cliente]["saldo"] += monto
        return True
    return False

def retirar(id_cliente, monto):
    if id_cliente in clientes and 0 < monto <= clientes[id_cliente]["saldo"]:
        clientes[id_cliente]["saldo"] -= monto
        return True
    return False

def solicitar_credito(id_cliente, monto, cuotas):
    if id_cliente in clientes and monto > 0 and cuotas > 0:
        clientes[id_cliente]["credito"] += monto
        clientes[id_cliente]["cuotas"] = cuotas
        clientes[id_cliente]["saldo"] += monto
        return True
    return False

def pagar_cuota(id_cliente, monto):
    if id_cliente in clientes and clientes[id_cliente]["credito"] > 0:
        cuota = clientes[id_cliente]["credito"] / clientes[id_cliente]["cuotas"]
        if monto >= cuota and clientes[id_cliente]["saldo"] >= monto:
            clientes[id_cliente]["saldo"] -= monto
            clientes[id_cliente]["credito"] -= cuota
            clientes[id_cliente]["cuotas"] -= 1
            return True
    return False

def cancelar_cuenta(id_cliente):
    if id_cliente in clientes and clientes[id_cliente]["saldo"] == 0 and clientes[id_cliente]["credito"] == 0:
        del clientes[id_cliente]
        del banco[id_cliente]
        return True
    return False

def ver_info(id_cliente):
    if id_cliente in clientes:
        return clientes[id_cliente]
    return None
