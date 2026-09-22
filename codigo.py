import pyautogui
import time
import pandas as pd

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pd.read_csv("C:/Users/INTEL/Documents/GITHUB/Automações de Tarefas e Bots/PRODUTOS2.CSV")

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=751, y=367)
pyautogui.write("arthurbhamoy@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha muito muito dificil")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

print(tabela)  

for linha in tabela.index:
    pyautogui.click(x=757, y=269)
    codigo = str(tabela.loc[linha, "codigo"]) 
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        pyautogui.press("tab")

pyautogui.press("enter")
pyautogui.scroll(5000)
