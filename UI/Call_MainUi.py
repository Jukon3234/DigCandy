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
        self.setWindowTitle('螞蟻人 V0.0.1')#title
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
        self.SaveText.setText(" ")



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

        with open('systemdata/datasave/data.json', 'w') as datafile:
            json.dump(Savedata,datafile)
        self.SaveText.setText("set成功")
        print("set成功")

    def Blockdet(slef):
        DET = GetBlockDET()
        if DET.FuncBlockPicDet() == True:
            DET.SysGetPic()
            DET.DC_Get_Verify()