import time

menu = """
o que deseja fazer? \n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

   => """

saldo=0
limite=500
extrato=""
numero_saques=0
LIMITE_SAQUES=3

while True:
    
    op=input(menu)
    if(op=='d'):
        valor=(float(input("\nInforme o valor solicitado\n")))
        if(valor>0):
            saldo+=valor
            extrato+=f"Deposito: {valor:.2f}\n"
            print(f"\n Seu novo Saldo é {saldo:.2f}")
        else:
            print("Valor invalido, insira um valor acima de 0")
    elif(op=='s'):
        valor=(float(input("Informe o valor solicitado")))
        acima_limite=valor>limite
        acima_saldo=valor>saldo
        acima_saques=numero_saques>=LIMITE_SAQUES

        if(acima_saldo):
            print("Valor maior que o saldo")            
        elif(acima_limite):
        
            print("Valor mair que o Limite")
        elif(acima_saques):
            print("Valor maior que o limite permitido")
        else:
            saldo-=valor
            extrato+=f"Saque: {valor:.2f}\n"
            print(f"\n Seu novo Saldo é {saldo:.2f}")
    elif(op=='e'):
        print("\n__________________________EXTRATO______________________")
        print(extrato)
        print("\n___________________________FIM_________________________")
    elif(op=='q'):
        break
    else:
        print("Opção Invalida")
    time.sleep(5)

print("Obrigado por usar nosso sistema")
