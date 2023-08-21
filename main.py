import pyautogui
import time
print("Lütfen gönderilecek mesajı yazınız")
print("Please write the message to be sent")
msg = input()
print("Lütfen mesajın kaç kere atılacağını yazınız")
print("Please write how many times the message will be sent")
tkr = int(input())
for i in range(tkr):
    pyautogui.write(msg)
    pyautogui.press("enter")