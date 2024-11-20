def tokenize(lines):
    words = []
    for line in lines:                                                                                    
      start = 0
      while start < (len(line)):                                  #loops until start index is the last position of the string
        end = start                                               
        if line[start].isspace():                         #if current position in string is space, then move to next
          start = start+1
        elif line[start].isalpha():                       #if current position in string is character, 
          end = start                                             
          while end < len(line) and line[end].isalpha():  #then check the next until it is not or the string ends.
            end = end + 1
          words.append((line[start:end]).lower())    #put .lower() here because words are appended to the list.       #Start and end now marks the length and pos of the "word" in the string, add to the list
          start = end                                             #Start pos for next word in string
        elif line[end].isdigit():
          end = start
          while end < len(line) and line[end].isdigit():
            end = end + 1
          words.append(line[start:end])  #digits don't need .lower()
          start = end
        else:                           #same goes for special characters
          words.append(line[start])
          start = start + 1
    return words

#The code below hasn't been changed since last submission
def countWords(txt,exception):
    li = tokenize(txt) #Gör om orden i listan till tokens
    sli = tokenize(exception)
    dict = {}
    for word in li:   
        if word in sli: #Om ordet är ett undantag 
            pass
        elif word in dict: #Om ordet redan finns i dictionary
            dict[word] +=1
        else: #Om det är ett nytt ord
            dict.setdefault(word, 1)
    return dict


def printTopMost(dict, placement):
    li=[]
    for word,num in dict.items(): li.append((word,num))
    li = sorted(li, key=lambda x: -x[1]) #Sortera allt som desc
    con=0
    for x,y in li:
        if con < int(placement): print(x.ljust(20)+str(y).rjust(5))
        con+=1