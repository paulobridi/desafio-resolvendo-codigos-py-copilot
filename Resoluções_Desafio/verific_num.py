#Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
#Uma dica é: Utilize condicionais para realizar a verificação e,
#se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.


def verificar_paridade(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

# Entrada do usuário
numero = int(input("Digite um número inteiro: "))
resultado = verificar_paridade(numero)
print(f"O número {numero} é {resultado}.")

#Digite no terminal: python verific_num.py 
