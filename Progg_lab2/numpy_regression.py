import sys
from numpy import *
import matplotlib.pyplot as plt

degree = sys.argv[2]

def col(matrix):
    if row(matrix) != 0:
        return len(matrix[0])    
    return 0

def row(matrix):
    return len(matrix)

def mat(r,c):
    mat = []
    for i in range(0,r):
        mat.append([0]*c)
    return mat

def powers(li, low, high):
    low = int(low)
    high = int(high)
    if high < low:
        return [[]] #osäker om detta är en laglig lösning. men om den är det så funkar allt susen.
    matrix = mat(row(li), abs(high-low)+1)
    con=0
    for i in range(0, row(li)):
        cun=0
        for n in range(low,high+1):
            matrix[con][cun] = li[con]**n  
            cun+=1
        con+=1
    return array(matrix)

def poly(a : list, x : float) -> int:
    num : int = 0
    for n in range(0,int(degree)+1):
        num += a[n]*x**n
    return num

def main():
    data = loadtxt(sys.argv[1])
    
    data_transposed = transpose(data)
    X = data_transposed[0]
    Y = data_transposed[1]
    
    Xp = powers(X, 0, degree)
    Yp = powers(Y, 1, 1)

    Xpt = transpose(Xp)
    XtX = matmul(Xpt, Xp)
    XtY = matmul(Xpt, Yp)

    a = matmul(linalg.inv(XtX), XtY)
    a = a[:,0]

    Xmin = min(X)
    Xmax = max(X)

    X2 = linspace(Xmin,Xmax,int((Xmax-Xmin)/0.2)).tolist()
    
    plt.plot(X2, [poly(a,x) for x in X2]) #Visar den linjära ekv b + m * x där x är temperatur
    plt.plot(X,Y,'ro') #Visar alla punkter den linjära funktionen är baserad på
    plt.show()
    
main()