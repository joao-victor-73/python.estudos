'''import datetime  # importar a biblioteca

# Pegar a data completa de hoje: 2023-04-16
print(datetime.date.today())

# Pegar apenas o ano: 2023
print(datetime.date.today().year)

# Pegar apenas o mês: 4
print(datetime.date.today().month)

# Pegar apenas o dia: 16
print(datetime.date.today().day)

'''
from datetime import datetime, timedelta
# Importando da biblioteca a função datetime

# Um timedelta é a diferença entre duas datas. Você pode pegar
# e fazer uma subtração ou adição com as datas, ou então você pode
# criar o seu próprio timedelta para você adicionar dias, horas,
# minutos, segundos, etc.

fmt = '%d/%m/%Y %H:%M:%S'  # Formato que aparecera as datas

data_inicio = datetime.strptime('22/05/2022 07:30:14', fmt)
data_fim = datetime.strptime('02/12/2020 20:37:14', fmt)

# Pegando a diferença entre duas datas e isso não resultará
# em uma nova data, apenas em algo chamado timedelta:
print(data_fim - data_inicio)


print("----------------------")
# < Utilizando o método now() >

# Horas e datas atuais: 2023-04-16 15:26:09
print(datetime.now())  # A - M - D  H-M-S
