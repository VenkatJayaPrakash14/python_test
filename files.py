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


def testMsg(passed):
    if passed:
       return 'Test Passed'
    else :
       return 'Test Failed'

testWrite = "myfiles"
testAppend = "example.txt"
passed = True

genFiles("myfiles","example.txt")

with open("myfiles",'r') as file:
    ogWrite = file.readlines()

with open("example.txt",'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles("myfiles",testAppend)
except:
    print('Error')

with open("myfiles",'r') as file:
    clWrite = file.readlines()

with open("example.txt",'r') as file:
    clAppend = file.readlines()
        
# checking if total no of rows is same, including headers

if (len(ogWrite) + len(ogAppend) != len(clWrite) + len(clAppend)):
    print("The number of rows do not add up. Make sure your final files have the same header and format.")
    passed = False
    
for line in clWrite:
    if  'no' in line:
        passed = False
        print("Inactive members in file")
        break
    else:
        if line not in ogWrite:
            print("Data in file does not match original file")
            passed = False
print ("{}".format(testMsg(passed)))