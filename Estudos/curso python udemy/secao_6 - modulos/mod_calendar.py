import calendar

ano = 2014
mes = 5  # 1 à 12
dia = 31  # 1 à 31

'''< ANOS BISSEXTOS >'''

# leapdays(x, y) retorna a quantidade de anos bissextos entre
# os dois valores fornecidos
print('O número de anos bissextos entre 1950 e 2021 é de: ', end='')
print(calendar.leapdays(1950, 2021))

# isleap() retorna true se o ano é bissexto
if (calendar.isleap(ano)):
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} NÃO é bissexto')


# Calendario apenas de um referido mês do ano:
print(calendar.month(ano, mes))

# Caledário do ano completo
# ano pode ser digitado sem utilização de variável.
print(calendar.calendar(ano))

calendar.prcal(ano, 2, 1, 6)
# prcal() é outra função para printar o calendário
# mas sem a necessidade de utilizar o print.
