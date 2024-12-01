#vamos solicitar como entrada dois número inteiros e depois vamos realizar um operação simples entre eles.

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

operacao = input("Digite a operação que deseja realizar (+,-,*,/):")

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(abs(num1 - num2))
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print('Operação Inválida')

