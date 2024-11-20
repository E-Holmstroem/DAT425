def transpose(matrixOld):
    if matrixOld == []:
      return []
    matrixNew = []
    for rows in range(0,len(matrixOld[0])):                     #lägg till så många rader i ny matris som det finns kolumner i gammal matris. Dock tomma
        matrixNew.append([])                                   
        for columns in range(0,len(matrixOld)):                 #i varje rad i ny matris, lägg till så måmga element som det finns rader i gammal matris.
          matrixNew[rows].append(matrixOld[columns][rows])      #sätt värdet från rad:kolumn från gammal matris till kolumn:rad i ny matris.
    return matrixNew

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

def matmul(matrix1, matrix2):
  matrixNew = []
  matrix2 = transpose(matrix2)
  for rows1 in range(0,len(matrix1)):
    matrixNew.append([])
    for rows2 in range(0, len(matrix2)):
      sum = 0
      for columns in range(0, len(matrix2[0])):
        sum = sum + matrix1[rows1][columns]*matrix2[rows2][columns]
      matrixNew[rows1].append(sum)
  return matrixNew

def invert(matrix):
   det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
   return [[matrix[1][1]/det,-1*matrix[0][1]/det],[-1*matrix[1][0]/det,matrix[0][0]/det]]

def loadtxt(file):
    matrixRet = []
    lines = open(file, encoding="utf-8")
    for line in lines:  
      matrixTemp = []                                                                                 
      start = 0
      while start < (len(line)):                                
        end = start                                               
        if line[start].isspace() == True or line[start].isalpha() == True:                         
          start = start+1
        elif line[end].isdigit() == True or line[end] == ".":
          end = start
          while end < len(line) and (line[end].isdigit() == True or line[end] == "."):
            end = end + 1
          matrixTemp.append(float(line[start:end]))
          start = end
      matrixRet.append(matrixTemp)
    return matrixRet