from conta import Conta


def call_all_extracts(account_array):
    for item in account_array:
        item.extract()


def call_all_deposits(names, value):
    for item in names:
        item.deposit(value)


def call_all_withdraws(names, value):
    for item in names:
        item.withdraw(value)


def main():
    account_one = Conta(123, 'Thiago', 500.0)
    account_two = Conta(124, 'Erica', 595.0)
    account_three = Conta(125, 'Hacky Boy', 9955.0)
    account_names = [account_one, account_two, account_three]
    print('')
    print('*************************')
    print('* SALDO DE CADA TITULAR:')
    print('*************************')
    call_all_extracts(account_names)
    print('')
    print('*************************')
    print('* DEPÓSITOS: ')
    print('*************************')
    call_all_deposits(account_names, 255.0)
    # account_one.deposit(15.0)
    # account_two.deposit(85.0)
    # account_three.deposit(9999.0)
    print('')
    print('*************************')
    print('* SAQUES: ')
    print('*************************')
    call_all_withdraws(account_names, 150.0)
    # account_one.withdraw(99.0)
    # account_two.withdraw(85.0)
    # account_three.withdraw(15.0)
    print('')
    print('*************************')
    print('* TRANSFERÊNCIAS: ')
    print('*************************')
    account_one.transfer(10.0, account_two)
    print('')
    print('*************************')
    account_two.transfer(5.0, account_one)
    print('')
    print('*************************')
    account_three.transfer(15.0, account_one)


# TODO: Arrumar funções call_all
# TODO: Diminuir tamanho da main


if __name__ == '__main__':
    main()

