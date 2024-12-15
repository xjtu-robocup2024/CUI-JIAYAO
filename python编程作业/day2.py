def day2_zuoye_1():
    str=input()#input()输入默认是str类型!!!
    letters = 0
    spaces = 0
    digits = 0
    other = 0
    for i in str:
        if i.isalpha():
            letters += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1
        else:
            other=other+1
    print(f"{letters},{spaces},{digits},{other}")

def day2_zuoye_2():
    x=int(input())
    a=x
    for i in range(5):
        x=10*x+a
        print(x)

def day2_zuoye_3():
    x = 100
    a=0
    for i in range(10):
        x=x/2
        a=a+x
    print(a,x)

def day2_zuoye_4():
    num=int(input())
    for x in range(num):
        a = x // 100
        b = (x % 100) // 10
        c = x % 10
        y=a**3+b**3+c**3
        if 0<y//100<10 and y==x:
            print(y)


def day2_zuoye_5():
    myset=set()
    for i in range(101,200):
        if (i%2)!=0 and (i%3)!=0 and (i%5)!=0 and (i%7)!=0:
            myset.add(i)
    print(myset)

