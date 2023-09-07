menu = """

[1] Depositar 
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    # DEPÓSITO
    if opcao == "1":
        resposta_usuario = float(input("Informe o valor do depósito: "))
        if resposta_usuario > 0:
            valor_deposito = resposta_usuario
        else:
            print("Operação falhou! O valor informado é inválido.")
            continue
        alerta = f"Você deseja confirmar o depósito de R$ {valor_deposito:.2f}? \n\n[1] Confirmar \n[0] Cancelar \n\n=> "
        opcao = int(input(alerta))
        if opcao == 1:
            print("Depósito realizado com sucesso!")
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        elif opcao == 0:
            print("Operação de depósito cancelada.")

    # SAQUE
    elif opcao == "2":
        valor_saque = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor_saque > 0:
            alerta = f"Você deseja confirmar o saque de R$ {valor_saque:.2f}? \n\n[1] Confirmar \n[0] Cancelar \n\n=> "
            opcao = int(input(alerta))
            if opcao == 1:
                print("Saque realizado com sucesso!")
                saldo -= valor_saque
                extrato += f"Saque: R$ {valor_saque:.2f}\n"
                numero_saques += 1
            elif opcao == 0:
                print("Operação de saque cancelada.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    # EXTRATO
    elif opcao == "3":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")        

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
