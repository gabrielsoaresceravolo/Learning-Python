# Considere as seguintes regras/clausulas e implemente um código em Prolog que responda cada uma das perguntas abaixo
#
# progenitor(sara, isaque).
# progenitor(abraão, isaque).
# progenitor(abraão, ismael).
# progenitor(isaque, esaú).
# progenitor(isaque, jacó).
# progenitor(jacó, josé).
#
# Quem são os filhos de José?
# Quem é progenitor de José?
# Esaú e Jacó possuem um progenitor em comum? Se sim que é ele?
# Quem são os netos de Abraão?
# -------------------------------------------------------------
#
# Progenitor(José, x) = FALSE
# Progenitor(x, José) = Jacó
#
# Progenitor(x, Esaú) = Isaque
# Progenitor(x, Jacó) = Isaque
# -Sim, eles possuem um progenitor em comum que é isaque
#
# Progenitor(Abraão, x), Progenitor(x, y) = Esaú, Jacó

# -=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=

# Implemente um algoritmo em Python, que dado a distância total (em km) percorrida por um
# automóvel e a quantidade de combustível (em litros) consumida para percorrê-la, calcule o consumo
# médio de combustível. OBS: Consumo médio = Distância Percorrida / Litros Consumidos. Mostre o
# consumo médio obtido e uma mensagem conforme a tabela abaixo:
#
# Consumo < 5 Venda o carro agora!
# 5>= Consumo =< 10 Pense em vender o carro!
# Consumo > 10 Relativamente econômico!

distancia = float(input("Digite a distancia percorrida em Km: "))
combustivel = float(input("Digite a quantidade de combustivel em litros consumido: "))

consumoMedio = distancia / combustivel

if consumoMedio < 5:
    print("Venda o carro agora!")
elif 5 <= consumoMedio <= 10:
    print("Pense em vender o carro!")
else:
    print("Relativamente econômico!")

# -=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=

print("Qual numero você deseja decobrir o fatorial?")
numero = float(input("Numero: "))

# Função que transforma o numero inteiro em fatorial
def calcular_fatorial(numero):

    if numero < 0: # Verificar se o número é positivo
        return "O número deve ser positivo!"

    # Descobrindo o fatorial
    elif numero == 0:
        return 1
    else:
        fatorial = 1

        # Valor do numero fatorial
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")


