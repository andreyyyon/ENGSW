import pyautogui
from PIL import Image

# Coordenadas e dimensões
x, y, largura, altura = 608, 786, 250, 40

# Captura a região da tela
screenshot = pyautogui.screenshot(region=(x, y, largura, altura))

# Salva a captura de tela para verificação
screenshot.save("regiao_capturada.png")

# Exibe a captura de tela (opcional)
screenshot.show()