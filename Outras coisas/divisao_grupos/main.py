import pandas as pd
from datetime import datetime

# 1. Carregar a planilha
df = pd.read_excel('nomes_teste.xlsx')

# 2. Função para calcular a idade
def calcular_idade(data_nasc):
    hoje = datetime.today()
    return hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

# 3. Aplicar a função na coluna de data de nascimento
df['Idade'] = df['Data de Nascimento'].apply(pd.to_datetime).apply(calcular_idade)

# 4. Criar a coluna 'Grupo de Idade'
def definir_grupo(idade):
    if 14 == idade <= 15:
        return '14-15 anos'
    elif 16 <= idade <= 18:
        return '16-18 anos'
    else:
        return '18+ anos'

df['Grupo de Idade'] = df['Idade'].apply(definir_grupo)

# 5. Criar os subgrupos com no máximo 20 pessoas por categoria
grupos = {}
for categoria, grupo in df.groupby('Grupo de Idade'):
    subgrupos = [grupo.iloc[i:i+20] for i in range(0, len(grupo), 20)]
    for idx, sub in enumerate(subgrupos, 1):
        nome_aba = f'{categoria} - Grupo {idx}'
        grupos[nome_aba] = sub  # Armazena cada subgrupo como uma aba

# 6. Criar um arquivo Excel com várias planilhas
with pd.ExcelWriter('pessoas_agrupadas_por_idade.xlsx') as writer:
    for nome_aba, df_grupo in grupos.items():
        df_grupo.to_excel(writer, sheet_name=nome_aba, index=False)

print("Processo concluído! O arquivo 'pessoas_agrupadas.xlsx' foi gerado com abas separadas para cada grupo.")
