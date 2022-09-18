from typing import Optional
import pydantic
import fastapi

# SISTEMA DE CADASTRO DE MUSICAS PARA UMA PLAYLIST

# ======================
# Persistencia / Repositorio
# ======================

MEMORIA_MUSICAS = []


def persistencia_musica_salvar(nova_musica):
    codigo_nova_musica = len(MEMORIA_MUSICAS) + 1
    # Ajuste da persistencia
    nova_musica["codigo"] = codigo_nova_musica
    # Salva na persistencia/repositorio
    MEMORIA_MUSICAS.append(nova_musica)
    return nova_musica


def persistencia_musica_pesquisar_todas():
    lista_musicas = list(MEMORIA_MUSICAS)
    return lista_musicas


def persistencia_pesquisar_pelo_codigo(codigo):
    musica_procurada = None
    for musica in MEMORIA_MUSICAS:
        if musica["codigo"] == codigo:
            musica_procurada = musica
            break
    return musica_procurada


def persistencia_deletar_pelo_codigo(codigo):
    del_musica = None
    for musica in MEMORIA_MUSICAS:
        if musica["codigo"] == codigo:
            del_musica = MEMORIA_MUSICAS.remove(musica)
            break
    return del_musica


# ======================
# Regras / Casos de Uso / BO(Business Object)
# ======================


def regras_musica_cadastrar(nova_musica):
    # TODO  Validar a nova musica
    # regras_musica_validar_nova_musica(nova_musica)
    nova_musica = persistencia_musica_salvar(nova_musica)
    return nova_musica


def regras_musica_pesquisar_todas():
    return persistencia_musica_pesquisar_todas()


def regras_musica_pesquisar_pelo_codigo(codigo):
    return persistencia_pesquisar_pelo_codigo(codigo)


def regras_musicas_deletar_pelo_codigo(codigo):
    return persistencia_deletar_pelo_codigo(codigo)

    # ======================
    # API Rest / Controlador
    # ======================

    # pydanctic estruturacao orientada a objetos para definir oq entra no programa
    # variavel global com o papel de gerenciar,determinar, passar as instrucoes para como a api rest na parte de atendimento ira trabalhar
app = fastapi.FastAPI()

# ------ rotas / caminhos

# ** Rota raiz **


@app.get("/")
def rota_raiz():
    return {
        "ok": True,
        "versão": "Fase 1"
    }


@app.get("/musicas")
def rota_musica_pesquisar_todas():
    return regras_musica_pesquisar_todas()


@app.get("/musicas/{codigo}")
def rota_musica_pesquisar_pelo_codigo(codigo: int):
    print("Consulta pelo código: ", codigo)
    return regras_musica_pesquisar_pelo_codigo(codigo)


class NovaMusica(pydantic.BaseModel):
    nome: str
    artista: str
    tempo: Optional[int]


@app.post("/musicas")
def rota_musica_cadastrar(nova_musica: NovaMusica):
    print("Registrando uma nova musica: ", nova_musica.dict())
    nova_musica = regras_musica_cadastrar(nova_musica.dict())
    return nova_musica

# no mesmo caminho posso ter metodos diferentes
# associando o metodo get a este caminho e qdo bater na requisicao vai chamar esta funcao


@app.put("/musicas/{codigo}")
def rota_musica_atualizar(codigo: int):
    print("Atualiza pelo codigo: ", codigo)


@app.delete("/musicas")
def rota_deleta_musica_pelo_codigo(codigo: int):
    ...
