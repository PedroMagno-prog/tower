"""
TESTES com o GEM pra aprender a função
# Exemplo de uso com scipy
x = [1, 50, 100] # ANDAR
y = [80, 55, 10] # PESO definido (balanceamento)

# Cria a função do polinômio interpolador
poly_test = lagrange(x, y) # poly é LITERALMENTE a função?

# Estima um valor
print(poly_test(50)) # poly(90) = f(x)
print(poly_test)
"""
"""
Conclusão:
    poly tem uma precisão cirúrgica, mas tem margem de erro na casa sla 0.000 000 000 000 23

"""
import random
from collections import Counter

# --- 1. CONFIGURAÇÕES GERAIS DO SISTEMA DE LOOT ---
# Ajuste estes valores para balancear seu jogo

# Os nomes das raridades. O "Comum" é especial.
COMMON_RARITY_NAME = "Comum"

# Os "extremos" do seu jogo
MIN_FLOOR = 1
MID_FLOOR = 50
MAX_FLOOR = 100

# 🧠 ÂNCORA A: Pesos de loot base no Andar 1 (Início do Jogo)
WEIGHTS_FLOOR_1 = {
    "Comum": 80,
    "Incomum": 15,
    "Raro": 4,
    "Épico": 0.9,
    "Lendário": 0.1
}
# 🧠 ÂNCORA B: Pesos de loot base no Andar 50 (Mid-Game)
# Note como "Incomum" sobe rápido aqui, e entra em declínio depois
WEIGHTS_FLOOR_50 = {
    "Comum": 55,
    "Incomum": 30,
    "Raro": 10,
    "Épico": 4,
    "Lendário": 1
}

# 🧠 ÂNCORA C: Pesos de loot base no Andar 100 (Fim de Jogo)
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
    #Interpolação Linear: Calcula um ponto entre 'a' e 'b' baseado em 't'.
    return a + (b - a) * t
# Andar 50:
# 80 + (10-80) * 50
# 80 + (10-80) * 1


def calculate_base_weights(andar: int) -> dict:

     # PASSO 1: Calcula os pesos de loot base para o andar atual
     #usando interpolação linear entre o Andar 1 e o Andar 100.

    # Garante que o andar atual esteja dentro dos limites
    andar = max(MIN_FLOOR, min(andar, MAX_FLOOR))

    # Calcula o andar do jogador (0.0 para Andar 1, 1.0 para Andar 100)
    andar = (andar - MIN_FLOOR) / (MAX_FLOOR - MIN_FLOOR)
    print(f"andar: {andar}")
    base_weights = {}

    # Itera por todas as raridades definidas na Âncora A
    for rarity in WEIGHTS_FLOOR_1.keys():
        weight_start = WEIGHTS_FLOOR_1[rarity]
        weight_end = WEIGHTS_FLOOR_100[rarity]

        # Calcula o peso interpolado
        calculated_weight = lerp(weight_start, weight_end, andar)
        base_weights[rarity] = calculated_weight
    print(f"base_weights {base_weights}")
    return base_weights


def apply_difficulty_modifier(base_weights: dict, difficulty_percent: float) -> dict:

    #PASSO 2: Aplica o modificador de dificuldade aos pesos base.
    #Diminui "Comum" e aumenta todos os outros.

    # Converte a dificuldade (ex: 80%) para um fator (ex: 0.8)
    difficulty_mod = max(0.0, min(difficulty_percent / 100.0, 1.0))

    print(f"difficulty_mod {difficulty_percent}")
    print(f"difficulty_mod {difficulty_mod}")

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
        print(f"final_wight: {final_weight}")
        final_weights[rarity] = max(0.01, final_weight)
    print(f"final_weights {final_weights}")
    return final_weights


def get_loot_rarity(final_weights: dict) -> str:

    #PASSO 3: Realiza a rolagem de RNG com base nos pesos finais.
    #Retorna o nome da raridade sorteada.

    # Extrai as raridades e seus pesos correspondentes
    rarities = list(final_weights.keys())
    weights = list(final_weights.values())
    # random.choices faz a seleção ponderada para nós
    # Retorna uma lista de 1 item, então pegamos o [0]
    chosen_rarity = random.choices(rarities, weights=weights, k=1)[0] # https://www.google.com/search?q=random.choices+weights&oq=random.choices+wei&gs_lcrp=EgZjaHJvbWUqCQgAEAAYExiABDIJCAAQABgTGIAEMgYIARBFGDkyCggCEAAYExgWGB4yCggDEAAYExgWGB4yCggEEAAYExgWGB4yCggFEAAYExgWGB4yCggGEAAYExgWGB4yCggHEAAYExgWGB4yCggIEAAYgAQYogQyCggJEAAYgAQYogTSAQkyNjM0NmowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
    return chosen_rarity

# --- 3. EXECUÇÃO E SIMULAÇÃO ---

def main_gem():
    #Função principal para demonstrar e testar o sistema.

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

if __name__ == '__main__':
    main_gem()