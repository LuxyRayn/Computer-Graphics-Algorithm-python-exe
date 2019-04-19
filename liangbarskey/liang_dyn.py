import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


polygon = [[20, 20], [120, 20], [70, 100], [50, 80], [30, 120], [20, 50], [50, 50], [20, 20]]

class image():
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.xdatar, self.ydatar = [], []
        self.lnr, = self.ax.plot([], [], 'r-')
        self.xdatal, self.ydatal = [], []
        self.lnl, = self.ax.plot([], [], 'r-')
        self.xdatab, self.ydatab = [], []
        self.lnb, = self.ax.plot([], [], 'r-')
        self.xdatat, self.ydatat = [], []
        self.lnt, = self.ax.plot([], [], 'r-')

    def plot_line(self,x1,x2,y1,y2,wxl,wxr,wyb,wyt):
        plt.plot([x1,x2],[y1,y2],'g')
        plt.scatter([x1, x2], [y1, y2], color='b')

        p1 = -(x2 - x1)
        q1 = x1 - wxl
        p2 = x2 - x1
        q2 = wxr - x1
        p3 = -(y2 - y1)
        q3 = y1 - wyb
        p4 = y2 - y1
        q4 = wyt - y1

        ymax = max(y1,y2)
        ymin = min(y1,y2)

        if p1 == 0 and p2 == 0:  # 算法过程2
            if q1 > 0 and q2 > 0:
                if ymin >= wyb and ymax <= wyt:  # 两端点都在窗口内
                    plt.plot([x1, x2], [ymin, ymax], 'm')
                elif ymin < wyb and ymax <= wyt:
                    plt.plot([x1, x2], [wyb, ymax], 'm')  # 一个端点在窗口内
                elif ymin >= wyb and ymax > wyt:
                    plt.plot([x1, x2], [ymin, wyt], 'm')  # 一个端点在窗口内
                else:
                    plt.plot([x1, x2], [wyb, wyt], 'm')  # 端点都不在窗口内

        elif p3 == 0 and p4 == 0:  # 算法过程3
            if q3 > 0 and q4 > 0:
                if x1 >= wxl and x2 <= wxr:  # 两端点都在窗口内
                    plt.plot([x1, x2], [y1, y2], 'm')
                elif x1 < wxl and x2 <= wxr:
                    plt.plot([wxl, x2], [y1, y2], 'm')  # 一个端点在窗口内
                elif wxl >= x1 and x2 > wxr:
                    plt.plot([x1, wxr], [y1, y2], 'm')  # 一个端点在窗口内
                else:
                    plt.plot([wxl, wxr], [y1, y2], 'm')  # 端点都不在窗口内


        else:  # 算法过程45
            ul = 0
            ur = 1
            for e in [[p1, q1], [p2, q2], [p3, q3], [p4, q4]]:
                if e[0] < 0:
                    ul = max(ul, e[1] / e[0])
                else:
                    ur = min(ur, e[1] / e[0])
            # 判断线代落在窗口内与否
            if ul < ur:
                plt.plot([x1 + ul * p2, x1 + ur * p2], [y1 + ul * p4, y1 + ur * p4], 'm')


    def init(self):
        self.ax.set_xlim(0,150)
        self.ax.set_ylim(0,150)
        return self.lnr,self.lnl,self.lnb,self.lnt

    def update_dot(self,window):
        win = window[4]

        xdatar = window[0][0]
        ydatar = window[0][1]

        xdatal = window[1][0]
        ydatal = window[1][1]

        xdatab = window[2][0]
        ydatab = window[2][1]

        xdatat = window[3][0]
        ydatat = window[3][1]

        self.lnr.set_data(xdatar, ydatar)
        self.lnl.set_data(xdatal, ydatal)
        self.lnb.set_data(xdatab, ydatab)
        self.lnt.set_data(xdatat, ydatat)

        for i in range(len(polygon) - 1):
            self.plot_line(polygon[i][0], polygon[i+1][0],polygon[i][1], polygon[i+1][1], win[0], win[1], win[2], win[3])

        return self.lnr,self.lnl,self.lnb,self.lnt

    def get_window(self,xmax,ymax):
        xl = int(xmax/2)
        yb = int(ymax/2)
        xr = int(xmax / 2)
        yt = int(ymax / 2)
        while xl > 0 and xr < xmax and yb > 0 and yt < ymax :
            xl -= 1
            xr += 1
            yb -= 1
            yt += 1
            lnr = [[xr for i in range(yt - yb + 1)], [i for i in range(yb, yt + 1)]]
            lnl = [[xl for i in range(yt - yb + 1)], [i for i in range(yb, yt + 1)]]
            lnb = [[i for i in range(xl, xr + 1)], [yb for i in range(xr - xl + 1)]]
            lnt = [[i for i in range(xl, xr + 1)], [yt for i in range(xr - xl + 1)]]
            line_4 = [xl,xr,yb,yt]
            yield lnr,lnl,lnb,lnt,line_4


def trans(speed):
    image_l = 150
    image_w = 150

    speed = speed
    # plt.axis([0, image_w, 0, image_l])
    cw = image()
    ani = FuncAnimation(cw.fig, cw.update_dot, frames=cw.get_window(image_w, image_l), interval=speed, init_func=cw.init)
    plt.show()
