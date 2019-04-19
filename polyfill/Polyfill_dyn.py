import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from polyfill import Polyfill多边形扫描转换

class image():
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.dot, = self.ax.plot([], [], 'ro')


    def init(self):
        self.ax.set_xlim(0,150)
        self.ax.set_ylim(0,150)
        return self.dot

    def update_dot(self,newd):
        self.dot.set_data(newd[0], newd[1])
        if newd[2] == 1:
            plt.scatter(newd[0], newd[1],color='r',s = 3)
        # plt.scatter(newd[0], newd[1], color='r', s=3)
        return self.dot

    def new_points(self,image_w,image_l,polygon,color,seg):
        all_point = Polyfill多边形扫描转换.PoliFill(image_w, image_l, polygon, color)

        for i in all_point:
            new_dot = i
            if new_dot[0]%5 == 0 and new_dot[1]%seg== 0:
                new_dot.append(1)
            else:
                new_dot.append(0)
            yield new_dot

    def plot_window(self,polygon):
        # 要连接的两个点的坐标
        draw_poly = []
        for i in polygon:
            draw_poly.append(i)
        draw_poly.append(polygon[0])
        for i in range(len(draw_poly) - 1):
            plt.plot([draw_poly[i][0], draw_poly[i + 1][0]], [draw_poly[i][1], draw_poly[i + 1][1]], 'g')
            plt.scatter([draw_poly[i][0], draw_poly[i + 1][0]], [draw_poly[i][1], draw_poly[i + 1][1]], color='b')



def trans(seg,color):
    image_l = 150
    image_w = 150
    # plt.axis([0, image_w, 0, image_l])
    cw = image()

    seg = seg
    color = color

    polygon = [
        [20, 20],
        [120, 20],
        [70, 100],
        [50, 80],
        [30, 120],
        [20, 50],
        [50, 50]
    ]

    cw.plot_window(polygon)

    ani = FuncAnimation(cw.fig, cw.update_dot, frames=cw.new_points(image_w, image_l, polygon,color, seg), interval=10,
                        init_func=cw.init)
    plt.show()
