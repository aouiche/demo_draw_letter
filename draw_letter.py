def draw_letter(letters):
    A=[[0,2,0,2,2],[4,2,4,2,2]]
    B=[[0,2,0,2,0],[3,2,3,2,3]]
    C=[[0,0,0,0,0],[3,1,1,1,3]]
    D=[[0,2,2,2,0],[3,2,2,2,3]]
    E=[[0,2,0,2,0],[3,1,3,1,3]]
    F=[[0,2,0,2,0],[3,1,3,1,1]]  
    length = len(letters)
    i0 = [0]*length
    i1 = [0]*length
    j = [0]*length 
    
    for l in range(0,length):
        i1[l],j[l] = eval(letters[l])
        
  
    print()
    for k in range(0,5) :
        x = " "*4+("*"+" "*i1[0][k])*j[0][k]
        if length != 1 :
             for l in range(1,length):
                if  i1[l-1][k] == 0:
                    
                    if j[l-1][k] == 1:
                            x += " "*3+(" "*5+("*"+" "*i1[l][k])*j[l][k])
                    elif  j[l-1][k] == 2:
                        x += " "*3+(" "*3+("*"+" "*i1[l][k])*j[l][k])       
                    elif j[l-1][k] == 3:
                        x += " "*2+(" "*4+("*"+" "*i1[l][k])*j[l][k])
                    else:
                        x += " "*3+(" "*2+("*"+" "*i1[l][k])*j[l][k])
                else:
                    if j[l-1][k] == 1:
                            x += " "*3+(" "*3+("*"+" "*i1[l][k])*j[l][k])
                    elif j[l-1][k] == 2:
                            x += " "*2+(" "+("*"+" "*i1[l][k])*j[l][k])
                    elif j[l-1][k] == 3:
                            x += " "*2+("*"+" "*i1[l][k])*j[l][k]
                    else:
                        x += " "*3+("*"+" "*i1[l][k])*j[l][k]
        print (x)
  
        
draw_letter(input("Enter your letter(from A ---> F) : "))

