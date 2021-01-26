def DeterminPassFail(grade1,grade2):
    ''' determines if student passed or failed'''
    if(grade1<60 and  grade2<60):
        print(" Student Failed")

    elif( grade1>=95 and grade2>=95):
        print("student Graduated with Honors:)")

    else:
        print(" Student Graduated")





def calcAverage(lst, size):
    ''' this calcuates and returns average ofe elements'''
    total=0
    for index in range(size):
        total+=lst[index]


    average=total/size

    print("The Average is ", average )




            
    


