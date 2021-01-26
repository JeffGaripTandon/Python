##getname=input("please tell me your name")
##print("welcome to python: "+ getname)
## 
##def getAbsNumber():
##    ''' this prints abs of number'''
##    number= int(input("enter number: "))
##    print(abs(number))
##
##
##getAbsNumber()
##
##
##def main():
##    getAbsNumber()
##



##
##def printHello():
##    print("Helllo World!")
##    
##
##
##
##
##printHello()

QUARTER=0.25
DIME=0.10
NICKEL=0.05
PENNIES=0.01


def calcNreturnVal():
    ''' calculates coin value'''
    numQuart= int(input("enter how many quarters: "))
    numDimes= int(input("enter how many Dimes: "))
    numNickels= int(input("enter how many Nickels: "))
    numPennies= int(input("enter how many Pennies: "))
    QuartAmnt= numQuart*QUARTER
    DimeAmnt=numDimes*DIME
    NickelAmnt=numNickels*NICKEL
    PenniesAmnt=numPennies*PENNIES
    total=QuartAmnt+DimeAmnt+NickelAmnt+PenniesAmnt
    #print(total)
    dollarVal= int(total)
    #print(dollarVal)
    decmialpart= total- int(total)
    print("the total is "+ str(dollarVal)+" and "+ str(int(decmialpart*100))+ " cents")
    
    
    
    


calcNreturnVal()

    
