from simpleeval import simple_eval
# CUIDADO: Este código é INSEGURO.
print("Calculadora Simples (Versão Insegura)")
print("Digite 'sair' para terminar.")

while True:
    expressao = input("Digite o cálculo: ")
    atr = int(input("o que adicionar?: "))
    if expressao.lower() == 'sair':
        break

    try:
        # A função eval() executa a string como código
        resultado = simple_eval(expressao+f"+{atr}")
        print(f"Resultado: {resultado}")
    except Exception as e:
        # Trata erros de sintaxe (ex: "5 + * 3")
        print(f"Erro na expressão: {e}")