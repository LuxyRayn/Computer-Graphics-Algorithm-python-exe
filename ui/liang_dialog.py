import wx
import wx.xrc
from liangbarskey import liang_dyn

class MyDialog4(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer4 = wx.GridSizer(0, 2, 0, 0)

        self.speed = wx.StaticText(self, wx.ID_ANY, u"扩散速度 （10的倍数 < 1000）", wx.DefaultPosition, wx.DefaultSize, 0)
        self.speed.Wrap(-1)
        gSizer4.Add(self.speed, 0, wx.ALL, 5)

        self.speed_fill = wx.TextCtrl(self, wx.ID_ANY, u"50", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.speed_fill, 0, wx.ALL, 5)

        self.OK = wx.Button(self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer4.Add(self.OK, 0, wx.ALL, 5)

        self.SetSizer(gSizer4)
        self.Layout()
        gSizer4.Fit(self)

        self.Centre(wx.BOTH)

        # Connect Events
        self.OK.Bind(wx.EVT_BUTTON, self.liang_f)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def liang_f(self, event):
        liang_dyn.trans(int(self.speed_fill.GetValue()))
        self.Destroy()
