import pyautogui as auto
import time
import os

def mostrar_coordenadas_mouse():
    while True:
        coordenadas = auto.position()
        print(f"(X: {coordenadas.x}) (Y: {coordenadas.y})")
        time.sleep(1)

if __name__ == "__main__":
    os.system('cls')
    print(f"Sistema carregando...")
    print(f"Pressione Ctrl + C para sair\n")
    time.sleep(5)
    mostrar_coordenadas_mouse()
