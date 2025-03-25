from pynput.keyboard import Controller
import pyautogui
from PIL import Image
import time

keyboard = Controller()

def printScreen(x, y, largura, altura):
    return pyautogui.screenshot(region=(x, y, largura, altura))

def recognizeColor(printScreen, corAlvo, tolerancia=30):
    printScreen = printScreen.convert("RGB")
    pixels = printScreen.load()
    r_alvo, g_alvo, b_alvo = corAlvo

    for i in range(printScreen.width):
        for j in range(printScreen.height):
            r, g, b = pixels[i, j]
            if (abs(r - r_alvo) <= tolerancia and
                abs(g - g_alvo) <= tolerancia and
                abs(b - b_alvo) <= tolerancia):
                print(f"Cor encontrada na posição X = {i}, Y = {j}")
                return True
    # print("Cor não encontrada")
    return False

def press_key(key):
    keyboard.press(key)

def release_key(key):
    keyboard.release(key)

def main():
    x, y, largura, altura = 608, 786, 250, 40
    cores = {
        "amarelo": (240, 240, 0),
        "vermelho": (237, 0, 12),
        "verde": (0, 179, 0)
    }
    teclas = {
        "amarelo": "j", 
        "vermelho": "s",
        "verde": "a"  
    }

    # # Foca na janela do jogo
    # pyautogui.click(x=500, y=500)  # Substitua pelas coordenadas da janela do jogo
    # time.sleep(1)

    tecla_pressionada = None

    while True:
        tela = printScreen(x, y, largura, altura)
        cor_encontrada = False

        for nomeCor, corRGB in cores.items():
            if recognizeColor(tela, corRGB):
                if tecla_pressionada != teclas[nomeCor]:
                    if tecla_pressionada:
                        release_key(tecla_pressionada)
                    press_key(teclas[nomeCor])
                    tecla_pressionada = teclas[nomeCor]
                cor_encontrada = True
                break

        if not cor_encontrada and tecla_pressionada:
            release_key(tecla_pressionada)
            tecla_pressionada = None

        # time.sleep(0.s05)  # Pequeno delay para evitar uso excessivo da CPU

if __name__ == "__main__":
    main()