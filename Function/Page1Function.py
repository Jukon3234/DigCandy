
from threading import Thread
from Function.DiscordBlockDet import GetBlockDET
from Function.Picture import GetPicFunction
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Function.Picture import GetPicFunction
import cv2
import os
import sys
import time
import Function.Foundation as Fun
import pyautogui
import time
import pyperclip
import win32gui
import numpy as np

class RunFunction:
    #===================================debug
    def debugLog(self):
        print("StopFunction: ", Fun.StopFunction)
        print("Function1FightCount: ", Fun.Function1FightCount)
        print("TypeSelect: ", Fun.TypeSelect)
        print("RunFlag: ", Fun.RunFlag)
    #====================================function
    def Mbox(self, title, text, style):
        return windll.user32.MessageBoxW(0, text, title, style)
        
    def RunFGscrept(self):
        if Fun.RunFlag == False:
            Fun.RunFlag = True
            Fun.StopFunction = False
            NoFrame = False
            x = GetPicFunction()
            try:
                a,b = x.getpoc()
                pyautogui.click(a+100,b+100)
            except:
                Fun.RunFlag = False
                NoFrame = True

                self.Mbox('警告', '檢測到取得視窗畫面異常', 0)
            #到主畫面時
            if Fun.Function1FightCount == 0 and NoFrame == False:
                #無限迴圈
                def Digloop():
                    while Fun.StopFunction == False:
                        try:
                            for i in range (1,10):
                                if i == 1:#ctrl
                                    pyautogui.hotkey('ctrl')
                                elif i == 2:#Down
                                    pyautogui.hotkey('down')
                                elif i == 3:#mouse click
                                    pyautogui.click(a+100,b+100)

                                if Fun.StopFunction:
                                    Fun.RunFlag = False
                                    break
                                if Fun.StepDelay != 0:
                                    Delay = Fuc.StepDelay/1000
                                    time.sleep(Delay)
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                break
                        except:
                            print("Function fail")
                            Fun.RunFlag = False
            else:
                #有限迴圈
                def Digloop():
                    for i in range(Fun.Function1FightCount):
                        C=i+1
                        TC=Fun.Function1FightCount
                        
                        for j in range (1,10):
                            if j == 1:#ctrl
                                pyautogui.hotkey('ctrl')
                            elif j == 2:#Down
                                pyautogui.hotkey('down')
                            elif j == 3:#mouse click
                                print("mouse")

                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                break
                            if Fun.StepDelay != 0:
                                Delay = Fuc.StepDelay/1000
                                time.sleep(Delay)
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            break
                        if Fun.StepDelay != 0:
                            RDelay = Fuc.RoundDelay/1000
                            time.sleep(RDelay)
                    Fun.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=Digloop)
            functionthread.setDaemon(True)
            functionthread.start()