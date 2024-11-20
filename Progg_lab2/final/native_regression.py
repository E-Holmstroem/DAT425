import sys
from matrix import *
import matplotlib.pyplot as plt

def main():
    data = loadtxt(sys.argv[1])
    
    data_transposed = transpose(data)
    X = data_transposed[0]
    Y = data_transposed[1]
    
    Xp = powers(X, 0, 1)
    Yp = powers(Y, 1, 1)

    Xpt = transpose(Xp)
    XtX = matmul(Xpt, Xp)
    XtY = matmul(Xpt, Yp)

    [[b], [m]] = matmul(invert(XtX), XtY)
    
    plt.plot(X, [b + m * x for x in X]) #For loop räknar ut varje y värde för alla x i listan X enligt linjär ekvation
    plt.plot(X,Y,'ro') #Plottar alla givna punkter den linjära funktionen är baserad på
    plt.show()
    
main()