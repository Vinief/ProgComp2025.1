print ('esse calcula o tempo de um mês para o outro no mesmo ano (considerando que não é ano bissexto)')
di = int(input('diga o dia inicial:')) 
mi = int(input('diga o mês inicial:'))
df = int(input('diga o dia final:'))
mf = int(input('diga o mês final:'))
#caso os meses sejam maiores que 12 ou menores que 0
if mi > 12 or mf > 12 or mi < 0 or mf < 0:
    print('essa data não existe!!!')
    #caso os meses que tem 30 dias tenham mais que 30 dias
if (mi == 4 or mi == 7 or mi == 9 or mi == 11) and di > 30:
    print('essa data não existe!!!') 
if (mf == 4 or mf == 7 or mf == 9 or mf == 11) and df > 30:
    print('essa data não existe!!!')
#caso o usuário tente usar ano bissexto  
if mi == 2 and di >= 29:
    print('não é ano bissexto!!!')
if mf == 2 and df >= 29:
    print('não é ano bissexto!!!')

else:
    #transforma os dias normais em dias julianos
    if mi >= 1:
        di -= 31
        if di > 0:
            print('essa data não exite!!!')
    else:
        if mi >= 2:
            di += 28
        if mi >= 3:
            di += 31
        if mi >= 4:
            di += 30
        if mi >= 5:
            di += 31
        if mi >= 6:
            di += 30
        if mi >= 7:
            di += 31
        if mi >= 8:
            di += 31
        if mi >= 9:
            di += 30
        if mi >= 10:
            di += 31
        if mi >= 11:
            di += 30
        if mi >= 12:
            di += 31
#transforma os dias normais em dias julianos
if mf >= 1:
    df -= 31
    if df > 0:
        print('essa data não exite!!!')
    else:
        if mf >= 2:
            df += 28
        if mf >= 3:
            df += 31
        if mf >= 4:
            df += 30
        if mf >= 5:
            df += 31
        if mf >= 6:
            df += 30
        if mf >= 7:
            df += 31
        if mf >= 8:
            df += 31
        if mf >= 9:
            df += 30
        if mf >= 10:
            df += 31
        if mf >= 11:
            df += 30
        if mf >= 12:
            df += 31
#calcula os dias
dias = df - di - 1
if dias > 0:
    print ('esse é o total de dias:',dias)
