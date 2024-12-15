def day3_zuoye1():
    x=1
    for i in range(10):
        x=(x+1)*2
    print(x)

def day3_zuoye2():
    pt="*"
    for i in range(4):
        x=2*i+1
        pf=pt.center(x,'*')
        pf=pf.center(7,' ')
        print(pf)
    for i in range(3):
        x=2*i+3
        pf=pt.center(8-x,'*')
        pf=pf.center(7,' ')
        print(pf)
num=input()
def day3_zuoye3(num0):
    length=len(num0)
    mystr=""
    print(f"数字长度为{length}")
    for i in range(length):
       mystr+=num0[length-i-1]
    print(mystr)
    return mystr

def day3_zuoye4():
    num1=day3_zuoye3(num)
    num2=day3_zuoye3(num1)
    print(num1,num2)

def day3_zuoye5():
    year=int(input())
    if (year%4)==0:
        print("闰年")
    if (year//100)%4==0 and (year%4)==0:
        print("世纪闰年")



