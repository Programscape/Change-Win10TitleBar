import winreg
import time
def regcolorchange():
    key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\DWM",0,winreg.KEY_ALL_ACCESS)
    #获取前台窗口的注册表颜色值
    value,type=winreg.QueryValueEx(key, "AccentColor")
    #赋给 AccentColorInactive ，修改后台窗口颜色
    winreg.SetValueEx(key,"AccentColorInactive",0,type,value)
regcolorchange()
