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

##### CORES

PRETO = "\033[0;30m"
VERDE = '\033[0;32m'
PADRAO = '\033[0m'
AMARELO = '\033[1;33m'

letras = ''

desempenho = { 1:'IMPOSSIVEL' , 2:'NINJA' , 3:'IMPRESSIONATE' , 4:'INTERESSANTE' , 5:'PODE MELHORAR' , 6:'FOI POR POUCO', 7:'UFA'} 

segredos = [palavras[random.randint(0,len(palavras)-1)]]

impedir_repiticao.remove(segredos[0])

segredos += [palavras[random.randint(0,len(palavras)-1)]]
segredos_copia = segredos.copy()

tentativas = 0
nao_pertence = []

print(segredos)

while tentativas < 7 and len(segredos_copia) != 0:
    try:
        chute = input('dig:').upper()
        teste = int(chute)
        print('apenas letras sao validas') 
    except:
        letras = ''
        if len(chute) == 5 and chute in palavras:
            for segredo in segredos:
                for pos_chute in range(len(chute)):
                
                    if chute[pos_chute] == segredo[pos_chute]:
                        letras += VERDE + chute[pos_chute] + PADRAO
                
                    if chute[pos_chute] != segredo[pos_chute] and chute[pos_chute] in segredo:       
                        letras += AMARELO + chute[pos_chute] + PADRAO
                    
                    if chute[pos_chute] not in segredo:
                        letras += PRETO + chute[pos_chute] + PADRAO
                        
                    if pos_chute == 4:
                        letras += '  '
                    
                    if chute[pos_chute] not in segredos[0] and chute[pos_chute] not in segredos[1] and chute[pos_chute] not in nao_pertence:
                        nao_pertence += chute[pos_chute]
                
            print(f'essas letras nao pertencem as palavras {nao_pertence}') 
            print(letras)
            tentativas += 1

        if len(chute) != 5:
            print('este jogo sustenta apenas palavras com 5 letras')
        
        if chute not in palavras and len(chute) == 5:
            print('essa palavra não é valida')
        
        if chute in segredos:
            segredos_copia.remove(chute)      
    
if len(segredos) == 0:
    print(desempenho[tentativas])
