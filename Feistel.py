

sbox = [6, 7, 8, 9, 'A' ,'B', 'C', 'D', 'E', 'F', 0, 1, 2, 3, 4, 5]
proccess = list()
Onekey = ""
#Split the value hexa
def halves(Text):
    half, rem = divmod(len(Text), 2)
    tungaNa = [Text[:half + rem],Text[half + rem:]]
    return tungaNa

#EXOR operations
def EXOR(a, b):
    num_a = int(a, 2)
    num_b = int(b, 2)
    result = num_a ^ num_b
    return bin(result)[2:].zfill(8)

#convertHexaTobinary
def hexaTobinary(str,bits):
    binary = bits.format(int(str, 16))

    if(len(binary) <= 16 ):
        for i in range(len(binary)-16):
            binary = '0'+binary
            print("mark",binary)
    return binary

#sboxValue
def sboxValue(binary):
    decimal = int(binary, 2)
    return hexaTobinary(str(sbox[int(decimal)]),"{0:04b}")

#Binary to hexa
def bintohexa(n):
    bi = int(n, 2)
    hex = format(bi, 'x')
    return(hex)


#calculate for Ri
def functRi(Li_1,ki,Ri_1):
    temp = EXOR(Ri_1,ki)
    proccess.append(("= F(%s)find the sbox value"%(temp)))
    print("= F(%s)find the sbox value"%(temp))
    h = halves(str(temp))
    proccess.append(("= %s-> %s"%(h[0],sboxValue(h[0]))))
    proccess.append(("= %s-> %s"%(h[1],sboxValue(h[1]))))
    print("= %s-> %s\n= %s-> %s"%(h[0],sboxValue(h[0]),h[1],sboxValue(h[1])))
    sBoxResult = sboxValue(h[0])+sboxValue(h[1])
    ri = EXOR(sBoxResult,Li_1)
    proccess.append(("= Li-1 ^ F(%s)"%(sBoxResult)))
    proccess.append(("= %s"%(sBoxResult)))
    print("= Li-1 ^ F(%s)\n= %s"%(sBoxResult,ri))
    return ri
   
  
def roundsDES(test, key, numberOfrounds):
    print("Calculate Li = Ri-1.\nCalculate Ri = Li-1 ^ F(Ri-1, Ki)")
    k2=hexaTobinary(halves(key)[1],"{0:08b}")
    k1=hexaTobinary(halves(key)[0],"{0:08b}")
    ri=hexaTobinary(halves(test)[1],"{0:08b}")
    li=hexaTobinary(halves(test)[0],"{0:08b}")
    if(int(numberOfrounds)%2!=0):
        for x in range(int(numberOfrounds)):
            ki = hexaTobinary(halves(key)[int(x%2)],"{0:08b}")
            proccess.append(("______________________________Round: %d"% (x+1)))
            proccess.append(("k%d: %s"%(x+1,ki)))
            
            #print("______________________________\nRound:", x+1)
            #print("k%d: %s"%(x+1,ki))
            #print("l%d = %s"% (x+1, ri))
            #print("r%d= %s^F(%s,%s)" %(x+1, li,ri,ki))
            temp = functRi(li,ki,ri)
            li = ri
            ri = temp
            proccess.append(("l%d:%s                 r%d:%s"%(x+1,li,x+1,ri)))
            print("l%d:%s\t\tr%d:%s"%(x+1,li,x+1,ri))
            
        
    else:
        for x in range(int(numberOfrounds)):
             if(x%2==0):
                proccess.append(("______________________________Round: %d"% (x+1)))
                proccess.append(("k%d: %s"%(x+1,k1)))
                #print("______________________________\nRound:", x+1)
                #print("l%d = %s"% (x+1, ri))
                #print("r%d= %s^F(%s,%s)" %(x+1, li,ri,k1))
                temp = functRi(li,k1,ri)
                li = ri
                ri = temp
                proccess.append(("l%d:%s                 r%d:%s"%(x+1,li,x+1,ri)))
                #print("l%d:%s\t\tr%d:%s"%(x+1,li,x+1,ri)) 
            
             else:
                proccess.append(("______________________________Round: %d"% (x+1)))
                proccess.append(("k%d: %s"%(x+1,k2)))
                #print("______________________________\nRound:", x+1)
                #print("l%d = %s"% (x+1, ri))
                #print("r%d= %s^F(%s,%s)" %(x+1, li,ri,k1))
                temp = functRi(li,k1,ri)
                li = ri
                ri = temp
                proccess.append(("l%d:%s                 r%d:%s"%(x+1,li,x+1,ri)))
                #print("l%d:%s\t\tr%d:%s"%(x+1,li,x+1,ri))
    Onekey = ("Key: %s | %s"%(hexaTobinary(key,"{0:016b}"), key))
    word = ri+li
    print("\nText/Cipher: %s | %s"%(word,bintohexa(word)))
    return "\nText/Cipher: %s | %s"%(word,bintohexa(word))
   



