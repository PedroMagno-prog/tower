import re
from core.funcoes.dice_roller import *

def read_action(comando: str) -> list:
    """
    parametro :comando: R#XdYdlAeZ+-W
    ex1: 4d6dl2
    ex2: 2#3d12dl1e-5

    retona obrigatoriamente a lista com todos os possíveis
    comandos, o que for opcional está com or N (N->None)
    return: ['R orN', 'X', 'Y', 'lA orN', 'Z orN', '+-W orN', 'False ou True']
    ex1: ['None', '4', '6', 'l1', 'None', '0', 'True']
    ex2: ['2', '3', '12', 'l1', '12', '5', 'False']
    """
    comando.strip() # Transforma '4d6 + 5' -> '4d6+5'
    comando.lower() # Transforma '3d12Dl2' -> '3d12dl2'

    comando_final = []
    index = 0
    comando_referencia = re.split(r'[#, d, e, +, -]', comando)
    # comando_referencia:
    # ex1: [-- '4', '6', 'l1', -- '0']
    # ex2: ['2', '3', '12', 'l1', '12', '-5']
    # The split() method returns a list of substrings.
    if '#' in comando:
        comando_final.append(comando_referencia[index]) #index=0
        index += 1 #index=1
    else:
        comando_final.append(1)


    comando_final.append(comando_referencia[index]) # X
    comando_final.append(comando_referencia[index + 1]) # Y
    index += 2 #index=3

    if ('l' in comando) or ('h' in comando):
        comando_final.append(comando_referencia[index]) #index=3
        index += 1 #index=4
    else:
        comando_final.append(None)

    # Crítico Explosivo eZ ou e ex: e8, e
    if 'e' in comando:
        comando_final.append(comando_referencia[index]) #index=4
        index += 1 #index=5
    else:
        comando_final.append(None)

    # Modificador + ou - ex: +3, -5
    adicao = True
    if ('-' in comando) or ('+' in comando):
        comando_final.append(comando_referencia[index])
        if '-' in comando:
            adicao = False
    else:
        comando_final.append(0)
    comando_final.append(adicao)
    return comando_final

def run_action(comando: str):
    c = read_action(comando)
    """
    return: ['R orN', 'X', 'Y', 'lA orN', 'Z orN', 'W orN', 'False ou True']
                0      1     2     3         4        5            6
    
    QUAL rolagem fazer é considerar só o A e Z. 
        o W só aplica no resultado final
        o R é simplesmente quantas vez vai fazer
    logo a prioridade do que definir primeiro é:
    l e h, A e Z | X e Y | W | R
         1           2     3   4 
    """
    rolagens = [] # lista de N-listas de resultados. As funcoes vao ter resolvido vantagens etc
    R = int(c[0])
    X = int(c[1])
    Y = int(c[2])
    funcao = roll_XdY
    A = False
    Z = False
    funcao(X, Y)

    if c[4] is not None:
        Z = int(c[4])
        funcao = roll_XdY_eZ
    if c[3] is not None:
        A = int(c[3])

    for r in range(R):
        rolagens[r] = funcao(X, Y)

    pass

run_action("3d6")
