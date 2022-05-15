class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    def set_nome_cliene(self, novo_nome):
        self.__nome = novo_nome

    def get_nome_cliente(self):
        return self.__nome.title()


