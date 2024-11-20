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

def transpose(matrix):
    mallMatrix = mat(col(matrix), row(matrix))
    for i in range(0, row(matrix)):
        for n in range(0, col(matrix)):
            mallMatrix[n][i] = matrix[i][n]
    return mallMatrix

def powers(li, low, high):
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
    return matrix

def matmul(mat1, mat2): #kan möjligtvis göra en matris med mat() istället och sedan lösa, men rn funkar detta bra
    inner_li = []
    li = []
    con=0
    tmat2 = transpose(mat2)
    
    for mat1_row in range(0, row(mat1)): 
        for tmat2_row in range(0, row(tmat2)): 
            for column in range(0, col(tmat2)):
                con += (mat1[mat1_row][column] * tmat2[tmat2_row][column])
            inner_li.append(con)
            con=0
        li.append(inner_li)
        inner_li = []
    return li

def invert(mat):
    det = (mat[0][0] * mat[1][1]) - (mat[1][0] * mat[0][1])
    return [[mat[1][1]/det, -mat[0][1]/det],[-mat[1][0]/det, mat[0][0]/det]]

def loadtxt(text):
    li = []
    txtF = open(text, encoding="utf-8")
    for line in txtF:
        li.append([float(x) for x in line.strip().split()])
    return li

