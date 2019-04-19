
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class image():
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.dot, = self.ax.plot([], [], 'ro')

    def init(self):
        self.ax.set_xlim(0,50)
        self.ax.set_ylim(0,30)
        dot, = self.ax.plot([], [], 'ro')
        return dot

    def update_dot(self,newd):

        self.dot.set_data(newd[0], newd[1])
        plt.scatter(newd[0], newd[1],color='r')
        return self.dot,

    def MPline(self,x,y,d,d1,d2,x2):
        while (x < x2):
            if d < 0:
                x += 1
                y += 1
                d += d2
            else:
                x += 1
                d += d1
            newdot = [x,y]
            yield newdot



def trans(x1, y1, x2, y2):
    x1, y1, x2, y2 = x1, y1, x2, y2

    cw = image()
    x = [x1, x2]
    y = [y1, y2]
    cw.ax.plot(x, y)

    a = y1 - y2
    b = x2 - x1
    y = y1
    x = x1
    d = 2 * a + b
    d1 = 2 * a
    d2 = 2 * (a + b)


    ani = FuncAnimation(cw.fig, cw.update_dot, frames=cw.MPline(x, y, d, d1, d2,x2), interval=400, init_func=cw.init)
    plt.show()
