import pyautogui
#pyautogui.mouseInfo()
#pyautogui.position()
#pyautogui.click()=simula el click izquierdo del mouse
#pyautogui.typewrite('message')=simula que se esta escribiendo un mensaje
#pyautogui.hotkey()
#pyautogui.moveTo()=simula el movimiento del cursor del raton

print(pyautogui.click(182 ,71 ))
pyautogui.typewrite('https://www.pinterest.es/')
pyautogui.hotkey("enter")
pyautogui.moveTo(1093, 232 , 3)
pyautogui.click(1093 , 232)
pyautogui.moveTo(880 , 435 , 1.75)
pyautogui.click(880 , 455)
pyautogui.typewrite("20120769@ce.pucmm.edu.do")
pyautogui.moveTo(912,498 , 1.75)
pyautogui.click(912 , 498)
pyautogui.typewrite("Pucmm2012")
pyautogui.moveTo(836 , 561 , 1.75)
pyautogui.click(836 , 561)
pyautogui.typewrite("25")
pyautogui.moveTo(907 , 617 , 1.75)
pyautogui.click(907 , 617)
