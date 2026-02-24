from core.colors import *
from core.functions.manager_db import *
from core.models.models import Character

print(f"{HIGHLIGHT}===================================={RESET}")
print(f"{HIGHLIGHT}{BOLD}            THE TOWER               {RESET}")
print(f"{HIGHLIGHT}===================================={RESET}")
print(f"{H3}{ITALIC}Hey you fool! Want to enter the Tower? Maybe you are worthy....\nbut first...{RESET}")
print(f"\n{H1}~~~WHO YOU ARE??~~~{RESET}\n")


def menu_criacao_personagem():
    player_character = Character
    archetype_list = load_archetype_data(return_list=True) # Lista de Archetypes [Archetype(name="Berserker",...), Archetype(),...]
    print(f"{H4}Choose your class: {RESET}")
    for i, archetype in enumerate(archetype_list):
        print(f"[{i+1}] {archetype.name}")
    classe = input("\nDigite o número da classe: ")
    print(player_character)
    print(archetype_list)

    pass

def new_character():
    escolha = menu_criacao_personagem()

    # Aqui entra a lógica de instanciar a classe dataclass do models.py que vimos antes
    if escolha == '1':
        print("Você escolheu Guerreiro! Preparando para entrar na Torre...")
        # char = Character(name="Hero", archetype=WarriorArchetype, ...)

new_character()