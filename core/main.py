from funcoes.util import run_action
from funcoes.rng import abrir_bau
from funcoes.cadastro_db import (
    carregar_dados,
    salvar_dados,
    criar_monstro,
    cadastro_monstro,
    cadastro_loot,
    ver_monstros,
    ver_loots
)

valor_em_po = {} # tabelar raridade com um valor X em PO

def gerar_encontro(nivel_party):
    dificuldade = int(input("Qual dificuldade deve ser o encontro? --> "))

    # level total dos monstros deve ser a soma dos niveis dos players

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


if __name__ == "__main__":
    main()
