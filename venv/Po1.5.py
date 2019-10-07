import pyautogui
import time
#pyautogui.mouseInfo()
#pyautogui.position()
#pyautogui.click()=simula el click izquierdo del mouse
#pyautogui.typewrite('message')=simula que se esta escribiendo un mensaje
#pyautogui.hotkey()
#pyautogui.moveTo()=simula el movimiento del cursor del raton

n=int(input("Numero de veces: "))
for i in range(n):
    print(pyautogui.click(182 ,71 ))
    pyautogui.typewrite('https://www.pinterest.es/')
    pyautogui.hotkey("enter")
    time.sleep(4)
    pyautogui.moveTo(1093, 232)
    time.sleep(2)
    pyautogui.click(1093 , 232)
    pyautogui.moveTo(880 , 435)
    time.sleep(2)
    pyautogui.click(880 , 455)
    pyautogui.typewrite(f"2{i}120769@ce.pucmm.edu.do")
    pyautogui.moveTo(912,498)
    time.sleep(2)
    pyautogui.click(912 , 498)
    pyautogui.typewrite(f"Pucmm2012{i}")
    pyautogui.moveTo(836 , 561)
    time.sleep(2)
    pyautogui.click(836 , 561)
    pyautogui.typewrite("25")
    pyautogui.moveTo(907 , 617)
    time.sleep(2)
    pyautogui.click(907 , 617)
