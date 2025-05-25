print('esse programa calcula sua sua nota e fala sua situação academica')
N1 = int(input('qual é a sua nota do 1°bimestre?'))
N2 = int(input('qual é a sua nota do 2°bimestre?'))
MD = (2*N1 + 3*N2)/5
MD = round(MD,1)
#verica se você esta reprovado, aprovado ou se vai pra prova final
if MD >= 6:
    situação = 'aprovado'
if MD < 2:
    situação = 'reprovado'
if 6 > MD >= 2:
    #calula a nota da sua media final e fala se você esta reprovado o aprovado
    print('você esta na prova final')
    NAF = int(input('qual foi a sua nota na prova final?'))
    MDF = (MD + NAF)/2
    if MDF >= 6:
        situação = 'aprovado'
    else:
        situação = 'reprovado'
#exibe sua situação
print('você foi',situação)
