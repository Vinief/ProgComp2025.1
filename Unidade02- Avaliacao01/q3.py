import random
           ##### LISTA DE PALAVRAS ACEITAS #####
palavras = ["ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"]

##### IMPEDE DUAS PALAVRAS IGUAIS NO JOGO #####

impedir_repiticao = palavras.copy()

##### CORES #####

PRETO = "\033[0;30m"
VERDE = '\033[0;32m'
PADRAO = '\033[0m'
AMARELO = '\033[1;33m'

##### PARAMETRO DE DESEMPENHO #####
desempenho = { 1:'IMPOSSIVEL' , 2:'NINJA' , 3:'IMPRESSIONATE' , 4:'INTERESSANTE' , 5:'PODE MELHORAR' , 6:'FOI POR POUCO', 7:'UFA'} 

segredos = [palavras[random.randint(0,len(palavras)-1)]]

impedir_repiticao.remove(segredos[0])

segredos += [palavras[random.randint(0,len(palavras)-1)]]

##### CRIA UMA COPIA PARA A VARIAVEL segredos PARA A COPARACAO #####
segredos_copia = segredos.copy()

tentativas = 0
nao_pertence = []

while tentativas < 7 and len(segredos_copia) != 0:
    ##### IMEPEDE A ENETRADA DE NUMEROS #####
    print(segredos[0],segredos[1])
    try:
        chute = input('dig:').upper()
        teste = int(chute)
        print('apenas letras sao validas') 
    except:
        letras = ''
        if len(chute) == 5 and chute in palavras:
            for segredo in segredos_copia:
                for pos_chute in range(len(chute)):
                    ##### VERIFICA SE A LETRA ESTA CERTA #####
                    if chute[pos_chute] == segredo[pos_chute]:
                        letras += VERDE + chute[pos_chute] + PADRAO
                    ##### VERIFICA SE A LETRA PERTENCE AS PALAVRAS SORTEADAS E SE ESTA NA POSICAO CERTA #####
                    if chute[pos_chute] != segredo[pos_chute] and chute[pos_chute] in segredo:       
                        letras += AMARELO + chute[pos_chute] + PADRAO
                    ##### VERIFICA SE A LETRA PERTENCE AS PALAVRAS SORTEADAS ##### 
                    if chute[pos_chute] not in segredo:
                        letras += PRETO + chute[pos_chute] + PADRAO
                    ##### SEPARA AS PALAVRAS SORTEADAS #####
                    if pos_chute == 4:
                        letras += '  '
                    ##### ARMAZENA AS LETRAS QUE NAO PERTENCEM A UMA LISTA #####
                    if chute[pos_chute] not in segredos[0] and chute[pos_chute] not in segredos[1] and chute[pos_chute] not in nao_pertence:
                        nao_pertence += chute[pos_chute]
            ##### EXIBE LETRAS QUE NAO PERTENCEM AS PALAVRAS E AS QUE VOCE ACERTOU #####
            print(f'essas letras nao pertencem as palavras {nao_pertence}') 
            print(letras)
            tentativas += 1
        ##### IMPEDE PALAVRAS MENORES OU MAIORES QUE O PERMETIDO ##### 
        if len(chute) != 5:
            print('este jogo sustenta apenas palavras com 5 letras')
        ##### IMEPDE PALAVRAS QUE NAO SAO VALIDAS #####
        if chute not in palavras and len(chute) == 5:
            print('essa palavra não é valida')
        ##### DEIXA DE EXIBIR PALAVRAS QUE JA FORAM DESCOBERTAS ####
        if chute in segredos_copia:
            segredos_copia.remove(chute)    
##### EXIBE O SEU DESEMPENHO NO JOGO #####
if len(segredos) == 0:
    print(desempenho[tentativas])
##### EXIBE AS PALAVRAS SOTEADAS CASO VOCE NAO ACERTE AS PALAVRAS #####
else:
    print(f'palavras: {segredos[0]}, {segredos[1]}')
