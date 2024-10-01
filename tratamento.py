import pandas as pd
import json

caminho_arquivo= r"C:/Users/hp/Documents/testes/dados_json.json"

# Função para ler o arquivo JSON usando Pandas
def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return pd.DataFrame(dados)

# Função para calcular os resultados a partir dos dados
def calcular_faturamento(df):
    # Filtrar os dias com faturamento (remover valores iguais a 0)
    faturamento_valido = df[df['valor'] > 0]

    # Calcular o menor e o maior valor de faturamento
    menor_faturamento = faturamento_valido['valor'].min()
    maior_faturamento = faturamento_valido['valor'].max()

    # Calcular a média mensal
    media_mensal = faturamento_valido['valor'].mean()

    # Contar o número de dias em que o faturamento foi superior à média
    dias_acima_da_media = faturamento_valido[faturamento_valido['valor'] > media_mensal].shape[0]

    return menor_faturamento, maior_faturamento, media_mensal, dias_acima_da_media

# Caminho do arquivo JSON
caminho_arquivo = r'C:/Users/hp/Documents/testes/dados_json.json'

# Ler os dados do arquivo JSON
df = ler_arquivo_json(caminho_arquivo)

# Calcular os resultados
menor_faturamento, maior_faturamento, media_mensal, dias_acima_da_media = calcular_faturamento(df)

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: {maior_faturamento:.2f}")
print(f"Média mensal de faturamento: {media_mensal:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")