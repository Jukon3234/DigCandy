
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
import random

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
                            if Fun.RandomX >> 0 or Fun.RandomY >> 0:
                                random_intX = random.randint(Fun.NRandomX,Fun.RandomX)
                                random_intY = random.randint(Fun.NRandomY,Fun.RandomY)
                            if i == 1 or i == 5:#ctrl
                                pyautogui.press('ctrl')
                            elif i == 2:#mouse click
                                pyautogui.click(Fun.P1X + random_intX,Fun.P1Y + random_intY)
                            elif i == 3:
                                pyautogui.click(Fun.P2X + random_intX,Fun.P2Y + random_intY)
                            elif i == 4:
                                pyautogui.click(Fun.P3X + random_intX,Fun.P3Y + random_intY)
                            elif i == 6:
                                pyautogui.click(Fun.P4X + random_intX,Fun.P4Y + random_intY)
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
                            random_intX = random.randint(Fun.NRandomX,Fun.RandomX)
                            random_intY = random.randint(Fun.NRandomY,Fun.RandomY)
                            if i == 1 or i == 5:#ctrl
                                pyautogui.press('ctrl')
                            elif i == 2:#mouse click
                                pyautogui.click(Fun.P1X + random_intX,Fun.P1Y + random_intY)
                            elif i == 3:
                                pyautogui.click(Fun.P2X + random_intX,Fun.P2Y + random_intY)
                            elif i == 4:
                                pyautogui.click(Fun.P3X + random_intX,Fun.P3Y + random_intY)
                            elif i == 6:
                                pyautogui.click(Fun.P4X + random_intX,Fun.P4Y + random_intY)
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