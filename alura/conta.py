# começar com letra maiúscula o nome

class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0) -> object:
        print('[INFO] Endereço alocado: {}'.format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extract(self):
        print('- O titular {} possui o de saldo: R${}'.format(self.__titular, self.__saldo))
        return True

    def deposit(self, value):
        self.__saldo += value
        print('- O novo saldo do titular {} é: R${}'.format(self.__titular, self.__saldo))
        return True

    def transfer(self, value, destinatario):
        self.withdraw(value)
        destinatario.deposit(value)
        print('[INFO] Transferência de R${} bem sucedida'.format(value))
        return True

    def __can_withdraw(self,value):
        available_balance = (self.__saldo + self.__limite)
        return value <= available_balance

    def withdraw(self, value):
        if (self.can_withdraw(value)):
            self.__saldo -= value
            print('- O novo saldo do titular {} é: R${}'.format(self.__titular, self.__saldo))
            return True
        else :
            print('Operação inválida! Não se deve sacar um valor maior que o limite permitido.')

    # *********************
    #       GETTERS
    # *********************
    def get_balance(self):
        return self.__saldo

    def get_name(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def all_banks_codes():
        return {"BB": '001', "Caixa Econõmica Federal": '104', "Bradesco": '237'}

    # *********************
    #       SETTERS
    # *********************
    @limite.setter
    def limite(self, limit):
        self.__limite = limit
        print('[INFO] Alteração do limite bem sucedida! Agora você possui um limite de R${}'.format(limit))
        # - 'set nunca retorna nada' ~ Nico


