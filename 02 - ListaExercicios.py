valorDolar = float(input("Digite o valor do dolar: "))
cotacaoDolar = float(input("Digite o valor da cotação atual do dolar: "))

valorReal = valorDolar * cotacaoDolar

print(f"com {str(valorDolar)} dolares você tera {str(valorReal)} reais")

# ==============================================================================

import math

cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"O valor da hipotenusa é: {str(hipotenusa)}")

# ==============================================================================

valorProduto = float(input("Digite o valor do produto: "))
valorDesconto = float(input("Digite o quanto de desconto: "))

desconto = valorDesconto / 100
valorFinal = desconto - valorProduto

print(f"O valor do produto sem desconto é: R${str(valorProduto)}")
print(f"O valor do produto com desconto é: R${str(valorFinal)}")

# ==============================================================================

valorPremio = float(input("Digite o valor do prêmio: "))

colocacao1 = valorPremio * 0.47
colocacao2 = valorPremio * 0.34
colocacao3 = valorPremio * 0.19

print(f"O primeiro lugar receberá: R$ {float(colocacao1)}")
print(f"O segundo lugar receberá: R$ {float(colocacao2)}")
print(f"O terceiro lugar receberá: R$ {float(colocacao3)}")

# ==============================================================================

import math

x1 = float(input("Digite o valor - (x1): "))
x2 = float(input("Digite o valor - (x2): "))
x3 = float(input("Digite o valor - (x3): "))
x4 = float(input("Digite o valor - (x4): "))

media = (math.sqrt(x1) + math.sqrt(x2) + math.sqrt(x3) + math.sqrt(x4)) / 4

print(f"A Média da Raiz Quadrada é: {str(media)}")

# ==============================================================================

codigoProduto = int(input("Digite o código do produto: "))

if (codigoProduto == 1):
    print("Alimento não-perecível")
elif (codigoProduto in [2, 3]):
    print("Alimento perecível")
elif (codigoProduto in [4, 5, 6]):
    print("Vestuário")
elif (codigoProduto in [7, 8, 9]):
    print("Limpeza")
elif (codigoProduto == 10):
    print("Utensílios domésticos")
elif (codigoProduto in [11, 12]):
    print("Eletrônicos")
else:
    print("Código inválido")

# ==============================================================================

distanciaTotal = float(input("Digite a distância total percorrida (em km): "))
combustivelConsumido = float(input("Digite a quantidade de combustível consumida (em litros): "))

consumoMedio = distanciaTotal / combustivelConsumido

print(f"Consumo médio: {str(consumoMedio)} km/l")

if (consumoMedio < 8):
    print("Venda o carro agora!")
elif (consumoMedio >= 8 and consumoMedio <= 12):
    print("Pense em vender o carro!")
else:
    print("Relativamente econômico!")

# ==============================================================================
    
mediaFinal = float(input("Digite a média final do aluno: "))
numFaltas = int(input("Digite o número de faltas do aluno: "))

if (numFaltas) > 14:
    if (mediaFinal) >= 9.0:
        conceito = "B"
    elif (mediaFinal) >= 7.5:
        conceito = "C"
    elif (mediaFinal) >= 6.0:
        conceito = "D"
    elif (mediaFinal) >= 4.0:
        conceito = "E"
    else:
        conceito = "E"
else:
    if (mediaFinal) >= 9.0:
        conceito = "A"
    elif (mediaFinal) >= 7.5:
        conceito = "B"
    elif (mediaFinal) >= 6.0:
        conceito = "C"
    elif (mediaFinal) >= 4.0:
        conceito = "D"
    else:
        conceito = "E"

print(f"Conceito final do aluno: {str(conceito)}")

# ==============================================================================

novoPreco = float(input("Digite o preço do produto: R$ "))

if (novoPreco < 250.00):
    imposto = 0.15
else:
    imposto = 0.25

PrecoImposto = novoPreco * (1 + imposto)

print(f"Novo preço do produto com imposto: R$ {str(PrecoImposto)}")

# ==============================================================================

peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

IMC = peso / altura**2

if (IMC < 18.5):
    print("Abaixo do peso!")
elif (18.5 <= IMC < 25):
    print("Peso esperado!")
elif (25 <= IMC < 30):
    print("Acima do peso!")
else:
    print("Muito acima do peso!")

print(f"O IMC calculado é: {str(IMC)}")

# ==============================================================================

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

resultado = a ** b

print(f"{a} elevado a {b} é igual a {resultado}")

# ==============================================================================

n = int(input("Digite um número inteiro positivo: "))

if(n < 0):
    print("Erro: Não é possível calcular o fatorial de um número negativo")
else:
    fatorial = 1
    i = 1
    while(i <= n):
        fatorial *= i
        i += 1
    print(f'O fatorial de {str(n)} é {str(fatorial)}.')

# ==============================================================================

p = int(input("Digite um número inteiro positivo: "))

if (p < 2):
    print(p, "não é um número primo!")
else:
    primo = True
    i = 2
    while (i <= int(p ** 0.5)):
        if (p % i == 0):
            primo = False
            break
        i += 1

    if (primo):
        print(f"{str(p)} é um número primo!")
    else:
        print(f"{str(p)} não é um número primo!")

# ==============================================================================

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))

numeroPrimo = []
num = a

while (num <= b):
    if (num > 1):

        i = 2

        while (i <= int(num ** 0.5)):
            if (num % i) == 0:
                break
            i += 1
    else:
        numeroPrimo.append(num) # está adicionando os números primos encontrados

num += 1

print(f"Números primos entre {str(a)} e {str(b)}: {str(numeroPrimo)}")

# ==============================================================================

n = int(input("Digite o valor de n para encontrar o n-ésimo termo da Sequência de Fibonacci: "))

fib1 = 1
fib2 = 1

if (n <= 0):
    print("N deve ser um número inteiro positivo maior que 0")
elif (n == 1 or n == 2):
    print(f"O {str(n)} termo da Sequência de Fibonacci é: 1")
else:
    i = 3
    while (i <= n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        i += 1

    print(f"O {str(n)} termo da Sequência de Fibonacci é: {str(fib)}")

# ==============================================================================

n = int(input("Digite um número inteiro positivo: "))

reverso = 0

while (n > 0):
    digito = n % 10
    reverso = reverso * 10 + digito
    n = n // 10

print(f"O número reverso é: {str(reverso)}")

# ==============================================================================

numero = int(input("Insira um número inteiro positivo maior ou igual a 10: "))

if (numero >= 10):

    numero_str = str(numero)
    if (numero_str == numero_str[::-1]):
        print(f"{str(numero)} é um número palíndromo")
    else:
        print(f"{str(numero)} não é um número palíndromo")
        
else:
    print("Por favor, insira um número inteiro positivo maior ou igual a 10")
