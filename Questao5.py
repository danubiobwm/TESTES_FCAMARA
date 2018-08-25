class Conta:

    def __init__(self, numero, nome, saldo=0):
        self.numero = numero
        self.correntista = nome
        self.saldo = saldo

    def alterarNome(self, nome):
        self.correntista = nome

    def deposito(self, valor):
        self.saldo = self.saldo + valor

    def saque(self, valor):
        self.saldo = self.saldo - valor

    def transferencia(self, outra, valor):
        self.saque(valor)
        outra.deposito(valor)


c1 = Conta(123, "JOAQUIM MOURA")
c2 = Conta(456, "MARIA DAS DORES")
c1.deposito(50)
c1.saque(10)
c1.deposito(100)
c1.transferencia(c2, 50)
c2.saque(30)

c1.alterarNome("JOAQUIM DE MOURA SILVA")
c2.alterarNome("MARIA DAS DORES BEZERRA")
print (c1.correntista,"Saldo c1: %i" %(c1.saldo))
print (c2.correntista, "Saldo c2: %i"%(c2.saldo))