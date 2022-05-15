class Conta:
    def __init__(self, numero, titular, saldo, limite ):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__condigo_banco = "001"
    
    @staticmethod
    def get_codigo_banco():
        return "001"

    @staticmethod
    def get_codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco': '237'}

    def extrato (self):
        print("Saldo: {} Titular: {}".format(self.__saldo,self.__titular))
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
         

    def saque(self, valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Seu saldo de {} não é suficiente para retirar {} ".format(self.__saldo, valor))

    def transferir(self, valor, conta_destino):
        self.saque(valor)
        conta_destino.depositar(valor)
        print("Transferencia realizada no valor de {} para {}".format(valor,conta_destino))

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def get_numero_conta(self):
        return self.__numero

    def set_limite(self, limite):
        self.__limite = limite