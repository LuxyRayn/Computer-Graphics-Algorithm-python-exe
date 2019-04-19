# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from midpointcircle import MidPointCircle_dyn

###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.Radius = wx.StaticText(self, wx.ID_ANY, u"Radius : (r < 150)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Radius.Wrap(-1)
        gSizer2.Add(self.Radius, 0, wx.ALL, 5)

        self.radius_fill = wx.TextCtrl(self, wx.ID_ANY, u"30", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.radius_fill, 0, wx.ALL, 5)

        point_or_lineChoices = [u"点显示", u"线显示"]
        self.point_or_line = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, point_or_lineChoices, 0)
        self.point_or_line.SetSelection(0)
        gSizer2.Add(self.point_or_line, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.m_button8, 0, wx.ALL, 5)

        self.SetSizer(gSizer2)
        self.Layout()
        gSizer2.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.point_or_line.Bind(wx.EVT_CHOICE, self.set_point_line)
        self.m_button8.Bind(wx.EVT_BUTTON, self.mpc_f)

    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def set_point_line(self, event):
        event.Skip()

    def mpc_f(self, event):
        self.r = int(self.radius_fill.GetValue())
        MidPointCircle_dyn.trans(self.r, int(self.point_or_line.GetSelection()))
        self.Destroy()