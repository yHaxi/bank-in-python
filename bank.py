lista_saques = []
lista_depositos = []
    
class Conta(object):
    
    def __init__(self,nome,cpf,senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = 0
        
        
    def sacar(self,valor):
        if(self.saldo>=valor):
            self.saldo-=valor
            lista_saques.append(valor)
            print('-'*10,'\nSaldo atual',"\n>",self.saldo,"\n-----------")
        else:
            print('Brother, quer um dinheiro emprestado? tá muito pobrinho')
            
    def depositar(self,valor):
        self.saldo+=valor
        lista_depositos.append(valor)
        print("Saldo atual \n> ", self.saldo)
       
        
    def mostrar(self):
        print("Saldo atual \n>  ", self.saldo)
        
i=0
print("-"*5, "Cadastre-se", "-"*5)
nome = input("Digite seu nome completo \n-> ")
cpf = input("Digite seu CPF \n-> ")
while(i==0):
    senha = input("Senha \n->")
    senha2 = input("Confirme a senha \n->")
    if (senha==senha2):
        conta=Conta(nome,cpf,senha)
        print("Cadastro efetuado com sucesso!")
        i=1
    else:
        print("Senhas não combinam \nDigite novamente")
a=0
while(a==0):
    print('-'*6, 'Painel', '-'*6)
    print('-> Depositar (1)')
    print('-> Sacar (2)')
    print('-> Verificar Saldo (3)')
    print('-> Consultar Extrato (4)')
    print('-> Finalizar Sessão (5)')
    print('-'*20,)
    op = int(input("\nDigite o valor da operação \n ->"))
    if(op==1):
        valor=float(input("Valor a ser depositado\n-> "))
        conta.depositar(valor)
    elif(op==2):
        valor=float(input("Valor a ser sacado\n-> "))
        conta.sacar(valor)
    elif(op==3):
        conta.mostrar()
    elif(op==4):
        print('-> Extrato de depositos (1)\n-> Extrato de Saques (2)')
        extract = int(input("Digite a operação: "))
        if extract == 1:
            for i in lista_depositos:
                print(f"Você depositou\n> ${i}")
        elif extract == 2:
            for x in lista_saques:
                print(f"Você sacou\n> ${x}")
    elif(op==5):
        a=1
    else:
        print("Operção invalida")
    
    
    
    
    
    
    
    