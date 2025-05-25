import random

numsort = random.randint(1,100)

tentativa1 = int(input('que número você quer chutar?'))
#verifica se você acetou o número 
if tentativa1 == numsort:
    print('parabens você acertou o número sorteado!!!',numsort)
#verifica se sua tentativa1 é maior ou menor que o número sorteado para reduzir o leque de possibilidades
if tentativa1 > numsort:
    print('suas opções são de',1,'até',tentativa1)
if tentativa1 < numsort:
    print('suas opções são de',tentativa1,'até',100)    

if tentativa1 != numsort:
    tentativa2 = int(input('que número você quer chutar?'))
    #verifica se você acetou o número
    if tentativa2 == numsort:
        print('parabens você acertou o número sorteado!!!',numsort)
    #verifica se sua tentativa1 e tentativa2 é maior ou menor que o número sorteado para reduzir o leque de possibilidades
    if tentativa2 > numsort and tentativa1 > numsort:
        print('suas opções são de',1,'até',tentativa2)
    if tentativa2 < numsort and tentativa1 < numsort:
        print('suas opções são de',tentativa2,'até',100)
    #cria um novo limite minimo ou máximo entre tentativa1 e tentativa2 e vice-versa 
    if tentativa2 < numsort < tentativa1:
        print('suas opções são de',tentativa2,'até',tentativa1)
    if tentativa2 > numsort > tentativa1:
        print('suas opções são de',tentativa1,'até',tentativa2)
    
    if tentativa2 != numsort:
        tentativa3 = int(input('que número você quer chutar?'))
        #verifica se você acetou o número
        if tentativa3 == numsort:
            print('parabens você acertou o número sorteado!!!',numsort)
        #verifica se sua tentativa1 e tentativa2 e tentativa 3 é maior ou menor que o número sorteado para reduzir o leque de possibilidades
        if tentativa3 > numsort and tentativa2 > numsort and tentativa1 > numsort:
            print('suas opções são de',1,'até',tentativa3)
        if tentativa3 < numsort and tentativa2 < numsort and tentativa1 < numsort:
            print('suas opções são de',tentativa3,'até',100)
        #verifica qual tentativa menor ou maior esta mais perto do número sorteado e define o limite minimo ou máximo apartir disso  
        if tentativa3 > numsort and tentativa1 < numsort and tentativa1 < tentativa2 and tentativa1 < tentativa3 and tentativa3 > tentativa2: 
            print('suas opções são de',tentativa1,'até',tentativa2)
        if tentativa3 > numsort and tentativa1 < numsort and tentativa1 < tentativa2 and tentativa1 < tentativa3 and tentativa3 < tentativa2: 
            print('suas opções são de',tentativa1,'até',tentativa3)
        if tentativa3 < numsort and tentativa1 > numsort and tentativa1 > tentativa2 and tentativa1 > tentativa3 and tentativa3 > tentativa2:
            print('suas opções são de',tentativa3,'até',tentativa1)
        if tentativa3 < numsort and tentativa1 > numsort and tentativa1 > tentativa2 and tentativa1 > tentativa3 and tentativa3 < tentativa2:
            print('suas opções são de',tentativa3,'até',tentativa2)
        if tentativa3 > numsort and tentativa2 < numsort and tentativa2 < tentativa1 and tentativa2 < tentativa3 and tentativa3 > tentativa1:
            print('suas opções são de',tentativa2,'até',tentativa1)
        if tentativa3 > numsort and tentativa2 < numsort and tentativa2 < tentativa1 and tentativa2 < tentativa3 and tentativa3 < tentativa1:
            print('suas opções são de',tentativa2,'até',tentativa3)
        if tentativa3 < numsort and tentativa2 > numsort and tentativa2 > tentativa1 and tentativa2 > tentativa3 and tentativa3 > tentativa1:
            print('suas opções são de',tentativa3,'até',tentativa2)
        if tentativa3 < numsort and tentativa2 > numsort and tentativa2 > tentativa1 and tentativa2 > tentativa3 and tentativa3 < tentativa1:
            print('suas opções são de',tentativa1,'até',tentativa2)
        if tentativa3 != numsort:
            tentativa4 = int(input('que número você quer chutar?'))
            #verifica se você acetou o número
            if tentativa4 == numsort:
                print('parabens você acertou o número sorteado!!!',numsort)
            else:
                print('você errou o número sorteado que foi é:',numsort)
