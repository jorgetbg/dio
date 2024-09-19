import time
from datetime import date

usuarios=[]
contas=[]
LIMITE_SAQUES=3


usuarios.append({"nome":'Jorge',"cpf":'123456789',"data_nascimento":'11/05/1900',"endereco":'José Otímo'})
contas.append({'cpf':'123456789','agencia':'0001',"numero":'01',"saldo":500.35,'extrato':"","limite":500,"numero_saques":0})

print(contas[0])
    


def pausa():
    time.sleep(3)

def menu():
    opcao =input( """
        o que deseja fazer? \n
            [u] Criar Usuario
            [c] Criar conta
            [d] Depositar
            [s] Sacar
            [e] Extrato
            [o] Saldo
            [q] Sair

        => """)
    if opcao == 'u':
        criar_usuario()
    elif opcao == 'c':
        criar_conta()
    elif opcao=='d':
        depositar(None)
    elif opcao=='s':
        sacar(None)
    elif opcao=='e':
        exibir_extrato(None)
    elif opcao=='o':
        ver_saldo()


    else: return opcao
    

def sacar(conta):
    
    if not conta:
        conta=opcao_de_conta()
    valor=(float(input("\nInforme o valor solicitado\n")))


    acima_limite=valor>conta['limite']
    acima_saldo=valor>conta['saldo']
    acima_saques=conta['numero_saques']>=LIMITE_SAQUES

    if(acima_saldo):
        print("Valor maior que o saldo")            
        sacar(conta)
    elif(acima_limite):
        
        print("Valor mair que o Limite")
        sacar(conta)
    elif(acima_saques):
        print("Valor maior que o limite permitido")
    
    else:
        conta['saldo']-=valor
        atualizar_extrato(conta, f"**Saque:\t\t {valor:.2f}\n")
        print(f"\n Seu novo Saldo é {conta['saldo']:.2f}")
    pausa()
    
    

def depositar(conta):
    if not conta:
        conta=opcao_de_conta()

    valor=(float(input("\nInforme o valor solicitado\n")))
    if(valor>0):
        conta['saldo']+=valor
        atualizar_extrato(conta, f"Deposito:\t\t {valor:.2f}\n")
        print(f"\n Seu novo Saldo é {conta['saldo']:.2f}")
        pausa()
    else:
        print("Valor invalido, insira um valor acima de 0")
        depositar(conta)

def opcao_de_conta():
    opcao=input("Qual opção você deseja inserir para continuar\n1)CPF\n2)Número da Conta")
    if(opcao=='1'):
        cpf=input("insira o CPF da conta")
        contas_do_usuario=filtrar_contas(cpf)
        print('\nQual conta deseja usar\n')
        i=1
        for conta in contas_do_usuario:
            print(f'{i} -- {conta['numero']}')
            i+=1
        conta_escolhida=contas_do_usuario[int(input('\n'))-1]
        return conta_escolhida
    elif(opcao=='2'):
        conta_escolhida=int(input('Insira o número da conta'))
   
        return contas[conta_escolhida-1]
    print('opcao invalida')

def filtrar_contas(cpf):
    contas_filtradas= [conta for conta in contas if conta['cpf']==cpf]
    return contas_filtradas




def exibir_extrato(conta):
    if not conta:
        conta=opcao_de_conta()
    print("\n__________________________EXTRATO______________________")
    print(conta['extrato'])
    print("\n___________________________FIM_________________________")


def atualizar_extrato(conta, operacao):
    data_atual='{}/{}/{}'.format(date.today().day, date.today().month,date.today().year)
    conta['extrato']+=f'{data_atual}\t\t{operacao}'

def criar_usuario():
    cpf=input("Informe o cpf do usuario (somente numeros)")
    usuario = filtrar_usuario(cpf,usuarios)
    if usuario:
        print("Usuario ja cadastrado")
        programa()

    nome=input("Insira o Nome do Usuario")
    data_nascimento=input("insira a data de nascimento")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({"nome":nome,"cpf":cpf,"data_nascimento":data_nascimento,"endereco":endereco})
    print("usuario cadastrado\n\n", usuarios[-1])
    programa()

def filtrar_usuario(cpf, usuarios):
    usuario_existente = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuario_existente



def criar_conta():
    cpf=input("Informe o cpf do usuario (somente numeros)")
    usuario=filtrar_usuario(cpf,usuarios)
    if not usuario:
        print("usuario não cadastrado, favor criar usuario primeiro")
        programa()
    numero_conta=len(contas)
    saldo=float(input("Digite o saldo inicial da conta"))
    limite=float(input("Digite o limite inicial da conta"))
    conta={'cpf':cpf,'agencia':'0001',"numero":numero_conta,"saldo":saldo,'extrato':[],"limite":limite,"numero_saques":0}
    contas.append(conta)
    print("conta criada com sucesso")
    programa()

def ver_saldo():
    conta=opcao_de_conta()
    print(f'Seu saldo atual é {conta['saldo']:.2f}')
    pausa()

def programa():
    if menu()!='q':
        programa()
    else: print("Obrigado por usar nosso sistema") 

programa()


