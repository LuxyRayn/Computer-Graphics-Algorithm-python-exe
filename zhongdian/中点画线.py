import matplotlib.pyplot as plt


def MPline(x1,y1,x2,y2):
    a = y1 - y2
    b = x2 - x1
    y = y1
    x = x1
    d = 2*a + b
    d1 = 2*a
    d2 = 2*(a+b)

    plt.scatter(x, y, color='b')
    while(x<x2):
        if d < 0:
            x += 1
            y += 1
            d += d2
        else:
            x += 1
            d += d1
        plt.scatter(x, y, color='b')


if __name__ == '__main__':

    plt.axis([0,150,0,150])
    

    line = [[40,40],[100,100]]

    MPline(line[0][0], line[0][1], line[1][0], line[1][1])

    plt.show()