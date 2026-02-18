from core.cores import RED, END_COLOR
lista_familias = ["Aberração", "Aranha", "Bandido", "Constructo", "Cultista", "Dragão", "Elfo Negro",
    "Fada", "Fera", "Gigante", "Gnoll", "Goblin", "Homem-Cobra", "Homem-Lagarto", "Humanoide", "Infernal",
    "Kobold", "Limo", "Monstruosidade", "Morto-Vivo", "Orc", "Planta", "Troglodita"]

def calcular_nivel_party(nivel: int, n_jogadores: int) -> int:
    return nivel * n_jogadores

def convert_dificuldade(dificuldade: str) -> int:
    print(f"{RED}Function: convert_dificuldade{END_COLOR}")
    dificuldade = dificuldade.strip().lower()
    dificuldades = {"facil": 50, "f": 50,
                    "normal": 75, "n": 75,
                    "dificil": 100, "d": 100,
                    "letal": 125, "l": 125,
                    "impossivel": 150, "i": 150}
    return dificuldades[dificuldade]

def listar_monstros_por_familia(lista_monstros_nao_filtrada:list, familia:str)-> list:
    print(f"{RED}Function: listar_monstros_por_familia{END_COLOR}")
    lista_monstros = list()
    for monstro in lista_monstros_nao_filtrada:
        if monstro.tipo != "Lendario":
            lista_monstros.append(monstro)

    if familia not in lista_familias:
        return lista_monstros

    lista_monstros_final = list()
    for monstro in lista_monstros:
        if monstro.familia == familia:
            lista_monstros_final.append(monstro)
    return lista_monstros_final