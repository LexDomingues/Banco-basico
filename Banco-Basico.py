def login():
    usuario = input("Digite o nome do usuário: ")
    senha = input("Digite sua nova senha do banco (8 dígitos):")
    if len(senha) < 8:
        print("A senha deve conter pelo menos 8 caracteres.")
    else:
        print("Senha criada com sucesso!")
    return usuario, senha
usuario, senha = login()
informacoes_usuario = {
    "nome": usuario,
    "senha": senha
}
def verificar_senha(senha_digitada):
    if senha_digitada == informacoes_usuario["senha"]:
        return True
    else:
        return verificar_senha(input("Senha incorreta. Digite sua senha novamente:"))
print("Seja bem-vindo ao Banco Básico, " + usuario + "! Digite sua senha para acessar sua conta.")
verificar_senha_digitada = input("Digite sua senha:")
if verificar_senha(verificar_senha_digitada):
    print("Acesso concedido!")

class Conta:
    def __init__(self, saldo = 0):
        Conta._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            Conta._saldo += valor
            print(f"Depósito de R${valor} realizado com sucesso.")
    
    def sacar(self, valor):
        if valor > Conta._saldo:
            print("Saldo insuficiente para saque.")
        elif valor <=0:
            print("Valor de saque deve ser positivo.")
        else:
            Conta._saldo -= valor
            print(f"Saque de R${valor} realizado com sucesso.")

conta = Conta()
def mostrar_saldo():
    print(f"Saldo atual: R${conta._saldo}")

def mostrar_menu():
    opcao = input("O que você irá fazer hoje " + informacoes_usuario["nome"] + "?" + "\n1 - Depositar\n2 - Sacar" + "\nDigite o número da opção desejada: ")
    print(opcao)
    if opcao == "1":
     valor = float(input("Digite o valor a ser depositado: "))
     conta.depositar(valor)
     mostrar_saldo()
     return mostrar_menu()
    elif opcao == "2":
     valor = float(input("Digite o valor a ser sacado: "))
     conta.sacar(valor)
     mostrar_saldo()
     return mostrar_menu()

mostrar_menu()