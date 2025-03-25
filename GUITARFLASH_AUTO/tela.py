import pyautogui
import time

print("Posicione o mouse na área desejada e aguarde 5 segundos...")
time.sleep(5)
x, y = pyautogui.position()
print(f"Coordenadas atuais do mouse: X = {x}, Y = {y}")