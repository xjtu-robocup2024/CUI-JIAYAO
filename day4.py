import numpy as np
def day4_zuoye1():
    x=[1,2,3,4,5]
    numbers = [str(num) for num in x]
    separator = ','
    result = separator.join(numbers)
    print(result)


def day4_zuoye2(arr, num):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] > num:
            new_arr.extend(arr[:i])
            new_arr.append(num)
            new_arr.extend(arr[i:])
            break
    else:
        new_arr.extend(arr)
        new_arr.append(num)

    return new_arr
sorted_array = [1, 3, 5, 7, 9]
new_number = 6
result = day4_zuoye2(sorted_array, new_number)
print(result)


def day4_zuoye3():
    x1 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
    x2 = np.array([
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]])
    result = x1 + x2
    print(result)

def day4_zuoye4():#直接切片简单些
    x=[1,3,5,7,4,2,1]
    i=4
    cut1=x[:i-1]
    cut2=x[(len(x)-i):]
    y=cut2+cut1
    print(y)


def day4_zuoye5():
    dict = {(1, 1): 0, (2, 2): 1, (3, 3): 2}
#元组时不可变的，因此可以作为字典的键，而集合和列表都是可变的，因此不能作为key

def day4_zuoye6():
    my_list = list(range(1000))
    even_numbers = [num for num in my_list if num % 2 == 0]
    print(even_numbers)

def day4_zuoye7():
    people=[]
    for i in range(233):
        if i%3==0:
            people.append(i)
    print(people)



