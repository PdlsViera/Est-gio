import json

# isso normalmente seria carregado do arquivo, aqui está para facilitar
dados_json = '''
{
  "faturamento": [
    {"dia": 1, "valor": 200},
    {"dia": 2, "valor": 0},
    {"dia": 3, "valor": 100},
    {"dia": 4, "valor": 150},
    {"dia": 5, "valor": 0},
    {"dia": 6, "valor": 300},
    {"dia": 7, "valor": 0},
    {"dia": 8, "valor": 180},
    {"dia": 9, "valor": 250},
    {"dia": 10, "valor": 0}
  ]
}
'''

dados = json.loads(dados_json)
faturamentos = [dia['valor'] for dia in dados['faturamento'] if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

menor_faturamento, maior_faturamento, dias_acima_da_media

print("Menor faturamento: " ,menor_faturamento)
print("Maior faturamento: ", maior_faturamento)
print("Dias acima da média: " , dias_acima_da_media)