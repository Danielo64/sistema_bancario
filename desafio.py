menu = """
        Banco de São Paulo

        1- Depósito
        2- Saque
        3- Extrato
        4- Sair
    """

deposito = 0;
numero_saques = 0;
saldo = 0.0;
SAQUE_DIARIO = 3;
extrato = "";

while True:
    print(menu);
    
    opcao = int(input("Digite uma opção: "));

    if opcao == 1:
        deposito = float(input("Digite o valor que deseja depositar: "));

        if deposito < 0:
            print("Não é permitido depositar valores negativos!");
        
        else:
            saldo += deposito;
            extrato += f"Depósito: R$ {deposito:.2f}\n";

    elif opcao == 2:
        if numero_saques >= SAQUE_DIARIO:
            print("Limite atingido de saques diários!");
        
        else:
            saque = float(input("Digite o valor que deseja sacar: "));

        if saque > saldo:
            print("Saldo indisponível para fazer saque!");
        
        elif saque > 500:
            print("Não é possível sacar mais do que R$500!");

        elif saque > 0:
            saldo -= saque;
            extrato += f"Saque: R$ {saque:.2f}\n";
            numero_saques += 1;
    
        else:
            print("O valor informado é inválido!");
    
    elif opcao == 3:
        print("Não foram feitas movimentações na conta" if not extrato else extrato);

        print(f"Saldo atual: R$ {saldo:.2f}");
    
    elif opcao == 4:
        break;

    else:
        print("Opção inválida. Tente novamente!");