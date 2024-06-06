# Importações

import os
import random

# ======================================================================================================================
# Caracteres Zalgos

zalgo_up = [
    '\u030d', '\u030e', '\u0304', '\u0305', '\u033f', '\u0311', '\u0306', '\u0310', '\u0352', '\u0357',
    '\u0351', '\u0307', '\u0308', '\u030a', '\u0342', '\u0343', '\u0344', '\u034a', '\u034b', '\u034c',
    '\u0303', '\u0302', '\u030c', '\u0350', '\u0300', '\u0301', '\u030b', '\u030f', '\u0312', '\u0313',
    '\u0314', '\u033d', '\u0309', '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369',
    '\u036a', '\u036b', '\u036c', '\u036d', '\u036e', '\u036f', '\u033e', '\u035b'
]

zalgo_down = [
    '\u0316', '\u0317', '\u0318', '\u0319', '\u031c', '\u031d', '\u031e', '\u031f', '\u0320', '\u0324',
    '\u0325', '\u0326', '\u0329', '\u032a', '\u032b', '\u032c', '\u032d', '\u032e', '\u032f', '\u0330',
    '\u0331', '\u0332', '\u0333', '\u0339', '\u033a', '\u033b', '\u033c', '\u0345', '\u0347', '\u0348',
    '\u0349', '\u034d', '\u034e', '\u0353', '\u0354', '\u0355', '\u0356', '\u0359', '\u035a', '\u0323'
]

zalgo_mid = [
    '\u0315', '\u031b', '\u0340', '\u0341', '\u0358', '\u0321', '\u0322', '\u0327', '\u0328', '\u0334',
    '\u0335', '\u0336', '\u034f', '\u035c', '\u035d', '\u035e', '\u035f', '\u0360', '\u0362', '\u0338',
    '\u0337', '\u0361', '\u0489'
]

# ======================================================================================================================
# Gerador Zalgo

def zalgo_text(text, intensity=10):
    zalgo_text = ''

    for char in text:
        if char.isalpha():
            for i in range(random.randint(0, intensity)):
                zalgo_text += random.choice(zalgo_up + zalgo_down + zalgo_mid)
        zalgo_text += char
    return zalgo_text

# ======================================================================================================================
# Logica INPUT / OUTPUT

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para o usuário inserir o texto
def user_input_name():
    clear_console()
    name = input("Digite o texto que você deseja converter para Zalgo: ")
    return name
original_name = user_input_name()

# Gera 15 Zalgo aleatorios
zalgo_names = []
for _ in range(1):
    zalgo_name = zalgo_text(original_name)
    zalgo_names.append(zalgo_name)

# Obtém o caminho da área de trabalho para Salva o zalgos gerados em um arquivo na área de trabalho
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
file_path = os.path.join(desktop_path, "Zalgo.txt")

with open(file_path, "w", encoding="utf-8") as file:
    for name in zalgo_names:
        file.write(name + "\n")

print("\n\nSeu Zalgo foi criado e salvo em um arquivo .txt na area de trabalho\n\n")
