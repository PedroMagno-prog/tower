from scipy.interpolate import lagrange
from core.funcoes.cadastro_db import carregar_dados_monstros
from random import choice, choices
from core.funcoes.util import convert_dificuldade, listar_monstros_por_familia


"""
            Andar 1
C: 80 -- I: 15 -- R: 4 -- E: 0.9 -- L: 0.1
            Andar 25
C: 70 -- I: 20 -- R: 8 -- E: 1.5 -- L: 0.5
            Andar 50
C: 55 -- I: 30 -- R: 10 -- E: 4 -- L: 1
            Andar 75
C: 35 -- I: 20 -- R: 25 -- E: 15 -- L: 5
            Andar 100
C: 5 -- I: 10 -- R: 40 -- E: 30 -- L: 15
"""
ANDARES =        [1,   25,  50, 75, 100]
PESOS = {"Comum":[80,  70,  55, 35, 5],
       "Incomum":[15,  20,  30, 20, 10],
          "Raro":[4,   8,   10, 25, 40],
        "Épico": [0.9, 1.5, 4,  15, 30],
     "Lendário": [0.1, 0.5, 1,  5,  15]}



print("="*56)
# index: [0] = Andar 1; [1] = Andar 25; [2] = Andar 50; [3] = Andar 75; [4] = Andar 100

"""
DIFICULDADE = inversamente proporcional ao peso da raridade COMUM

Dif = 0% ; peso_comum = 100%
Dif = 50% ; peso_comum = 50%
Dif = 100% ; peso_comum = 0% 
"""

def rng_rarity(andar:int, dificuldade:int) -> dict:

    rng_polys = {}    # dicionário, com a função 'poly' pra cada raridade
    pesos_finais = {} # dicionário, com os pesos, pra cada raridade, do andar selecionado

    for r in PESOS:
        rng_polys[r] = lagrange(ANDARES, PESOS[r])
    for r in rng_polys:
        p = rng_polys[r](andar)
        if r == "Comum":
            pesos_finais[r] = p - p*(dificuldade/100)
        else:
            pesos_finais[r] = p

    return pesos_finais

def abrir_bau(andar:int, n_players:int) -> list:
    try:
        dificuldade = input("Qual a dificuldade do encontro que acabaram de ter?\n"
                        "   digite: facil, normal, dificil, letal ou impossivel: ")
        dificuldade = convert_dificuldade(dificuldade)
    except:
        dificuldade = 0

    pesos = rng_rarity(andar, dificuldade)
    raridades = list(pesos.keys())
    pesos = list(pesos.values())

    return list((choices(raridades, weights=pesos)[0]) for _ in range(n_players))

def gerar_encontro(nivel_party):
    dificuldade = 0
    while dificuldade == 0:
        try:
            dificuldade = input("Qual a dificuldade do encontro que acabaram de ter?\n"
                                "   digite: facil, normal, dificil, letal ou impossivel: ")
            dificuldade = convert_dificuldade(dificuldade)
        except:
            dificuldade = 0
    nivel_monstros_max = (dificuldade/100) * nivel_party
    print(f"O nível total dos monstros será: {nivel_monstros_max}")

    familia = input(""
        "\n==> Bandido: Humanos fora da lei."
        "\n==> Goblin: Goblins, Bugbears e Hobgoblins. "
        "\n==> Kobold: Kobolds."
        "\n==> Morto-Vivo: Esqueletos, Zumbis, Múmias, Vampiros, Cavaleiros da Morte, etc."
        "\n==> Homem-Cobra: Snakemen."
        "\n==> Troglodita: Troglodytes."
        "\n==> Planta: Monstros vegetais (Seedlings, Treants)."
        "\n==> Fada: Criaturas feéricas (Sprites, Gremlins, Mav)."
        "\n==> Infernal: Demônios e diabos (Fiends)."
        "\n==> Fera: Animais (Lobos, Raptors, Morcegos) e criaturas bestiais."
        "\n==> Cultista: Humanos fanáticos."
        "\n==> Gnoll: Gnolls."
        "\n==> Limo: Oozes e Gelatinas."
        "\n==> Dragão: Drakes e Dragões."
        "\n==> Aranha: Aranhas gigantes e ettercaps."
        "\n==> Monstruosidade: Criaturas híbridas ou não-naturais (Mimicos, Grifos, Quimeras, Aberrações)."
        "\n==> Constructo: Máquinas de mana (Scions, Hulks, Titans)"
        "\n==> Humanoide: NPCs gerais (Druidas, Magos)."
        "\n==> Homem-Lagarto: Lizardfolk."
        "\n==> Orc: Orcs."
        "\n==> Gigante: Gigantes, Trolls e Ogros."
        "\n==> Elfo Negro: Drow e Driders."
        "\n==> Aberração: Criaturas alienígenas ou psíquicas (Cloakers, Ul'vek, Dravok)."
        "\n\nQual família de monstros vai compôr o encontro? Ou não escreva nada para usar todos: ")

    lista_monstros = carregar_dados_monstros(True)
    lista_monstros_final = listar_monstros_por_familia(lista_monstros, familia)

    soma_nivel_monstros = 0
    encontro = list()

    while soma_nivel_monstros < nivel_monstros_max:
        monstro = choice(lista_monstros_final)
        if monstro.nivel+soma_nivel_monstros > nivel_monstros_max:
            continue
        encontro.append(monstro)
        soma_nivel_monstros += monstro.nivel
    for m in encontro:
        print(m)

    pass

# print(abrir_bau(78, 4))
# gerar_encontro(20)