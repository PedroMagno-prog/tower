import json
import os
from core.models.models import Monstro, Loot
# --- Nosso "Database" em Memória ---

# Esses são os nomes dos arquivos que vamos usar
ARQUIVO_MONSTROS = "banco\monstros.json"
ARQUIVO_LOOTS = "banco\loots.json"

# Essas listas vão guardar os OBJETOS em memória enquanto o programa roda
lista_monstros = []
lista_loots = []

def salvar_dados():
    # Salva em arquivos JSON, as listas criadas durante a core
    print("Salvando dados...")

    dados_monstros = [monstro.__dict__ for monstro in lista_monstros]
    dados_loots = [loot.__dict__ for loot in lista_loots]

    with open(ARQUIVO_MONSTROS, 'w', encoding='utf-8') as f:
        json.dump(dados_monstros, f, indent=4, ensure_ascii=False)
    with open(ARQUIVO_LOOTS, 'w', encoding='utf-8') as f:
        json.dump(dados_loots, f, indent=4, ensure_ascii=False)

    print("Dados Salvos com sucesso!")
    pass


def carregar_dados():
    """Carrega os dados dos arquivos JSON para as listas em memória."""
    global lista_monstros, lista_loots

    # --- Carrega Monstros ---
    if os.path.exists(ARQUIVO_MONSTROS):
        with open(ARQUIVO_MONSTROS, 'r', encoding='utf-8') as f:
            # 1. Lê os dados crus (lista de dicionários)
            dados_monstros = json.load(f)
            # 2. Recria os objetos Monster a partir dos dicionários
            lista_monstros = [Monstro(**dados) for dados in dados_monstros]

    # --- Carrega Loots ---
    if os.path.exists(ARQUIVO_LOOTS):
        with open(ARQUIVO_LOOTS, 'r', encoding='utf-8') as f:
            dados_loots = json.load(f)
            # O **dados é um atalho para "desempacotar" o dicionário
            # É o mesmo que: Loot(nome=dados['nome'], raridade=dados['raridade'], ...)
            lista_loots = [Loot(**dados) for dados in dados_loots]

    print(f"Dados carregados: {len(lista_monstros)} monstros, {len(lista_loots)} loots.")

def cadastro_monstro():
    print("Vamos cadastrar alguns monstros! (digite 'nimble' no CAMPO nome para sair)")
    print("=" * 56)
    while True:
        try:
            nome = input("Qual o nome dele? --> ")
            if nome == 'nimble':
                print("Voltando ao menu... ")
                return
            tipo = input("É Normal(n) ou Lendário(l)? --> ")
            if tipo == "n":
                tipo = "Normal"
            elif tipo == "l":
                tipo = "Lendário"
            else:
                raise Exception
            nivel = float(input("Qual o nível dele? --> "))
            descricao = input("Descreva o monstro (opcional) \n-->")
            novo_monstro = Monstro(nome=nome, tipo=tipo, nivel=nivel, descricao=descricao)
            lista_monstros.append(novo_monstro)
            print(f"\nMonstro '{novo_monstro.nome}' foi cadastrado. Não esqueça de salvar!")
        except:
            print("Tente Novamente")
            continue

    pass

def cadastro_loot():
    print("Vamos cadastrar um pouco de LOOT!")
    print("=" * 56)
    while True:
        try:
            nome = input("Qual o nome do item? (digite 'nimble' para sair) --> ")
            if nome == 'nimble':
                print("Voltando ao menu... ")
                return
            raridade = input("É Comum(c), Incomum(i), Raro(r), Épico (e) ou Lendário(l)? --> ")
            if raridade == "c":
                raridade = "Comum"
            elif raridade== "i":
                raridade = "Incomum"
            elif raridade== "r":
                raridade = "Raro"
            elif raridade== "e":
                raridade = "Épico"
            elif raridade== "l":
                raridade = "Lendário"
            else:
                raise Exception
            valor = int(input("Qual o valor do item em Peças de Ouro? --> "))
            descricao = input("Descreva o monstro (opcional) \n-->")
            novo_loot = Loot(nome=nome, raridade=raridade, valor=valor, descricao=descricao)
            lista_loots.append(novo_loot)
            print(f"\nLoot '{novo_loot.nome}' foi cadastrado. Não esqueça de salvar!")
        except:
            print("Tente Novamente")
            continue

    pass


def ver_monstros():
    print("\n--- Lista de Monstros Cadastrados ---")
    if not lista_monstros:
        print("(Nenhum monstro cadastrado)")
        return

    # O __str__ que você definiu é usado aqui!
    for monstro in lista_monstros:
        print(f"- {monstro}")


def ver_loots():
    print("\n--- Lista de Loots Cadastrados ---")
    if not lista_loots:
        print("(Nenhum loot cadastrado)")
        return

    for loot in lista_loots:
        print(f"- {loot}")