# Desafio 3: Operações Matemáticas

# Solicitar ao usuário a entrada de dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada: (+, -, /, *)")

if operacao == '+':
    print(num1 + num2);
elif operacao == '-':
    print(num1 - num2);
elif operacao == '/':
    print(num1 / num2);
elif operacao == '*':
    print(num1 * num2);