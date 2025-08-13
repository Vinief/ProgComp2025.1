passagem_interia = float(input('quanto é a passagem:')) 
passagem_meia = passagem_interia/2
diaria = int(input('quantas passagens voce usa por dia:'))
semanal = int(input('quantas vezes por semana:'))
passagem_disponivel = float(input('passagem disponivel:'))

dados = {}

##### quanto eh gasto em um dia #####

def gasto_diario (diaria):
    if diaria > 0:
        gasto_diario =  passagem_interia*diaria
        dados['diario'] = {'inteira':gasto_diario , 'meia' :gasto_diario/2}

        return gasto_diario
    else:
        resposta = 'digite um numero positivo'
        return resposta

gasto_diario(diaria)

print(dados)
##### quanto eh gasto na semana #####

def gasto_semanal (semana):
    if 7 > semana > 0 and gasto_diario(diaria) > 0:
        custo_semanal = gasto_diario(diaria)*semana
        dados['semanal'] = {'inteira':custo_semanal , 'meia' :custo_semanal/2}
        return custo_semanal
    else:
        resposta = 'digite um numero positivo:'
        return resposta        

##### para quantas semanas suas passagens duram #####
def passagem_semanal ():
    passagem_semana = passagem_disponivel//gasto_semanal(semanal)
    return passagem_semana

def passagem_diaria ():
    passagem_diaria = passagem_disponivel//gasto_diario(diaria)
    return passagem_diaria

def passagem_total():
    total = passagem_disponivel/passagem_interia
    return total
print(passagem_total())

print(f'{'interia':^15s}| {'meia':^}\n'+
      f'{f'diaria:':^}' + f' {passagem_diaria()}\n'+
      f'{f'semanal:':^}'+ f' {passagem_semanal()}\n')
