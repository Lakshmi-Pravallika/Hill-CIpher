
print('HILL CIPHER')
print('------------------')
print('1.ENCRYPTION')
print('2.DECRYYPTION')
choice = int(input('Enter Your Choice:-'))
if(choice == 1):
    s = ''
    for i in range(65,91):
        s = s + chr(i)
    l = list(s)
    print('Enter Number of Rows:-')
    r = int(input())
    print('Enter Number of Columns:-')
    c = int(input())

    #DECLARING RXC MATRIX
    m = [[0 for j in range(0,c)] for i in range(0,r)]
    print("Enter Matrix / KEY Elements:")
    for i in range(0,r):
        for j in range(0,c):
            m[i][j] = int(input())

    #PRINTING MATRIX GIVEN WITH THEIR INDICES
    print('Entered Matrix with their indices')
    for i in range(r):
        for j in range(c):
            #print(m[i][j],'->',i,j)
            None
    #print(len(m))
    
    #INPUT STRING / MESSAGE
    string = input('Entered Message:-')
    
    string = string.replace(' ','')
    q = list(string.upper())

    if(len(q)%2!=0):
        q.append('X')
    else:
        None
    #print('Plaintext with their indices')
    for i in range(0,len(q)):
        if(q[i] in l):
            #print(q[i],'->',l.index(q[i]))
            None
    
    #PLAINTEXT INDEX'S
    m1 = []
    for i in range(0,len(q)):
        for j in range(0,len(l)):
            if(q[i] == l[j]):
                m1.append(j)

    #print((m1))
    
    #SLICING THE GIVEN TEXT INTO TWO CHAR'S AND THEIR CIPHERTEXT INDECES
    r = []
    for i in range(0,len(m1),2):
        t = []
        t.append(m1[i])
        t.append(m1[i+1])
        for j in range(0,2):
            s=0
            for k in range(0,2):
                s = s + (t[k] * m[k][j])
            r.append(s%26)
    #print(r)
    
    #CIPHERTEXT
    c = ''
    for i in range(0,len(r)):
        c = c + l[r[i]]
    print("CIPHERED TEXT:-",(c))        #CONSIDER SPACE AFTER BETWEEN 2 CHARACTERS

elif(choice == 2):
    s = ''
    for i in range(65,91):
        s = s + chr(i)
    l = list(s)
    ct = input("Enter Cipher Text:-")
    lct = list(ct.upper())
    print('Enter Number of Rows:-')
    r = int(input())
    print('Enter Number of Columns:-')
    c = int(input())
    
    #DECLARING RXC MATRIX
    m = [[0 for j in range(0,c)] for i in range(0,r)]
    print("Enter Matrix / KEY Elements:")
    for i in range(0,r):
        for j in range(0,c):
            m[i][j] = int(input())
    
    #PRINTING MATRIX GIVEN WITH THEIR INDICES
    print('Entered Matrix with their indices')
    for i in range(r):
        for j in range(c):
            #print(m[i][j],'->',i,j)
            None
    
    det = (m[0][0]*m[1][1]) - (m[0][1]*m[1][0])
    inv = 0
    for i in range(1,det):
        if(det*i%26==1):
            #print(i)
            inv = i
    print('Inverse Mod:-',inv)
    temp = m[0][0]
    for i in range(0,2):
        for j in range(0,2):
            if(i!=j):
                m[i][j] = m[i][j] - (2*m[i][j])
            else:
                if(i == 0):
                    m[i][j] = m[1][1]
                elif(i == 1):
                    m[i][j] = temp
    #print(m)
    for i in range(0,2):
        for j in range(0,2):
            if(m[i][j]<0):
                m[i][j] = m[i][j] + 26
    #print(m)
    
    for i in range(0,2):
        for j in range(0,2):
            m[i][j] = m[i][j]*inv%26
            #print(m[i][j],'->',i,j)
            None
    #print(m)
    if(len(lct)%2!=0):
        lct.append('X')
    else:
        None
    
    for i in range(0,len(lct)):
        if(lct[i] in l):
            #print(lct[i],'->',l.index(lct[i]))
            None
    m1 = []
    for i in range(0,len(lct)):
        for j in range(0,len(l)):
            if(lct[i] == l[j]):
                m1.append(j)
    r = []
    for i in range(0,len(lct),2):
        t = []
        t.append(m1[i])
        t.append(m1[i+1])
        for j in range(0,2):
            s=0
            for k in range(0,2):
                s = s + (t[k] * m[k][j])
            r.append(s%26)
    
    print('DeCiphered Text:-')
    for i in range(len(r)):
        print(l[r[i]],end='')
