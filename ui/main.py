import wx
from ui import main_ui
from ui import bresenham_dialog
from ui import midpointcircle_dialog
from bezier import Bezier_dyn
from ui import polyfill_dialog
from ui import liang_dialog
from ui import zhongdian_dialog

class MyApp(wx.App):
    def OnInit(self):
        self.frame = mainForm(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


class mainForm(main_ui.main):
    def __init__(self,parent):
        main_ui.main.__init__(self, parent)

    def polyfill_f(self, event):
        self.frame = polyfill_dialog.MyDialog3(None)
        self.frame.Show()

    def Bresenham_input(self, event):
        self.frame = bresenham_dialog.MyDialog1(None)
        self.frame.Show()

    def midpointcicle_input(self, event):
        self.frame = midpointcircle_dialog.MyDialog2(None)
        self.frame.Show()

    def Bezier_f(self, event):
        Bezier_dyn.trans()

    def LiangBarskey_input(self, event):
        self.frame = liang_dialog.MyDialog4(None)
        self.frame.Show()

    def zhongdian_input(self, event):
        self.frame = zhongdian_dialog.MyDialog5(None)
        self.frame.Show()

if __name__ == '__main__':
    app = MyApp(False)
    # 主循环
    app.MainLoop()
