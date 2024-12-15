import random
def day1_zuoye_1():
    x=[1,2,3,4]
    myset = set()
    while(len(myset)<24):
        i=random.choice(x)#random.choice():在一个数组里面随机选择一个数
        j=random.choice(x)
        k=random.choice(x)
        three=100*i+10*j+k
        if i!=j and i!=k and j!=k:
           myset.add(three)
    print(myset)
    return myset

def day1_zuoye_2():
    num1=int(input())#要加int
    num2=int(input())
    num3=int(input())
    num4=int(input())
    arr=[num1,num2,num3,num4]
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j + 1]:
               arr[j],arr[j + 1]=arr[j + 1],arr[j]
    print(arr)
    return arr

def day1_zuoye_3():
    a = 0
    b = 1
    for i in range(20):
        c=a+b
        print(c)
        a=b
        b=c

def day1_zuoye_4():
    for i in range(9):
        x=i+1
        for x in range(x):
            print(f"{x}*{i}={x*i}",end="\t")#end="\t"意思是在后面加一个空格，end="\n"是换行
            #f""可以用{}写入变量名或者表达式，它会直接带入变量的数值或者计算表达式的值
        print(end="\n")
day1_zuoye_4()
