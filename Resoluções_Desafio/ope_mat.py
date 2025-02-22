# Solicitar como entrada dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(abs(num1 - num2))
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)
else:
    print("Operação inválida")

# Realizar uma operação simples (soma) entre eles
#resultado = num1 + num2

# Exibir o resultado
#print(f"A soma de {num1} e {num2} é {resultado}")

#Digite no terminal: python ope_mat.py