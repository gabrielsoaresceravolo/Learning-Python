# -*- coding: utf-8 -*-
"""python-funcoes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aDvbuABsb9MijiEZfE-ch45lwIAZERSJ

# ***Construindo funções em Python***

**Exemplo de função com retorno: Função soma**
"""

def soma(num1, num2):
    result = num1 + num2
    return result

"""**Exemplo de função sem retorno: Função mensagem**"""

def mensagem():
    print("O palmeiras não têm mundial...")

"""**Exemplo chamada de função**"""

def mostrarIdade(idade):
    print("Eu tenho " + str(idade) + " anos!")

mostrarIdade(28)

"""**Exemplo função com parâmetros nomeados**"""

def calcularAreaTriangulo(base, altura):
    return (base * altura / 2.0)

calcularAreaTriangulo(altura = 4.0, base = 2.0)