# -*- coding: utf-8 -*-
# 作者：籽怼
# QQ：2702114947
# 邮箱：ZiDuiMinecraft@outlook.com
# 版本：0.0.1


import wx
import wx.xrc
from Pack import AKForm


class mainForm(wx.App):
    def OnInit(self):
        self.SetAppName(u"AutoSkin")
        self.Frame = AKForm.MyFrame1(None)
        self.Frame.Show()
        return True


if __name__ == '__main__':
    Form = mainForm(redirect=True, filename="debug.txt")
    Form.MainLoop()
