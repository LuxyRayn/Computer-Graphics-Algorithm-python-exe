# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from polyfill import Polyfill_dyn

###########################################################################
## Class MyDialog3
###########################################################################

class MyDialog3(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer3 = wx.GridSizer(0, 2, 0, 0)

        self.color_speed = wx.StaticText(self, wx.ID_ANY, u"上色刷新速度（每n行）：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.color_speed.Wrap(-1)
        gSizer3.Add(self.color_speed, 0, wx.ALL, 5)

        self.speed = wx.TextCtrl(self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.speed, 0, wx.ALL, 5)

        self.color = wx.CheckBox(self, wx.ID_ANY, u"背景是否预先上色(不建议选择 速度慢)", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.color, 0, wx.ALL, 5)

        self.OK = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer3.Add(self.OK, 0, wx.ALL, 5)

        self.SetSizer(gSizer3)
        self.Layout()
        gSizer3.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.OK.Bind(wx.EVT_BUTTON, self.polyfill_f)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def polyfill_f(self, event):
        self.seg = int(self.speed.GetValue())
        Polyfill_dyn.trans(self.seg, self.color.GetValue())
        self.Destroy()

