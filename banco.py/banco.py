class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def ver_extrato(self):
        print(f"\nExtrato da Conta {self.numero} de {self.cliente.nome}")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")


# Simulação do sistema bancário
if __name__ == "__main__":
    # Criando um cliente
    cliente1 = Cliente("Líndici", "123.456.789-00")

    # Criando uma conta para esse cliente
    conta1 = Conta("001", cliente1)

    # Adicionando a conta ao cliente
    cliente1.adicionar_conta(conta1)

    # Realizando operações
    conta1.depositar(500)
    conta1.sacar(100)

    # Exibindo extrato
    conta1.ver_extrato()
