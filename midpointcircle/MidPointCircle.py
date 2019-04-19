import matplotlib.pyplot as plt

#d = F（xi + 1, yi – 0.5）= (xi + 1)2 + (yi – 0.5)2 – R2

def MPC(r):
    x = 0
    y = r
    d = 1.25 - r
    # 特别的，在第一个象限的第一个点（0, R）时，可以推倒出判别式d的初始值d0：
    # d0 = F(1, R – 0.5) = 1 – (R – 0.5)
    # 2 – R2 = 1.25 - R

    plt.scatter(x, y, color='b')
    while x <= y:
        if d < 0:
            d += 2*x+3
        # 若d < 0，则取P1为下一个点，此时P1的下一个点的判别式为：
        # d’ = F（xi + 2, yi – 0.5）= (xi + 2)2 + (yi – 0.5)2 – R2
        # 展开后将d带入可得到判别式的递推关系：
        # d’ = d + 2xi + 3
        else:
            d += 2*(x-y)+5
            y -= 1
        # 若d > 0，则取P2为下一个点，此时P2的下一个点的判别式为：
        # d’ = F（xi + 2, yi – 1.5）= (xi + 2)2 + (yi – 1.5)2 – R2
        # 展开后将d带入可得到判别式的递推关系：
        # d’ = d + 2(xi - yi) + 5
        x += 1
        plt.scatter(x, y, color='b')


if __name__ == '__main__':

    plt.axis([0,150,0,150])

    MPC(150)

    plt.show()