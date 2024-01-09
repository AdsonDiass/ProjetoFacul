import pyautogui
import time #pause especificamente uma linha do codigo
#escrever - write
#clicar - click
#apertar uma tecla -  press
#apertar mais de uma tecla - hotkey
# rolar pagina - scroll(numero)

#instalar pip isntallpandas numpy openpyxl e pip install pyautogui
pyautogui.PAUSE = 1 #pause o codigo inteira 

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
time.sleep(5)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x= 974, y= 475)
pyautogui.write("fernando@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234567890")
pyautogui.press("tab")
pyautogui.press("enter")

import pandas
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: #repetir as linhas
   #manual #pyautogui.write("6.95")
  #pyautogui.press("tab")
 
 pyautogui.click(x=767, y=322)
 #codigo
 codigo = tabela.loc[linha, "codigo"]
 pyautogui.write(codigo)
 pyautogui.press("tab")
 #marca
 pyautogui.write(tabela.loc[linha, "marca"])
 pyautogui.press("tab")
 #tipo
 pyautogui.write(tabela.loc[linha, "tipo"])
 pyautogui.press("tab")
 #categoria
 pyautogui.write(str(tabela.loc[linha, "categoria"])) # "1"
 pyautogui.press("tab")
 #preco
 pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
 pyautogui.press("tab")
 #custo
 pyautogui.write(str(tabela.loc[linha, "custo"]))
 pyautogui.press("tab")
 #obs
 obs = tabela.loc[linha, "obs"]
 if not pandas.isna(obs):
    pyautogui.write(obs)

 pyautogui.press("tab")
 
 pyautogui.press("enter")
 pyautogui.scroll(500)

