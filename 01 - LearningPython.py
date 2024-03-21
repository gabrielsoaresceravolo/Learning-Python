variavel_1 = 12
variavel_2 = 2.35
variavel_3 = "Gabriel"
variavel_4 = True
lista = [1,2,3,4,5,6,7,8,9,0]

# ============================================================================

print("Teste de uma frase para ser imprimida")
print(lista)
print("Teste de uma frase" + str(lista))

# ============================================================================

nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")

print("\nOlá " + nome + ", tudo bem?")
print(f"Você realmente tem {idade} anos? 🤔\n")

# ============================================================================

print("\nVocê gostaria de converter de qual para qual?")
print("Converter fahrenheit em celsius? - 1 ")
print("Converter celsius em fahrenheit? - 2\n")

escolha = int(input("Escolha um tipo de conversor: "))

if escolha == 1 :
    fahrenheit = input("Digite a temperatura em fahrenheit: ")
    celsius = (fahrenheit - 32) * 5/9
    print(f"A sua temperatura em fahrenheit equivalem a {celsius} graus Celsius")

elif escolha == 2 :
    celsius = input("Digite a temperatura em celsius: ")
    fahrenheit = (celsius * 9/5) + 32
    print(f"A sua temperatura em fahrenheit equivalem a {fahrenheit} graus Celsius")

else:
    print("Escolha não encontrada!")

# ============================================================================
