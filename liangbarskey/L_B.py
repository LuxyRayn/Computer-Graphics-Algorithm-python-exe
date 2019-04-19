import matplotlib.pyplot as plt
import numpy as np

def plot_window(wxl,wxr,wyb,wyt):
    # 要连接的两个点的坐标
    x = [[wxl,wxr],[wxr,wxr],[wxr,wxl],[wxl,wxl]]
    y = [[wyb,wyb],[wyb,wyt],[wyt,wyt],[wyt,wyb]]
    for i in range(len(x)):
        plt.plot(x[i], y[i], color='r')

def plot_line(x1,x2,y1,y2,wxl,wxr,wyb,wyt):
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


if __name__ == '__main__':

    plt.axis([0,150,0,150])

    window = [40,100,40,100]
    polygon = [[20,20],[120,20],[70,100],[50, 80],[30, 120],[20, 50],[50, 50],[20,20]]

    plot_window(window[0],window[1],window[2],window[3])

    for i in range(len(polygon)-1):
        plot_line(polygon[i][0], polygon[i+1][0],polygon[i][1], polygon[i+1][1],window[0],window[1],window[2],window[3])

    plt.show()