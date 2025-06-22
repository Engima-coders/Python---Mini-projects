import random
c=[1,2,3]
s=''
p=0
print("Welcome to Rock Paper Scissor")
while True:
    com_ch=random.choice(c)
    user_ch=int(input("Enter your choice 1->Rock 2->Scissor 3->Paper"))
    if user_ch>=4 or user_ch<1:
        continue
    if com_ch==user_ch:
        
        print("TIE")
    elif com_ch==3 and user_ch==1:
        
        print("YOU LOOSE")
    elif user_ch==3 and com_ch==1:
        
        print("YOU WIN")
        p+=1
    elif user_ch<com_ch:
        
        print("YOU WIN")
        p+=1
    elif com_ch<user_ch:
        
        print('YOU LOOSE')
    s=input("If u want to exit then type 'E' else type 'C'")
    if s=='e' or s=='E':
        break
print("Thank you!")
print("Your Score is",p)
    

