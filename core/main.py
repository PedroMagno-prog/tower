"""
A ideia aqui é

se baseando no nível do personagem

"""
import random
from collections import Counter
from models.models import Monstro, Loot
from funcoes.util import *
from funcoes.dice_roller import *
from funcoes.cadastro import (
    carregar_dados,
    salvar_dados,
    cadastro_monstro,
    cadastro_loot,
    ver_monstros,
    ver_loots
)

valor_em_po = {} # tabelar raridade com um valor X em PO

def criar_monstro():

    tipo_monstro = input("Deseja criar um monstro Normal (n) ou Lendário (l)? --> ")
    if tipo_monstro == "l":
        # Em desenvolvimento
        pass
    else:
        print("Deseja ")
        pass
    print("Deseja criar um monstro em que nível?")
    # criar_monstro()

    pass

def gerar_encontro(nivel_party):
    dificuldade = int(input("Qual dificuldade deve ser o encontro? --> "))

    # level total dos monstros deve ser a soma dos niveis dos players

    pass

def abrir_bau(andar):
    dificuldade = int(input("Qual dificuldade foi a sala ddo baú? --> "))
    pass


def menu(nivel_party, andar):
    # menu que processa uma única vez. No Main temos o loop infinito
    print("=" * 56,
          "\nEscolha uma opção:"
          "\n(1) Cadastrar Monstro"
          "\n(2) Cadastrar Loot"
          "\n(3) Ver Monstros"
          "\n(4) Ver Loot"
          "\n(5) Criar um Monstro"
          "\n(6) Gerar um Encontro"
          "\n(7) Abrir um Baú"
          "\n\n(10) SALVAR"
          "\nDigite qualquer outro valor pra sair para sair"
          )
    print("=" * 56)
    opcao = input("--> ")
    # --- O "Dispatch Table" (Dicionário de Opções) ---
    # Usamos 'lambda' para "atrasar" a execução das funções
    # e para conseguir passar os argumentos corretos (nivel_party, andar).
    opcoes = {
        '1': lambda: cadastro_monstro(),
        '2': lambda: cadastro_loot(),
        '3': lambda: ver_monstros(),
        '4': lambda: ver_loots(),
        '5': lambda: criar_monstro(),
        '6': lambda: gerar_encontro(nivel_party),
        '7': lambda: abrir_bau(andar),
        '10': lambda: salvar_dados()
    }
    # 1. Usamos .get() para buscar a função no dicionário.
    # 2. Se a 'opcao' (ex: '1') existe, 'funcao_a_executar'
    #    recebe o lambda (ex: lambda: criar_monstro()).
    # 3. Se a 'opcao' (ex: '5') não existe, 'funcao_a_executar' recebe 'None'.
    funcao_a_executar = opcoes.get(opcao)

    if funcao_a_executar:
        funcao_a_executar()  # Executa o lambda (que por sua vez chama a função real)
        return True  # Retorna True para continuar no loop 'while opcao_menu:'
    else:
        print("\nVoltando ao setup inicial...")
        return False  # Retorna False para quebrar o loop 'while opcao_menu:'
    pass

def main():
    carregar_dados()
    while True:
        print("="*20 + "Bem-Vindo Criador_Dev!" + "="*20)
        print()
        print("Antes de começarmos, precisamos definir alguns valores... ")
        n_jogadores = int(input("Quantos jogadores estão jogando? --> "))
        nivel = int(input("Em que nível, individualmente, eles estão? (Exe: todos estão no nível 3) --> "))
        nivel_party = calcular_nivel_party(nivel, n_jogadores)
        print("Nível da Party é " + str(nivel_party))
        andar = int(input("Em qual andar a party se encontra? --> "))


        opcao_menu = True
        while opcao_menu:
            opcao_menu = menu(nivel_party, andar)

    print("Programa finalizado")
    pass


# --- 1. CONFIGURAÇÕES GERAIS DO SISTEMA DE LOOT ---
# Ajuste estes valores para balancear seu jogo

# Os nomes das raridades. O "Comum" é especial.
COMMON_RARITY_NAME = "Comum"

# Os "extremos" do seu jogo
MIN_FLOOR = 1
MAX_FLOOR = 100

# 🧠 ÂNCORA A: Pesos de loot base no Andar 1 (Início do Jogo)
WEIGHTS_FLOOR_1 = {
    "Comum": 80,
    "Incomum": 15,
    "Raro": 4.0,
    "Épico": 0.9,
    "Lendário": 0.1
}

# 🧠 ÂNCORA B: Pesos de loot base no Andar 100 (Fim de Jogo)
# Note como "Comum" aqui é mais raro que "Incomum"
WEIGHTS_FLOOR_100 = {
    "Comum": 10,
    "Incomum": 20,
    "Raro": 40,
    "Épico": 20,
    "Lendário": 10
}

# ⚙️ MODIFICADORES DE DIFICULDADE (0% a 100%)
# A penalidade máxima que "Comum" pode sofrer com 100% de dificuldade
# (0.5 = 50% de redução no peso)
# No caso alterei pra 1.0 pra ser uma redução TOTAL na dificuldade 100. Não há itens comuns nas
MAX_COMMON_PENALTY = 0.5

# O bônus máximo que os itens raros podem receber com 100% de dificuldade
# (1.0 = 100% de bônus, ou seja, dobra o peso)
MAX_RARE_BONUS = 1.0


def lerp(a: float, b: float, t: float) -> float:
    """Interpolação Linear: Calcula um ponto entre 'a' e 'b' baseado em 't'."""
    return a + (b - a) * t
# 80 + (10-80) * 50

def calculate_base_weights(andar: int) -> dict:
    """
    PASSO 1: Calcula os pesos de loot base para o andar atual
    usando interpolação linear entre o Andar 1 e o Andar 100.
    """
    # Garante que o andar atual esteja dentro dos limites
    andar = max(MIN_FLOOR, min(andar, MAX_FLOOR))

    # Calcula o andar do jogador (0.0 para Andar 1, 1.0 para Andar 100)
    andar = (andar - MIN_FLOOR) / (MAX_FLOOR - MIN_FLOOR)

    base_weights = {}

    # Itera por todas as raridades definidas na Âncora A
    for rarity in WEIGHTS_FLOOR_1.keys():
        weight_start = WEIGHTS_FLOOR_1[rarity]
        weight_end = WEIGHTS_FLOOR_100[rarity]

        # Calcula o peso interpolado
        calculated_weight = lerp(weight_start, weight_end, andar)
        base_weights[rarity] = calculated_weight

    return base_weights


def apply_difficulty_modifier(base_weights: dict, difficulty_percent: float) -> dict:
    """
    PASSO 2: Aplica o modificador de dificuldade aos pesos base.
    Diminui "Comum" e aumenta todos os outros.
    """
    # Converte a dificuldade (ex: 80%) para um fator (ex: 0.8)
    difficulty_mod = max(0.0, min(difficulty_percent / 100.0, 1.0))

    final_weights = {}
    for rarity, base_weight in base_weights.items():
        if rarity == COMMON_RARITY_NAME:
            # Aplica a penalidade ao item comum
            penalty_factor = MAX_COMMON_PENALTY * difficulty_mod
            final_weight = base_weight * (1.0 - penalty_factor)
        else:
            # Aplica o bônus a todas as outras raridades
            bonus_factor = MAX_RARE_BONUS * difficulty_mod
            final_weight = base_weight * (1.0 + bonus_factor)

        # Garante que o peso nunca seja zero ou negativo
        final_weights[rarity] = max(0.01, final_weight)

    return final_weights


def get_loot_rarity(final_weights: dict) -> str:
    """
    PASSO 3: Realiza a rolagem de RNG com base nos pesos finais.
    Retorna o nome da raridade sorteada.
    """
    # Extrai as raridades e seus pesos correspondentes
    rarities = list(final_weights.keys())
    weights = list(final_weights.values())

    # random.choices faz a seleção ponderada para nós
    # Retorna uma lista de 1 item, então pegamos o [0]
    chosen_rarity = random.choices(rarities, weights=weights, k=1)[0]
    return chosen_rarity


# --- 3. EXECUÇÃO E SIMULAÇÃO ---

def main_gem():
    """Função principal para demonstrar e testar o sistema."""

    # --- PARÂMETROS DA SIMULAÇÃO ---
    NUM_ROLLS = 50000  # Simular 50.000 aberturas de baú
    # -------------------------------

    andar = int(input("Qual andar os jogadores se encontram? --> "))
    dificuldade = int(input("Qual foi a dificuldade? --> "))

    print(f"--- 🎲 SIMULAÇÃO DE LOOT ---")
    print(f"Andar: {andar} | Dificuldade: {dificuldade}%\n")

    # PASSO 1: Calcular os pesos base apenas para o Andar
    base_weights = calculate_base_weights(andar)
    print("--- Pesos Base (só pelo Andar) ---")
    for r, w in base_weights.items():
        print(f"{r:>9}: {w:.2f}")
    print("-" * 35)

    # PASSO 2: Aplicar o modificador de dificuldade
    final_weights = apply_difficulty_modifier(base_weights, dificuldade)
    print(f"--- Pesos Finais (Andar + Dificuldade {dificuldade}%) ---")
    for r, w in final_weights.items():
        print(f"{r:>9}: {w:.2f}")
    print("-" * 35)

    # PASSO 3: Simular a abertura de vários baús
    print(f"📈 Simulando {NUM_ROLLS} aberturas de baú...")
    loot_results = []
    for _ in range(NUM_ROLLS):
        rarity = get_loot_rarity(final_weights)
        loot_results.append(rarity)

    # Contar e exibir os resultados
    loot_counts = Counter(loot_results)

    # Ordenar pela ordem de raridade original para melhor visualização
    print("\n--- RESULTADO DA SIMULAÇÃO ---")
    total_rolls = sum(loot_counts.values())

    for rarity in WEIGHTS_FLOOR_1.keys():
        count = loot_counts[rarity]
        percentage = (count / total_rolls) * 100
        print(f"{rarity:>9}: {count} rolagens ({percentage:.2f}%)")


if __name__ == "__main__":
    main()
    #main_gem()
