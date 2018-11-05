import math

#Prints a transposition table for an affine cipher.
#a must be coprime to m=26.
darray = [-1 for i in range(26)]
msg = [3,20,17,14,17,12,13,18,6]

def affine(a, b):
  for i in range(26):
    #print(chr(i+65) + ": " + chr(((a*i+b)%26)+65))
    darray[i] = chr(((a*i+b)%26)+65)

def printmsg():
    for i in range(len(msg)):
        print(darray[msg[i]], end="")


for i in range(26):
    for k in range(26):
        if math.gcd(k,26) == 1:
            affine(k,i)
            print("a=", k, "b=", i)
            printmsg()
            print()


affine(21,0)
print("a= 21 b= 0")
printmsg()