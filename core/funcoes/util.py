def calcular_nivel_party(nivel: int, n_jogadores: int) -> int:
    return nivel * n_jogadores

def convert_dificuldade(dificuldade: str) -> int:
    dificuldades = {"facil": 50, "normal": 75, "dificil": 100, "letal": 125, "impossivel": 150}
    return dificuldades[dificuldade]
