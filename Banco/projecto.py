import os

# Varriáveis para arzenar o total em coonta, extrato, limite de saque
saldoTotal= 0;
extrato="";
LIMITE_SAQUE= 3;
operacoes_de_saque = 0;
#--------------------------------------------------
while True:
    # AREA DE BOAS VINDAS AO BANCO
    confirm= int(input("""
    --------------------------------------------
    |          BEM VINDO AO TITO-BANK          |
    --------------------------------------------
    |   DESEJA COMEÇAR A EFECTUAR OPERAÇÕES?   |
    --------------------------------------------
    |                Sim = 1 Não = 0           |
    --------------------------------------------
                        """));
     # Menu de acções do banco
    os.system('cls')
    if confirm == 1:
        opcao=int(input("""
    ---------------------------------------------
    |            OPERAÇÕES DISPONÍVEIS          |
    ---------------------------------------------
    |                                           |
    |                 1- DEPÓSITO               |
    |                 2- SAQUE                  |
    |                 3- VER EXTRATO            |
    |                                           |
    ---------------------------------------------
    |           ESCOLHA UMA OPERAÇÃO            |
    ---------------------------------------------
                        """));
    # Verficando as operações    
        os.system('cls')
        if opcao == 1:
            while True:
                valor= int(input("""
    ---------------------------------------------
    |    INSIRA O VALOR QUE DESEJAS DEPOSITAR   |
    ---------------------------------------------
                        """));
    # O DEPÓSITO SÓ ACONTECE CASO O VALOR FOR POSITIVO
                os.system('cls')
                if valor >= 1:
                    print(f"""
    ---------------------------------------------
    |     COMPRAVATIVO DE DEPÓSITO TITO-BANK    |
    ---------------------------------------------
    |             DEPÓSITO DE R$ {valor:.2f}     |
    ---------------------------------------------
    |         OPERAÇÃO FEITA COM SUCESSO!       |
    ---------------------------------------------
                        """);
                    #EFECTUANDO O DEPÓSITO
                    saldoTotal +=valor;
                    extrato += f"Depósito de R$ {valor:.2f} || ";
                    break;
                else:
# Garantindo que o usuário digite apenas valores positivos, caso não o programa irá lhe manda inserir o valo novamente
                    continuar_operacao=int(input("""
    ----------------------------------------------
    | O VALOR A SER DEPOSISTADO DEVE SER POSITIVO |
    -----------------------------------------------
    |      Deseja continuar ? sim = 1 não = 0     |
    -----------------------------------------------
                        """));
# PÓS ELE ERRAR NO VALOR QUE DEVERIA SER INTEIRO O PROGRAM LHE PERGUNTA SE ELE DESEJA VOLTAR A TENTAR OU VAI VOLTAR AO MENU PRINCIPAL
                    os.system('cls');
                    if continuar_operacao== 0:
                       break;
        #OPRAÇÃO DE SAQUE
        elif opcao == 2:
             while True:
                valor= int(input("""
    ----------------------------------------------
    |     INSIRA O VALOR QUE DESEJAS SACAR       |
    ----------------------------------------------
                        """));
                os.system('cls');
    # CONTROLANDO O NÚMERO DE VEZES QUE O USUÁRIO JÁ FEZ O SAQUE
                if LIMITE_SAQUE <= int(operacoes_de_saque):
                    os.system('cls');
                    print("""
    -----------------------------------------------
    |     VOCÊ SÓ PODE REALIZAR 3 SAQUES DIÁRIOS  |
    -----------------------------------------------
                        """);
                    break;
         # VERIFICANDO SE O SAQUE ESTÁ DENTRO DO LIMITE DE SAQUE POR DIA R$ 5OO,00
                if saldoTotal >= valor and valor > 0 and valor <= 500:
                    print(f"""
    ---------------------------------------------
    |     COMPRAVATIVO DE SAQUE TITO-BANK       |
    ---------------------------------------------
    |             SAQUE DE R$ {valor:.2f}       |
    ---------------------------------------------
    |         OPERAÇÃO FEITA COM SUCESSO!       |
    ---------------------------------------------
                        """);
                       #EFECTUANDO O SAQUE
                    saldoTotal -= valor;
                    operacoes_de_saque += 1;
                    extrato += (f"SAQUE de R$ {valor:.2f} || ");
                    break;
                elif valor > 500:
                    #EXIBINDO SMS DE ERRO CASO SE TENTAR FAZER SAQUE A CIMA DE 5OO
                    os.system('cls');
                    continuar_operacao=int(input("""
    ----------------------------------------------
    |    O VALOR LIMITE DE SAQUE É  R$ 500,00    |
    ----------------------------------------------
    |   DESEJA CONTINUAR ? Sim = 1 Não = 0       |
    ----------------------------------------------
                        """));
                    os.system('cls');
                    if continuar_operacao== 0:
                       break;
                else:
                    #ESTA SMS DE ERRO É EXIBIDA QUANDO O USUÁRIO TENTA SACAR UM VALOR ACINA DO TEM OU MESMO NEGATIVO E QUANDO N TENS DINHEIRO EM CONTA
                    print("""
    ------------------------------------------------
    |                 SAQUE INVÁLIDO               |
    ------------------------------------------------
    |  POSSIVELMENTE NÃO TENS SALDO NA CONTA, OU O |
    |  VALOR A  SACAR É MAIOR AO QUE TENS NA CONTA |
    |    POR ISTO NÃO TERÁS COMO SACAR O DINHEIRO  |
    |----------------------------------------------|
        """);
                    break;
        elif opcao==3:
            # EXIBINDO O EXTRATO BANCÁRIO
            resultado_extrato=("Nenhuma movimentação foi feita em sua conta." if not extrato else extrato);
            print(f"""
    -------------------------------------------------------------------------------------------------------------------------------------------
    |                                                    FACTURA DE ESTRATO BANCÁRIO                                                          |  
    -------------------------------------------------------------------------------------------------------------------------------------------
    |   REGISTRO DE ESTRATOS  REALIZADO: {resultado_extrato}                                                                                  |
    -------------------------------------------------------------------------------------------------------------------------------------------
    |   SALDO ACTUAL DE CONTA: {saldoTotal:.2f}                                                                                               |
    -------------------------------------------------------------------------------------------------------------------------------------------
    |                                                    EXTRATO DE CONTAS TITO BANK                                                          |  
    -------------------------------------------------------------------------------------------------------------------------------------------
            """);
    else:
        print("""
    ---------------------------------------------
    |    OBRIGADO PELA VISITA AO NOSSO BANCO    |
    ---------------------------------------------
        """);
        break;
     