
from threading import Thread
from Function.DiscordBlockDet import GetBlockDET
from Function.Picture import GetPicFunction
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
    def RunFGscrept(self):
        if Fun.RunFlag == False:
            self.Info_broswer.setText("腳本啟動")
            Fun.RunFlag = True
            Fun.StopFunction = False
            x = GetPicFunction()
            self.Info_broswer.setText("點擊遊戲視窗")
            pyautogui.click(100,100)
            #找到主畫面時
            if Fun.Function1FightCount == 0:
                #無限迴圈
                def Digloop():
                    self.Info_broswer.setText("進入迴圈")
                    while Fun.StopFunction == False:
                        try:
                            self.Info_broswer.setText("1")
                            pyautogui.hotkey('ctrl')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("2")
                            pyautogui.hotkey('down')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("3")
                            pyautogui.hotkey('ctrl')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("4")
                            pyautogui.hotkey('ctrl')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("5")
                            pyautogui.hotkey('ctrl')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("6")
                            pyautogui.hotkey('down')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("7")
                            pyautogui.hotkey('down')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("8")
                            pyautogui.hotkey('ctrl')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("9")
                            pyautogui.hotkey('ctrl')
                            if Fun.StopFunction:
                                Fun.RunFlag = False
                                self.Info_broswer.setText("中止")
                                break
                            self.Info_broswer.setText("10")
                            Fun.RunFlag = False
                            self.Info_broswer.setText("結束")
                        except:
                            print("Function fail")
                            Fun.RunFlag = False
                            self.Info_broswer.setText("迴圈出錯")
            else:
                #有限迴圈
                def Digloop():
                    for i in range(Fun.Function1FightCount):
                        C=i+1
                        TC=Fun.Function1FightCount
                        
                        self.Info_broswer.setText("1")
                        pyautogui.hotkey('ctrl')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("2")
                        pyautogui.hotkey('down')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("3")
                        pyautogui.hotkey('ctrl')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("4")
                        pyautogui.hotkey('ctrl')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("5")
                        pyautogui.hotkey('ctrl')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("6")
                        pyautogui.hotkey('down')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("7")
                        pyautogui.hotkey('down')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("8")
                        pyautogui.hotkey('ctrl')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("9")
                        pyautogui.hotkey('ctrl')
                        if Fun.StopFunction:
                            Fun.RunFlag = False
                            self.Info_broswer.setText("中止")
                            break
                        self.Info_broswer.setText("10")
                        Fun.RunFlag = False
                        self.Info_broswer.setText("結束")
                        time.sleep(1)
                        if Fun.StopFunction:
                            self.Info_broswer.setText("中止")
                            break
                    Fun.RunFlag = False
        
            global functionthread
            functionthread = Thread(target=Digloop)
            functionthread.setDaemon(True)
            functionthread.start()