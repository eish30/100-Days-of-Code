from random import randint
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['0','1','2','3','4','5','6','7','8','9']
symb = ['!',"#",'$','%','&','(',')','*','+']
ran = [letters,num,symb]
print("Welcome to Password Generator!")
nletters = int(input("How many letters would you like in your password? "))
nsymb = int(input("How many symbols would you like? "))
nnum = int(input("How many numbers would you like? "))
password = ''
for i in range(0,nletters+nsymb+nnum):
    n1 = randint(0,2)
    if n1==0:
        if nletters!=0:
            password += letters[randint(0,55)]
            nletters -= 1
    if n1==1:
        if nsymb!=0:
            password += symb[randint(0,8)]
            nsymb -= 1
    if n1==2:
        if nnum!=0:
            password += num[randint(0,9)]
            nnum -= 1
print("Your password is -",password)