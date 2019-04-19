# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from bresenham import Bresenham_dyn


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.x_start = wx.StaticText(self, wx.ID_ANY, u"x_start : (x > 0)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.x_start.Wrap(-1)
        gSizer2.Add(self.x_start, 0, wx.ALL, 5)

        self.x_start_fill = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.x_start_fill, 0, wx.ALL, 5)

        self.y_start = wx.StaticText(self, wx.ID_ANY, u"y_start : (y > 0)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.y_start.Wrap(-1)
        gSizer2.Add(self.y_start, 0, wx.ALL, 5)

        self.y_start_fill = wx.TextCtrl(self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.y_start_fill, 0, wx.ALL, 5)

        self.x_end = wx.StaticText(self, wx.ID_ANY, u"x_end : (x < 15)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.x_end.Wrap(-1)
        gSizer2.Add(self.x_end, 0, wx.ALL, 5)

        self.x_end_fill = wx.TextCtrl(self, wx.ID_ANY, u"15", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.x_end_fill, 0, wx.ALL, 5)

        self.y_end = wx.StaticText(self, wx.ID_ANY, u"y_end : (y < 10)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.y_end.Wrap(-1)
        gSizer2.Add(self.y_end, 0, wx.ALL, 5)

        self.y_end_fill = wx.TextCtrl(self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.y_end_fill, 0, wx.ALL, 5)

        self.ok = wx.Button(self, wx.ID_ANY, u"ok", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.ok, 0, wx.ALL, 5)

        self.SetSizer(gSizer2)
        self.Layout()
        gSizer2.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.ok.Bind(wx.EVT_BUTTON, self.Bresenham_f)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Bresenham_f(self, event):
        self.x1 = int(self.x_start_fill.GetValue())
        self.y1 = int(self.y_start_fill.GetValue())
        self.x2 = int(self.x_end_fill.GetValue())
        self.y2 = int(self.y_end_fill.GetValue())
        Bresenham_dyn.trans(self.x1, self.y1, self.x2, self.y2)
        self.Destroy()