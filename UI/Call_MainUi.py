from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from UI.Homepage.ui_MainUI import Ui_GBF_MAIN
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
import systemdata.icon.ICON
from Function.Page1Function import RunFunction
from Function.DebugFunction import Debugfunction
from Function.Position import GBFPosition
from Function.DiscordBlockDet import GetBlockDET
from Function.Picture import GetPicFunction
import Function.Foundation as Fun
import json
import datetime
from win32gui import *
from ctypes import windll, byref
from ctypes.wintypes import HWND, POINT
import time
import sys
import win32gui
import os
import pyautogui as pag
import cv2
import keyboard
from pynput.mouse import Listener

class MainPageWindow(QtWidgets.QMainWindow,Ui_GBF_MAIN):
    chooseSignal = pyqtSignal(str)

    def __init__(self,parent=None):#起始位置
        super(MainPageWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUiindex()
        self.initbuttonUI()
        self.default()
        

    def initUiindex(self):#UI框架基礎設定
        titleicon = QtGui.QIcon()
        titleicon.addPixmap(QtGui.QPixmap(":/ICON.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Helpicon = QtGui.QIcon()
        self.setWindowIcon(titleicon)
        self.setWindowTitle('星爆螞蟻人 V0.1.1')#title
        Helpicon.addPixmap(QtGui.QPixmap(":/Heip.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)

    def default(self):#框架預設#最初全域變數歸檔
        if os.path.exists('./systemdata/datasave/data.json'):
            SaveFile = open('systemdata/datasave/data.json')
        else:
            SaveFile = open('systemdata/datasave/Default.json')
        savedata= json.load(SaveFile)
        Fun.DCBOT_Token = savedata['Bot']['TOKEN']
        Fun.DCBOT_ChannalID = savedata['Bot']['Channal_ID']
        self.RoundspinBox.setValue(savedata['Delay']['RoundDelay'])
        self.stepspinBox.setValue(savedata['Delay']['StepDelay'])
        self.Times_spinBox_2.setValue(savedata['function']['FightCount'])

        self.P1SPINX.setValue(savedata['Point']['P1X'])
        Fun.P1X = savedata['Point']['P1X']
        self.P2SPINX.setValue(savedata['Point']['P2X'])
        Fun.P2X = savedata['Point']['P2X']
        self.P3SPINX.setValue(savedata['Point']['P3X'])
        Fun.P3X = savedata['Point']['P3X']
        self.P4SPINX.setValue(savedata['Point']['P4X'])
        Fun.P4X = savedata['Point']['P4X']

        self.P1SPINY.setValue(savedata['Point']['P1Y'])
        Fun.P1Y = savedata['Point']['P1Y']
        self.P2SPINY.setValue(savedata['Point']['P2Y'])
        Fun.P2Y = savedata['Point']['P2Y']
        self.P3SPINY.setValue(savedata['Point']['P3Y'])
        Fun.P3Y = savedata['Point']['P3Y']
        self.P4SPINY.setValue(savedata['Point']['P4Y'])
        Fun.P4Y = savedata['Point']['P4Y']

        self.SaveText.setText(" ")
        self.setMouseTracking(True)



    def initbuttonUI(self):#按鈕設定
        self.actionHelp.triggered.connect(self.showDialog)
        self.actionsetting.triggered.connect(self.showDialog)
        self.Screptrun.clicked.connect(self.showDialog)
        self.FuncStopButton.clicked.connect(self.showDialog)
        self.SetButton.clicked.connect(self.showDialog)
        self.Times_spinBox_2.valueChanged.connect(self.showDialog)
        self.stepspinBox.valueChanged.connect(self.showDialog)
        self.RoundspinBox.valueChanged.connect(self.showDialog)
        self.FRWidge.clicked.connect(self.showDialog)
        keyboard.add_hotkey('F2', self.on_hotkey_triggered)
        keyboard.add_hotkey('Esc', self.on_hotkey_Stop)
        #self.DebugButton.clicked.connect(self.showDialog)
        self.P1.clicked.connect(self.showDialog)
        self.P2.clicked.connect(self.showDialog)
        self.P3.clicked.connect(self.showDialog)
        self.P4.clicked.connect(self.showDialog)
    
    
    
    def showDialog(self):#按鈕function
        sender = self.sender()
        if sender == self.actionHelp:
            self.chooseSignal.emit('Help')
        elif sender == self.actionsetting:
            self.chooseSignal.emit('setting')
        elif sender == self.Screptrun:
            self.Info_broswer.setText("腳本執行中")
            x=RunFunction()
            x.RunFGscrept()
            self.Info_broswer.setText(Fun.BroswerText)
        elif sender == self.FuncStopButton:
            Fun.StopFunction = True
            self.Info_broswer.clear()
            self.Mbox('緊急中止', '中止', 0)
        elif sender == self.SetButton:
            self.SaveFile()
        elif sender == self.Times_spinBox_2:
            self.settingtext()
        elif sender == self.FRWidge:
            self.chooseSignal.emit('change')
        elif sender == self.stepspinBox:
            self.SettingDelay()
        elif sender == self.RoundspinBox:
            self.SettingDelay()
        elif sender == self.P1:
            def on_click(x, y, button, pressed):
                if pressed:
                    Fun.P1X,Fun.P1Y = x, y                                        
                    listener.stop()                
            listener = Listener(on_click = on_click)
            listener.start()
            listener.join()
            self.P1SPINX.setValue(Fun.P1X)
            self.P1SPINY.setValue(Fun.P1Y)
        elif sender == self.P2:
            def on_click(x, y, button, pressed):
                if pressed:
                    Fun.P2X,Fun.P2Y = x, y                    
                    listener.stop()                
            listener = Listener(on_click = on_click)
            listener.start()
            listener.join()
            self.P2SPINX.setValue(Fun.P2X)
            self.P2SPINY.setValue(Fun.P2Y)
        elif sender == self.P3:
            def on_click(x, y, button, pressed):
                if pressed:
                    Fun.P3X,Fun.P3Y = x, y
                    listener.stop()                
            listener = Listener(on_click = on_click)
            listener.start()
            listener.join()
            self.P3SPINX.setValue(Fun.P3X)
            self.P3SPINY.setValue(Fun.P3Y)
        elif sender == self.P4:
            def on_click(x, y, button, pressed):
                if pressed:
                    Fun.P4X,Fun.P4Y = x, y                    
                    listener.stop()                
            listener = Listener(on_click = on_click)            
            listener.start()
            listener.join()
            self.P4SPINX.setValue(Fun.P4X)
            self.P4SPINY.setValue(Fun.P4Y)
            
                        
        #elif sender == self.DebugButton:
        #   if Fun.DCBOT_EN == True:
        #       DET = GetPicFunction()
        #       DET2 = GetBlockDET()
        #       Picture = cv2.imread('./systemdata/img/systemimg/BLOCK.PNG')
        #       if DET.PicDetTF(Picture) == True:
        #           DET2.SysGetPic()
        #           DET2.DC_Get_Verify()
        #    else:
        #       print("no Function")
        #elif sender == self.DebugButton:
        #    self.SetScreenfuntion()
        #    x=Debugfunction()
        #    x.debugLog()
    def on_hotkey_triggered(self):
        if Fun.RunFlag == False:
            QMetaObject.invokeMethod(self.Info_broswer, 'setText', Qt.QueuedConnection, Q_ARG(str, "腳本執行中"))
            x=RunFunction()
            x.RunFGscrept()
            if Fun.BroswerText != " ":
                QMetaObject.invokeMethod(self.Info_broswer, 'setText', Qt.QueuedConnection, Q_ARG(str, Fun.BroswerText))
    
    def on_hotkey_Stop(self):
        if Fun.StopFunction == False:
            Fun.StopFunction = True
            QMetaObject.invokeMethod(self.Info_broswer, 'setText', Qt.QueuedConnection, Q_ARG(str, "中斷程序"))
            self.Mbox('終止', '緊急終止', 0)

    def Mbox(self, title, text, style):
        return windll.user32.MessageBoxW(0, text, title, style)

    def settingtext(self):
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        if Fun.Function1FightCount == 0:
            self.label_1.setText("Set 無上限")
        else:
            self.label_1.setText("Set :"+str(Fun.Function1FightCount))

    def SettingDelay(self):
        Fun.StepDelay = self.stepspinBox.value()
        Fun.RoundDelay = self.RoundspinBox.value()

    def SaveFile(self):
        Fun.Function1FightCount = self.Times_spinBox_2.value()
        Savedata = {}
        Savedata['function'] = {'FightCount': Fun.Function1FightCount}
        Savedata['Bot'] = {'TOKEN': Fun.DCBOT_Token,'Channal_ID': Fun.DCBOT_ChannalID,'Enabled' : Fun.DCBOT_EN}
        Savedata['Delay']={'StepDelay': Fun.StepDelay, 'RoundDelay': Fun.RoundDelay}
        Savedata['Point'] = {'P1X': Fun.P1X,'P1Y': Fun.P1Y,'P2X': Fun.P2X, 'P2Y': Fun.P2Y,'P3X' : Fun.P3X, 'P3Y' : Fun.P3Y, 'P4X' : Fun.P4X, 'P4Y' : Fun.P4Y}
        with open('systemdata/datasave/data.json', 'w') as datafile:
            json.dump(Savedata,datafile)
        self.SaveText.setText("set成功")
        print("set成功")

    def Blockdet(slef):
        DET = GetBlockDET()
        if DET.FuncBlockPicDet() == True:
            DET.SysGetPic()
            DET.DC_Get_Verify()