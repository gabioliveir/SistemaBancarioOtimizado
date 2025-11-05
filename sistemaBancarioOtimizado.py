

def menu():
    menu = """
    Bem-vindo(a) ao sistema bancário! Escolha uma opção do menu:
    ______________MENU___________________
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar usuário
    [c] Cadastrar conta corrente
    [q] Sair
    _________________________________________
    => """
    return input(menu)

def sacar(*, saldo,valor_saque,num_saque,lim_saque,limite_conta,extrato):

    excedeu_saldo = valor_saque > saldo

    excedeu_limite = valor_saque > limite_conta

    excedeu_saques = num_saque >= lim_saque

    if excedeu_saldo:
         print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
         print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
         print("Operação falhou! Número máximo de saques excedido.")

    elif valor_saque > 0:
        saldo -= valor_saque
        extrato += f"Saque: R$ {valor_saque:.2f}\n"
        num_saque += 1
        print("Saque realizado com sucesso")


    else:
        print("Operação falhou! O valor informado é inválido.")
    
    
    return saldo, extrato

def  depositar(saldo,valor_deposito,extrato, /):
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        print("\n Deposito realizado com sucesso")
    else:
        print( "Operação falhou! O valor informado é inválido.")
    
    return saldo,extrato

def mostrar_extrato(saldo, /,* ,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = input("Informe somente o número do CPF : ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Já esxite um usuário com esse CFP!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento neste formato (dd-mm-aaaa): ")
    endereco = input("Inform o endereço nesse padrão(logradouro,nro - bairro - cidade/sigla estado): ")

    usuarios.append({'nome': nome,'data_nascimento': data_nascimento,'cpf': cpf,'endereco': endereco})

    print("Usuário cadastrado com sucesso!")



def criar_conta_corrente(agencia,numero_conta,usuarios,):
    cpf = input("Informe seu CPF: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta corrente criada com sucesso!")
        return {'agencia': agencia, 'numero_conta': numero_conta,'usuario': usuario}
   
    print("Usuário não encontrado")
    

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = " "
    numero_saques = 0
    num_conta = 0
    usuarios = []
    contas = []
    contador_numero_conta = 1
    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo,valor,extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo= saldo,
                valor_saque= valor,
                lim_saque= LIMITE_SAQUES,
                num_saque= numero_saques,
                limite_conta= limite,
                extrato= extrato
            )
        
        elif opcao == "u":
            criar_usuario(usuarios)

        
        elif opcao == "c":
            conta = criar_conta_corrente(AGENCIA,num_conta,usuarios)

            if conta:
                contas.append(conta)
                #para futuramente excluir contas 
                contador_numero_conta += 1 

        elif opcao == "e":
            mostrar_extrato(saldo,extrato=extrato)

        elif opcao == "q":
            print("Até a próxima!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()






