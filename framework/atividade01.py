from csv import DictReader
#pacote csv dentro dele tem uma classe chamada DictReader
import json
#importo o pacote json que ajuda a converter

# Atividade 1
# Criar um script que converte um arquivo .CSV com cabeçalho para um arquivo JSON.

#primeiro passo é ler o arquivo csv
def ler_arquivo_csv():
    # Open(quem,como)
    # quem = caminho + nome do arquivo
    # como: 'r'leR, 'w' escreWer
    # with conexao com o banco de dados e fecha dps do bloco
    #open funcao nativa no python p/abrir arquivos com o caminho
    with open("musicas.csv", "r") as arq_csv:
        #DictReader lê e extrai cada linha do arquivo
        leitor_csv = DictReader(arq_csv)
        registros = [
            registro
            #para cada informacao da linha ele gera um dicionario onde add nessa lista
            for registro in leitor_csv
        ]
        print(registros)
        return registros

#pegar aas informacoes do csv que ja estao convertidas para uma estrutura do python uma lista de obj/dicionario e passar p um arquivo json 
def salvar_arquivos_json(registros):
    #cria/substitui o arquivo com as informacoes passada pra ele
    with open("saida.json", "w") as arq_json:
        #usei o pct json nativo do python p chamar a funcao dele Dump(dentro do pct json)
        #cujo papel é escrever/transformar uma lista de registros em arq json 
        json.dump(registros, arq_json)


def principal():
    registros = ler_arquivo_csv()
    salvar_arquivos_json(registros)


if __name__ == "__main__":
    principal()
