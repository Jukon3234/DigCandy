
from threading import Thread
from Function.DiscordBlockDet import GetBlockDET
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import os
import sys
import time
import Function.Foundation as Fun
import pyautogui

class RunFunction:
    #===================================debug
    def debugLog(self):
        print("StopFunction: ", Fun.StopFunction)
        print("Function1FightCount: ", Fun.Function1FightCount)
        print("TypeSelect: ", Fun.TypeSelect)
        print("RunFlag: ", Fun.RunFlag)
    #====================================function
    def RunFGscrept(self):
        if Fun.RunFlag == False:
            Fun.RunFlag = True
            Fun.StopFunction = False
            if Fun.Function1FightCount == 0:
                def Digloop():
                    while Fun.StopFunction == False:
                        
                        for i in range (1,7):
                            if i == 1 or i == 5:#ctrl
                                pyautogui.keyDown('ctrl')
                                time.sleep(0.13)
                                pyautogui.keyUp('ctrl')
                            elif i == 2:#mouse click
                                pyautogui.click(Fun.P1X,Fun.P1Y)
                            elif i == 3:
                                pyautogui.click(Fun.P2X,Fun.P2Y)
                            elif i == 4:
                                pyautogui.click(Fun.P3X,Fun.P3Y)
                            elif i == 6:
                                pyautogui.click(Fun.P4X,Fun.P4Y)
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                break
                            if Fun.StepDelay != 0:
                                Delay = Fun.StepDelay/1000
                                time.sleep(Delay)
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            break
                        if Fun.RoundDelay != 0:
                            RDelay = Fun.RoundDelay/1000
                            time.sleep(RDelay)
                        
            else:
                def Digloop():
                    for i in range(Fun.Function1FightCount):
                        for i in range (1,7):
                            if i == 1 or i == 5:#ctrl
                                pyautogui.hotkey('ctrl')
                            elif i == 2:#mouse click
                                pyautogui.click(Fun.P1X,Fun.P1Y)
                            elif i == 3:
                                pyautogui.click(Fun.P2X,Fun.P2Y)
                            elif i == 4:
                                pyautogui.click(Fun.P3X,Fun.P3Y)
                            elif i == 6:
                                pyautogui.click(Fun.P4X,Fun.P4Y)
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                break
                            if Fun.StepDelay != 0:
                                Delay = Fun.StepDelay/1000
                                time.sleep(Delay)
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            break
                        if Fun.RoundDelay != 0:
                            RDelay = Fun.RoundDelay/1000
                            time.sleep(RDelay)
                    Fun.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=Digloop)
            functionthread.setDaemon(True)
            functionthread.start()