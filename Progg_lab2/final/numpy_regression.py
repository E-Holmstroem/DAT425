import sys
from numpy import *
import matplotlib.pyplot as plt

degree = int(sys.argv[2])

def poly(a : list, x : float) -> int:
    num : int = 0
    for n in range(0,int(degree)+1):
        num += a[n]*x**n
    return num

def powers(list,n1,n2):
    matrixNew = []
    for rows in range(0,len(list)):                     
        count = n1 
        matrixNew.append([])                                   
        for columns in range(0,((n2-n1)+1)):        
          matrixNew[rows].append(list[rows])
          matrixNew[rows][columns] = matrixNew[rows][columns]**count
          if count <= n2:
            count = count + 1
    return matrixNew

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