passagem_interia = float(input('quanto é a passagem:')) 
passagem_meia = passagem_interia/2
diaria = int(input('quantas passagens voce usa por dia:'))
semanal = int(input('quantas vezes por semana:'))
passagem_disponivel = float(input('passagem disponivel:'))


def passagem_diaria (diaria):
    if diaria > 0:
        gasto_diario =  passagem_interia*diaria
        return gasto_diario
    else:
        resposta = 'digite um numero positivo'
        return resposta

def passagem_semanal (semana):
    if 7 > semana > 0 and passagem_diaria(diaria) > 0:
        gasto_semanal = passagem_diaria(diaria)*semana
        return gasto_semanal
    else:
        resposta = 'digite um numero positivo:'
        return resposta        



print(f'dias: {round(passagem_diaria(diaria)//passagem_disponivel)}' /  
        f'semanas:{round(passagem_semanal(semanal)//passagem_disponivel)}' /
        f'total: semana: {round(passagem_semanal(semanal))} dia:{round((passagem_semanal%semanal)//diaria)}'
        f'(meia)dias: {round(passagem_diaria(diaria)//passagem_disponivel)}' /  
        f'(meia)semanas:{round(passagem_semanal(semanal)//passagem_disponivel)}' /
        f'(meia)total: semana:{round(passagem_semanal(semanal))} dia:{round((passagem_semanal()%semanal)//diaria)}')
