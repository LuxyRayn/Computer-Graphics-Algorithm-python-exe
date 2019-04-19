# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
# from ui import bresenham_dialog
###########################################################################
## Class main
###########################################################################

class main(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.Bresenham = wx.Button(self, wx.ID_ANY, u"Bresenham", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.Bresenham, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.LiangBarskey = wx.Button(self, wx.ID_ANY, u"Liang-Barskey", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.LiangBarskey, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.MidPointCircle = wx.Button(self, wx.ID_ANY, u"MidPointCircle", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.MidPointCircle, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.多边形扫描填充 = wx.Button(self, wx.ID_ANY, u"多边形扫描填充", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.多边形扫描填充, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.中点画线 = wx.Button(self, wx.ID_ANY, u"zhongdian", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.中点画线, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Bezier = wx.Button(self, wx.ID_ANY, u"Bezier", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer1.Add(self.Bezier, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bresenham.Bind(wx.EVT_BUTTON, self.Bresenham_input)
        self.LiangBarskey.Bind(wx.EVT_BUTTON, self.LiangBarskey_input)
        self.MidPointCircle.Bind(wx.EVT_BUTTON, self.midpointcicle_input)
        self.多边形扫描填充.Bind(wx.EVT_BUTTON, self.polyfill_f)
        self.中点画线.Bind(wx.EVT_BUTTON, self.zhongdian_input)
        self.Bezier.Bind(wx.EVT_BUTTON, self.Bezier_f)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Bresenham_input(self, event):
        event.Skip()

    def LiangBarskey_input(self, event):
        event.Skip()

    def midpointcicle_input(self, event):
        event.Skip()

    def polyfill_f(self, event):
        event.Skip()

    def zhongdian_input(self, event):
        event.Skip()

    def Bezier_f(self, event):
        event.Skip()




