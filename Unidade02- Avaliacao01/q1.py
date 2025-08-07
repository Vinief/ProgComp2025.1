'''
1) (4 pontos) Faça um programa que permita o cadastramento de MAC adresses
vinculados a um CPF. O seu programa suportar as seguintes operações: 
a) cadastrar CPF; 
b) adicionar MAC address a um CPF; 
c) remover um MAC address de um CPF; 
d) remover o CPF (só permitir se não existirem MAC addresses vinculados);
e) listar os CPF cadastrados; 
f) listar os MAC adresses vinculados a um CPF; 
g) salvar o “banco de dados” em um arquivo (perguntar o nome do arquivo); 
h) ler o “banco de dados” de um arquivo (perguntar o nome do arquivo). 
Em todas as operações que requerem entrada de CPF e MAC adresses, valide-os.
'''
import json
import cpf # Importa uma função para validação de CPF!

tabela_cpf_mac = {}
#tabela_cpf_mac = {12345678900:['00:1A:2B:3C:4D:5E','00:1C:2A:3B:4D:5E'] ,'11630408433':['00:1A:2B:3C:4D:5E']}
#print(tabela_cpf_mac) # testes

###################################################################################################################
# Função do menu principal!
def menu_principal():   
    print  (    "\n" + f"{'CÓDIGO':^6s} : AÇÃO QUE DESEJA REALIZAR\n" + 
                f"{'1':^6s} : Cadastrar CPF\n" + f"{'2':^6s} : Adicionar MAC address a um CPF\n" + 
                f"{'3':^6s} : Remover um MAC address de um CPF\n" + f"{'4':^6s} : Remover o CPF\n" + 
                f"{'5':^6s} : listar os CPF cadastrados\n" + 
                f"{'6':^6s} : listar os MAC adresses vinculados a um CPF\n" + 
                f"{'7':^6s} : Salvar o “banco de dados” em um arquivo\n" + 
                f"{'8':^6s} : ler o “banco de dados” de um arquivo\n" + 
                f"{'0':^6s} : Finaliza o programa\n\n" + "Digite o código da ação que deseja realizar: "
                )
    return int (input("Selecione sua opcao: "))
###################################################################################################################
###################################################################################################################
# Função de verificação de MAC Address!
# Um endereço MAC válido é composto por 12 dígitos hexadecimais (0-9 e A-F), 
# geralmente separados por dois pontos ou hífens, como 00:1A:2B:3C:4D:5E
def check_mac(mac : str) -> bool:
    if type(mac) != str:
        return False
    # Tenta converter para hexadecimal!
    var_2 = mac.split(':')
    for x in var_2:
        try:
            int(x , 16)
        except:
            return False
    # Checa se contem 12 caracteres!
    mac = mac.replace(":", "").replace("-", "")
    if len(mac) != 12:
        return False
    print("MAC Válido")
    return True
###################################################################################################################
###################################################################################################################

# Chamado da função menu!
opcao = menu_principal()
###################################################################################################################
###################################################################################################################
# Cadastra um CPF!
if opcao == 1: # a
    print("Cadastrar um CPF!\n")
    var_1= input("Digite o CPF a qual deseja cadastrar: ")
    if cpf.cpf_valido(var_1) == True:
        #
        # This method adds a key with a specified default value if the key is not already present in the dictionary.
        tabela_cpf_mac.setdefault(var_1,[])
    else:
        print("CPF Inválido!")
###################################################################################################################
###################################################################################################################
# Adicionar MAC address a um CPF!
if opcao == 2:  # b
    print("Adicionar MAC address a um CPF!\n")
    var_3 = input("Digite a qual CPF deseja cadastrar um endereço MAC: ")
    if cpf.cpf_valido(var_3) == True:
        if (var_3) in tabela_cpf_mac.keys():
            var_4 = input("Digite o endereço MAC que deseja cadastrar: ")
            if check_mac(var_4) == True:
                lista_temp = [] # lista vazia
                lista_temp = tabela_cpf_mac[var_3] # lista recebe valor da chave cpf
                #print("temp",lista_temp,type(var_3),type(lista_temp)) ############# # testes
                lista_temp = lista_temp.append(var_4)
                #print(tabela_cpf_mac[var_3],"455") ############## # testes
                tabela_cpf_mac[var_3] = lista_temp #???????????????????????
                #print("temp",tabela_cpf_mac[var_3],456) # testes
            else:
                print("O endereço MAC que deseja cadastrar é inválido!")
        else:
            print("O CPF informado não está cadastrado!")
    else:
        print("CPF Inválido!")       
###################################################################################################################
###################################################################################################################
if opcao == 3:  # c
    print("Remover um MAC address de um CPF!\n")
    var_5 = input("Digite a qual CPF deseja REMOVER um endereço MAC: ")
    if cpf.cpf_valido(var_5) == True:
        if (var_5) in tabela_cpf_mac.keys():
            var_6 = input("Digite o endereço MAC que deseja REMOVER: ")
            if check_mac(var_6) == True:
                lista_temp2 = [] # lista vazia
                lista_temp2 = tabela_cpf_mac[var_5] # lista recebe valor da chave cpf
                if var_6 in lista_temp2:
                    lista_temp2 = lista_temp2.pop(lista_temp2.index(var_6))
                    tabela_cpf_mac[var_5] = lista_temp2
                    #rint("temp",tabela_cpf_mac[var_5],777) # testes
                else:
                    print("O endereço MAC que deseja REMOVER não está vinculado a este CPF!")
            else:
                print("O endereço MAC que deseja cadastrar é inválido!")
        else:
            print("O CPF informado não está cadastrado!")
    else:
        print("CPF Inválido!")
###################################################################################################################
###################################################################################################################
if opcao == 4:  # d
    print("Remover um CPF cadastrado!\n")
    var_7 = input("Digite o CPF que deseja REMOVER: ")
    if cpf.cpf_valido(var_7) == True:
        if (var_7) in tabela_cpf_mac.keys():
            lista_temp3 = [] # lista vazia
            lista_temp3 = tabela_cpf_mac[var_7] # lista recebe valor da chave cpf
            if len(lista_temp3) == 0:
                del tabela_cpf_mac[var_7]
            else:
                print("O CPF que deseja remover contem MACs a ele associados e por isso não pode ser removido!")
        else:
            print("O CPF informado não está cadastrado!")
    else:
        print("CPF Inválido!")
###################################################################################################################
###################################################################################################################
# Lista os CPF cadastrados!
if opcao == 5: # e
    print("listando os CPF cadastrados!")
    for var in tabela_cpf_mac.keys():
        print("CPF:",var)    
###################################################################################################################
###################################################################################################################
# Lista os MAC adresses vinculados a um CPF!
if opcao == 6: # f
    print("Listar os MAC adresses vinculados a um CPF!\n")
    var_8 = input("Digite o CPF ao qual deseja cheacar os MACs a ele vinculado: ")
    if cpf.cpf_valido(var_8) == True:
        if (var_8) in tabela_cpf_mac.keys():
            lista_temp4 = [] # lista vazia
            lista_temp4 = tabela_cpf_mac[var_8] # lista recebe valor da chave cpf
            if len(lista_temp4) > 0:
                print(f"Listando os MAC adresses vinculados ao CPF: {var_8}")
                for y in lista_temp4:
                    print (y)
            else:
                print("O CPF informado não contem MACs a ele associado!")
        else:
            print("O CPF informado não está cadastrado!")
    else:
        print("CPF Inválido!")
###################################################################################################################
###################################################################################################################
if opcao == 7: # g
        
        try:
            nome_arquivo = input('qual vai ser o nome do arquivo:')
            arquivo = open(nome_arquivo, 'r')
            arquivo.close
            print('esse arquivo ja exite!!!')
            #decisao = input('esse arquivo ja esta exite deseja apagar tudo oque tem nele?\n' +
            #      '1 - sim\n' +
            #      '2 - nao\n')
            #if decisao == 1:
            #    fd = open (arquivo, "w")
        except FileNotFoundError:
            arquivo = open(nome_arquivo, "w")
            for a in tabela_cpf_mac.keys:
                arquivo.write( a + '_' + str(tabela_cpf_mac[a]) + ' ' +'\n')
            arquivo.close()
        except:
            print('houve algum erro tente novamente')
###################################################################################################################
###################################################################################################################
if opcao == 8: # h
    try:
        fd = open(input(''),'r')
        ##### TIRA OS ESPACOS #####
        arquivo = (fd.read()).split()
        for dados in arquivo:
        ##### TIRA OS OS COLCHETES E A VIRGULA DA LISTA DE MACS #####
            organizar += [dados.replace('[','').replace(']','').replace(',',' ').split('_')]
        for a in organizar:
            ##### EXIBE OS DADOS #####
            print(f'CPF:{a[0]} MAC:{a[1]}')
        fd.close() 
    except FileNotFoundError:
        print('esse arquivo nao existe!!!')
    except:
        print('houve algum erro tente novamente')
###################################################################################################################

# print(tabela_cpf_mac) # testes



################################################
'''
import json
d = json.loads(texto)     # Carrega banco de dados
t = json.dumps(d)         #Converte dicionário em texto

'''
################################################
