import matplotlib.pyplot as plt

def Bresenham(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    e = -dx

    x = x1
    y = y1

    for i in range(dx+1):
        plt.scatter(x, y, color='b')
        x += 1
        e = e + 2*dy
        if e >= 0:
            y += 1
            e = e-2*dx


if __name__ == '__main__':

    plt.axis([0,150,0,150])

    line = [[40,40],[100,100]]

    Bresenham(line[0][0], line[0][1], line[1][0], line[1][1])

    plt.show()