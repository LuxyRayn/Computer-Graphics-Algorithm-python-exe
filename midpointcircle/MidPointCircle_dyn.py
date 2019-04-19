
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class image:
    def __init__(self):
        self.fig, self.ax = plt.subplots()  # 生成子图，相当于fig = plt.figure(),ax = fig.add_subplot(),其中ax的函数参数表示把当前画布进行分割，例：fig.add_subplot(2,2,2).表示将画布分割为两行两列
        self.dot, = self.ax.plot([], [], 'ro')
        self.xdata, self.ydata = [], []
        self.ln, = self.ax.plot([], [], 'r-', animated=False)
        self.pov = True

    def init(self):
        self.ax.set_xlim(0,150)
        self.ax.set_ylim(0,150)
        return self.ln

    def update_dot(self,newd):
        if self.line_or_point == 0:
            self.dot.set_data(newd[0], newd[1])
            plt.scatter(newd[0], newd[1],color = 'r')
            return self.dot
        else:
            self.xdata.append(newd[0])
            self.ydata.append(newd[1])
            self.ln.set_data(self.xdata, self.ydata)
            return self.ln

    def MPC(self,r):
        x = 0
        y = r
        d = 1.25 - r
        while x <= y:
            if d < 0:
                d += 2*x+3
            else:
                d += 2*(x-y)+5
                y -= 1
            x += 1
            li = [x,y]
            yield li


def trans(ra,line_point):
    r = ra
    cw = image()
    cw.line_or_point = line_point
    ani = FuncAnimation(cw.fig, cw.update_dot, frames=cw.MPC(r), interval=100, init_func=cw.init)
    plt.show()