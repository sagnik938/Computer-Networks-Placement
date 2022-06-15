#code for even parity
mat = []

def checkpar(sample):
    cnt = 0
    for s in sample:
        if( s == '1'):
            cnt+=1
    if(cnt%2 == 0):
        return('0')
    else:
        return('1')
    
def genpar(word):
    i = 0
    for letter in word:
        mat.append((str(bin(ord(letter)))[2:]))
        mat[i] = mat[i] + checkpar(mat[i])
        i+=1
    
    code = ""
    for i in range(8):
        t = ""
        for elem in mat:
            t += elem[i]
        code += checkpar(t)
    mat.append(code)
    print(mat)

genpar("HELLO")