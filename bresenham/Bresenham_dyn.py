
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class image:
    def __init__(self):
        self.fig, self.ax = plt.subplots()  # 生成子图，相当于fig = plt.figure(),ax = fig.add_subplot(),其中ax的函数参数表示把当前画布进行分割，例：fig.add_subplot(2,2,2).表示将画布分割为两行两列
        self.dot, = self.ax.plot([], [], 'ro')



    def init(self):
        self.ax.set_xlim(0,15)
        self.ax.set_ylim(0,10)
        return self.dot

    def update_dot(self,newd):
        self.dot.set_data(newd[0], newd[1])
        plt.scatter(newd[0], newd[1],color='r')
        return self.dot

    def Bresenham(self,x,y,dx,dy,e):
        for i in range(dx+1):
            li = [x,y]
            yield li
            x += 1
            e = e + 2*dy
            if e >= 0:
                y += 1
                e = e-2*dx


def trans(x1,y1,x2,y2):
    x1, y1, x2, y2 = x1,y1,x2,y2
    cw = image()

    x = [x1, x2]
    y = [y1, y2]
    plt.plot(x, y)

    dx = x2 - x1
    dy = y2 - y1
    e = -dx

    x = x1
    y = y1

    ani = FuncAnimation(cw.fig, cw.update_dot, frames=cw.Bresenham(x, y, dx, dy, e), interval=1000, init_func=cw.init)
    plt.show()
