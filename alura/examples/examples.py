def cria_conta(numero,titular,saldo,limite):
    conta = { "numero": numero, "titular": titular, "saldo":saldo, "limite":limite }
    return conta


def deposita(conta,valor):
    conta["saldo"] += valor
    return True


def saca(conta,valor):
    conta["saldo"] -= valor
    return True


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))


if __name__ == "__main__":
    conta = cria_conta(123,"Nico", 55.0, 1000.0)
    print("conta: ", conta)
    deposita(conta, 15.0)
    print('depósito 15.0')
    extrato(conta)
    saca(conta,20.0)
    print('saque 20.0')
    extrato(conta)