class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    def get_nome(self):
        print('[INFO] Getting value...')
        print('[INFO] Name "{}" getted sucessfully'.format(self.__nome))
        return self.__nome.title()

    @nome.setter
    def nome(self, value):
        print('[INFO] Setting new value...')
        self.__nome = value
        print('[INFO] New value: {}'.format(value))


if __name__ == '__main__':
    cliente = Cliente('thiago')
    cliente.nome
    cliente.nome = 'Thiago  Kasper'
