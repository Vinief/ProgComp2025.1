print('Até duas horas: R$ 8,00/hora ou fração;') 
print('Entre três e quatro horas: R$ 5,00/hora ou fração;') 
print('Horas seguintes: R$ 3,00/hora ou fração.')
print('Depois de 12h, o custo passa a ser fixo: R$ 30,00')

periodo = int(input('quanto tempo você passou no estacinamento?(digite em minutos)'))/60
#transforma minutos em horas para ficar mais facil de escrever o código

#separa o valor a ser pago e explica ao usuário o motivo de estar pagando aquele valor
if periodo >= 0.1:
    taxa = 8
    pagamento = 'você deve pagar 8R$ pela 1hr'
    if periodo > 1:
        taxa = taxa + 8
        pagamento = pagamento + ', mais 8R$ pelas 2hrs'
    if periodo > 2:
        taxa = taxa + 5
        pagamento = pagamento + ', mais 5R$ pelas 3hrs'
    if periodo > 3:
        taxa = taxa + 5
        pagamento = pagamento + ', mais 5R$ pelas 4hrs'
    if periodo > 4:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 5hrs'
    if periodo > 5:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 6hrs'
    if periodo > 6:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 7hrs'
    if periodo > 7:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 8hrs'
    if periodo > 8:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 9hrs'
    if periodo > 9:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 10hrs'
    if periodo > 10:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 11hrs'
    if periodo > 11:
        taxa = taxa + 3
        pagamento = pagamento + ', mais 3R$ pelas 12hrs'
    if periodo > 12:
        taxa = 30 
        pagamento = 'você paga 30R$(valor fixo)'
        print(pagamento)
    else:
        periodo = round(periodo,1)
        print(pagamento,'dando um valor total de:',taxa,'por ter passado:',periodo,'hrs')
