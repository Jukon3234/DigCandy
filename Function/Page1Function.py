
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
    def curmv(self,x,y):
        random_Curmove = random.randint(Fun.NCurmoveTimeRan,Fun.CurmoveTimeRan)
        CurTime=(Fun.CurmoveTime/1000)+ random_Curmove/1000
        print("CurTime",CurTime)
        pyautogui.moveTo(x, y, duration = CurTime)
        pyautogui.mouseDown(x, y, button = 'left')
        pyautogui.mouseUp(x, y, button = 'left')    

    def RunFGscrept(self):
        if Fun.RunFlag == False:
            Fun.RunFlag = True
            Fun.StopFunction = False
            if Fun.Function1FightCount == 0:
                def Digloop():
                    while Fun.StopFunction == False:
                        random_DelayStep = random.randint(Fun.NstepdelayRandom,Fun.stepdelayRandom)
                        random_DelayRound = random.randint(Fun.NRounddelayRandom,Fun.RounddelayRandom)
                        for i in range (1,7):
                            if Fun.RandomX >> 0 or Fun.RandomY >> 0:
                                random_intX = random.randint(Fun.NRandomX,Fun.RandomX)
                                random_intY = random.randint(Fun.NRandomY,Fun.RandomY)
                            else:
                                random_intX = 0
                                random_intY = 0
                            if i == 1:
                                curmoveX=Fun.P1X + random_intX
                                curmoveY=Fun.P1Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 2:#mouse click
                                curmoveX=Fun.P2X + random_intX
                                curmoveY=Fun.P2Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 3:
                                curmoveX=Fun.P3X + random_intX
                                curmoveY=Fun.P3Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 4:
                                curmoveX=Fun.P4X + random_intX
                                curmoveY=Fun.P4Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 5:
                                curmoveX=Fun.P5X + random_intX
                                curmoveY=Fun.P5Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 6:
                                curmoveX=Fun.P6X + random_intX
                                curmoveY=Fun.P6Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                break
                            if Fun.StepDelay != 0:
                                Delay = Fun.StepDelay/1000 + random_DelayStep/1000
                                time.sleep(Delay)
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            break
                        if Fun.RoundDelay != 0:
                            RDelay = Fun.RoundDelay/1000 + random_DelayRound/1000
                            time.sleep(RDelay)                        
            else:
                def Digloop():
                    for i in range(Fun.Function1FightCount):
                        random_DelayStep = random.randint(Fun.NstepdelayRandom,Fun.stepdelayRandom)
                        random_DelayRound = random.randint(Fun.NRounddelayRandom,Fun.RounddelayRandom)
                        for i in range (1,7):
                            if Fun.RandomX >> 0 or Fun.RandomY >> 0:
                                random_intX = random.randint(Fun.NRandomX,Fun.RandomX)
                                random_intY = random.randint(Fun.NRandomY,Fun.RandomY)
                            else:
                                random_intX = 0
                                random_intY = 0
                            if i == 1:
                                curmoveX=Fun.P1X + random_intX
                                curmoveY=Fun.P1Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 2:#mouse click
                                curmoveX=Fun.P2X + random_intX
                                curmoveY=Fun.P2Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 3:
                                curmoveX=Fun.P3X + random_intX
                                curmoveY=Fun.P3Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 4:
                                curmoveX=Fun.P4X + random_intX
                                curmoveY=Fun.P4Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 5:
                                curmoveX=Fun.P5X + random_intX
                                curmoveY=Fun.P5Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            elif i == 6:
                                curmoveX=Fun.P6X + random_intX
                                curmoveY=Fun.P6Y + random_intY
                                self.curmv(curmoveX,curmoveY)
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                break
                            if Fun.StepDelay != 0:
                                Delay = Fun.StepDelay/1000 + random_DelayStep/1000
                                time.sleep(Delay)
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            break
                        if Fun.RoundDelay != 0:
                            RDelay = Fun.RoundDelay/1000 + random_DelayRound/1000
                            time.sleep(RDelay)
                    Fun.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=Digloop)
            functionthread.setDaemon(True)
            functionthread.start()