from random import randint as rnd

memReg = "myfiles"
exReg = "example.txt"
fee =('yes','no')

def genFiles(current,old):
    with open("myfiles",'w+') as writefile: 
        print(writefile.write('Membership No  Date Joined  Active  \n'))
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            print(writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)])))


    with open("example.txt",'w+') as writefile: 
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015,2020))+ '-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            print(writefile.write(data.format(rnd(10000,99999),date,fee[1])))


genFiles(memReg,exReg)


def cleanFiles(currentMem, exMem):
    memReg = "myfiles"
exReg = "example.txt"
cleanFiles(memReg,exReg)



headers = "Membership No  Date Joined  Active  \n"
with open("example.txt",'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open("myfiles",'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())