"""
Wabbajack Download Automator
Author: Pissolato32
License: MIT License
Description: 
    This script automates the process of clicking the "Slow Download" button 
    on Nexus Mods, helping users bypass the need for manual interaction 
    when downloading large modpacks.

Usage:
    Run the script while the download page is open. 
    It will detect and click the "Slow Download" button automatically.

"""


import time
import pyautogui

count = 0  # Número inicial de downloads
start_time = time.time()  # Marca o início da execução

def click_slow_download(count):
    """Procura o botão 'Slow Download' na tela e clica."""
    button_image = r".\slow_download.png"  # Caminho da imagem do botão
    found = False  # Variável para controlar se o botão foi encontrado
    
    try:
        button_location = pyautogui.locateCenterOnScreen(button_image, confidence=0.7)
        
        if button_location:
            pyautogui.click(button_location)
            count += 1  # Incrementa o contador
            print(f"Botão 'Slow Download' clicado!")
            found = True

    except Exception as e:
        pass  # Ignorar exceções e não imprimir erro repetidamente
    
    return count, found

# Loop para monitorar e clicar no botão
print("Procurando o botão 'Slow Download'...")
while True:
    count, found = click_slow_download(count)

    # Ajusta o tempo de espera de acordo com o resultado da busca
    if found:
        time.sleep(2)  # Aguardar 2 segundos quando o botão é encontrado
    else:
        time.sleep(5)  # Aguardar mais tempo quando o botão não é encontrado
