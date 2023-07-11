#1.Basic-print all integers from 0 to 150
for i in range (151):
    print(i)
#2.Multiple of Five- Print all the multiples of 5 from 5 to 1000
for i in range(5,1001,5):
    print(i)
#3.Counting, the Dojo Way- Print integers 1 to 100.if divisible by 5,print "Coding" instead.if divisible by 10,print "Coding Dojo"
for i in range (1,101):
    if (i%5==0 and i%10!=0):
        print("Coding")
    elif (i%10==0):
        print("Coding Dojo")
    else:
        print(i)
        
#4.Whoa. That Sucker's Huge-add odd integers from 0 to 500,000 and print the final sum
sum=0
for i in range (1,500000,2):
    sum+=i
print(sum)
#5.Countdown by Fours- Print positive numbers starting at 2018, counting down by four
for i in range (2018,0,-4):
    print (i)
#6.Flexible Counter- Set three variables/lowNum,highNum,mult.Starting at lowNum and going through highNum,print only thr integers that are a multiple of mult. For example,if lowNum=2,highNum=0, and mult=3,the loop should print 3,6,9(on successive lines)
def Flexible(lowNum,highNum,mult):
    for i in range (lowNum,highNum+1):
        if (i%mult==0):
            print(i)
    return None
Flexible(2,9,3)
        