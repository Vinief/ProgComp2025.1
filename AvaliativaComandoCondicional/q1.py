print('esse programa soma os algorismos de um número até 4 algarismos')
n = int(input('digite seu número:'))

#verefica se os núemros são maiores que 9999 
if n <= 9999  :
    #separa o algarismo dos milhares
    a = n //1000 
    #separa o algarismo das centena
    b = (n - a * 1000)//100
    #separa o algarismo das dezena
    c = (n - (a *1000 + b *100)) //10
    #separa o algarismo da unidade
    d = (n - (a *1000 + b *100 + c * 10))
    #soma todos os algarismos
    e = a + b + c + d
#exibe a soma dos algarismos
print('essa é a soma dos algarismos:',e)
