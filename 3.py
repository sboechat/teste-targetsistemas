# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
import json

def calcular_faturamento(faturamento: list):
    menor = faturamento[0]["valor"]
    maior = faturamento[0]["valor"]
    media = 0
    dias_uteis = 0
    for valor in faturamento:
        valor = valor["valor"]
        if valor != 0:
            if valor < menor:
                menor = valor
            if valor > maior:
                maior = valor
            dias_uteis+=1
            media += valor
    
    media = media / dias_uteis
    acima_media = 0
    for valor in faturamento:
        valor = valor["valor"]
        if valor > media:
            acima_media+=1
    
    print(f'''
            Menor valor: {menor}
            Maior valor: {maior}
            Dias com faturamento superior à média mensal: {acima_media}
          ''')
    
def main():
    with open("./files/dados.json") as file:
        faturamento = json.load(file)
    calcular_faturamento(faturamento)

if __name__ == '__main__':
    main()