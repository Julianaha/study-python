import requests

# CRIAÇÃO DE UM SCRIPT QUE LÊ DE UMA API O VALOR DA COTAÇÃO DO DÓLAR DE HOJE


def ler_cotacao_dolar():
    url = "https://economia.awesomeapi.com.br:443/json/last/USD-BRL"
    resposta_web = requests.get(url)
    # padrao para consultar api verbo get

    if not resposta_web.ok:
        return None
    # se der errado retorna nada

    # caso contrario retorna um json
    resposta_json = resposta_web.json()
    return resposta_json


def obter_valor_dolar(cotacao_web):
    valor_dolar = cotacao_web["USDBRL"]["bid"]
    return valor_dolar


def principal():
    cotacao_web = ler_cotacao_dolar()
    valor_dolar = obter_valor_dolar(cotacao_web)
    print("Valor do dolar ", valor_dolar)


if __name__ == "__main__":
    principal()
