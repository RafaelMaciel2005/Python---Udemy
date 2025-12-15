import pyautogui as posicaoAbrirGoogle

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(4)


#Clicamos no botão Start ou seja no botão do Windows
posicaoAbrirGoogle.doubleClick(x=111, y=39)

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(6)

#Digitamos o site do google
posicaoAbrirGoogle.typewrite('https://www.google.com/')

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(3)

#Apertamos a tecla enter
posicaoAbrirGoogle.press('enter')

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(7)

#Digitamos o site do google
posicaoAbrirGoogle.typewrite('Dolar hoje')

#Tempo de espera para o computador pensar
posicaoAbrirGoogle.sleep(3)

#Apertamos a tecla enter
posicaoAbrirGoogle.press('enter')

