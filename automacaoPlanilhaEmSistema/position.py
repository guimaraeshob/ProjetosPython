import pyautogui
import time

time.sleep(4)
# Obtenha a posição atual do mouse
x, y = pyautogui.position()

# Exiba as coordenadas x e y
print(f"A posição do mouse é x: {x}, y: {y}")
