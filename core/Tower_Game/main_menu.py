from core.colors import *
from core.functions.manager_db import load_archetype_data
print(f"{HIGHLIGHT}===================================={RESET}")
print(f"{HIGHLIGHT}{BOLD}            THE TOWER               {RESET}")
print(f"{HIGHLIGHT}===================================={RESET}")
print(f"{H3}{ITALIC}Hey you fool! Want to enter the Tower? Maybe you are worthy...\nbut first..{RESET}")
print(f"\n{H1}~~~WHO YOU ARE??~~~{RESET}\n")


def menu_criacao_personagem():
    load_archetype_data()
    print(f"{H4}Choose your class: {RESET}")
    for i in range(12):
        print(f"[{1}] {}")
    print("[1] Barbarian")
    print("[2] Hunter")
    print("[3] Wizard")
    print("[4] Cleric")
    classe = input("\nDigite o número da classe: ")

    pass

def new_character():
    escolha = menu_criacao_personagem()

    # Aqui entra a lógica de instanciar a classe dataclass do models.py que vimos antes
    if escolha == '1':
        print("Você escolheu Guerreiro! Preparando para entrar na Torre...")
        # char = Character(name="Hero", archetype=WarriorArchetype, ...)

new_character()