from core.colors import *

print(f"{HIGHLIGHT}===================================={RESET}")
print(f"{HIGHLIGHT}{BOLD}            THE TOWER               {RESET}")
print(f"{HIGHLIGHT}===================================={RESET}")
print(f"{H3}{ITALIC}Hey you fool! Want to enter the Tower? Maybe you are worthy...\nbut first..{RESET}")
print(f"\n{H1}~~~WHO YOU ARE??~~~{RESET}\n")


def menu_criacao_personagem():

    print(f"{H4}Choose your class: {RESET}")
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