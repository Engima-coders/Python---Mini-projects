import random
import string
num=['1','2','3','4','5','6','7','9','8','0']
sym=['*','+','/','-',',','&','^','$','%','#','@','!']
print('Welcome to Password Generator')
nl=int(input('How many letters you want in your password?'))
nn=int(input('How many numbers you want in your password?'))
ns=int(input('How many symbols you want in your password?'))
pw=[]
for i in range(0,nn):
    c=random.choice(num)
    pw.append(c)
for i in range(0,ns):
    c=random.choice(sym)
    pw.append(c)
for i in range(0,nl):
    c=random.choice(string.ascii_letters)
    pw.append(c)
random.shuffle(pw)
pw2=''.join(pw)
print (pw2)
print ('Thank You!')