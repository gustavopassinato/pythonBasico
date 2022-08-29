
contador=1
listaClientes = []

while(contador <= 2 ):
    cliente = {}
    print("Digite as informações do cliente ", contador)
    print("-"*35)
    cliente.update({"agencia": 12345})
    cliente.update({"nome": input("Digite seu nome: ")})
    cliente.update({"telefone": input("Digite seu telefone: ")})
    cliente.update({"dataNascimento": input("Digite sua data de nascimento: ")})
    cliente.update({"cpf": input("Digite seu número do seu cpf: ")})
    cliente.update({"rendaMensal": float(input("Digite sua renda mensal: "))})
    cliente.update({"saldo": float(input("Digite seu saldo inicial: "))})
    cliente.update({"saques": []})
    cliente.update({"depositos": []})
    print("-"*35)
    print("")

    listaClientes.append(cliente)
    contador+=1


print("")
print("")
print("")
print("-"*35)
while(True):
    resposta = int(input("Digite 1 para realizar operação ou 0 para sair"))
    if(resposta == 1):
        numConta = int(input("Digite o numero da sua conta: "))

        print("")
        print("")
        print("")
        print("-"*35)

        cliente = listaClientes[numConta]

        while(True):
            print(listaClientes[0])
            print("")
            print("-"*35)
            print(listaClientes[1])
            print("")
            print("")
            print("")
            print("-"*35)
            opcao = int(input("Digite 1 para realizar saque, 0 para realizar deposito, 3 para sair ou 4 para transferir"))
            saldo = cliente["saldo"]
            if(opcao == 1): 
                retirada = float(input("Digite a quantidade a ser sacada: "))
                if(retirada<= saldo):
                    cliente["saldo"] -= retirada
                    cliente["saques"].append(retirada)
                elif(retirada> saldo):
                    print("Saldo insuficiente!")
            if(opcao == 0):
                entrada = float(input("Digite a quantidade a ser depositada: "))
                cliente["saldo"] += entrada
                cliente["depositos"].append(entrada)
            if(opcao == 4):
                numContaDestino = int(input("Digite o num da conta de destino: "))
                clienteDestino = listaClientes[numContaDestino]

                retirada = float(input("Digite a quantidade a ser transferida: "))
                if(retirada<= saldo):
                    cliente["saldo"] -= retirada
                    clienteDestino["saldo"] += retirada
                    cliente["saques"].append(retirada)
                    clienteDestino["depositos"].append(retirada)
                elif(retirada> saldo):
                    print("Saldo insuficiente!")

            if(opcao == 3):
                break
            else:
                print("Resposta inválida!")
    elif(resposta == 0 ):
        exit()
    else:
        print("Resposta inválida!")