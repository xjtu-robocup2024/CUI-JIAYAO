import csv
import random

# 生成10行3列的随机数，并写入CSV文件
filename = 'random_numbers.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for _ in range(10):
        row = [random.randint(0, 100) for _ in range(3)]  # 生成0到100之间的随机数
        writer.writerow(row)

print(f"CSV文件 '{filename}' 已生成。")


import csv

# 定义计算中位数的函数
def median(lst):
    n = len(lst)
    sorted_lst = sorted(lst)
    mid = n // 2
    if n % 2 == 0:  # 偶数个数，取中间两个数的平均值
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:  # 奇数个数，取中间那个数
        return sorted_lst[mid]

# 读取CSV文件并计算第二列的最大值、最小值、平均值和中位数
filename = 'random_numbers.csv'
second_column_values = []

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        try:
            second_column_values.append(int(row[1]))  # 假设CSV文件没有标题行，且第二列索引为1（从0开始计数）
        except ValueError:
            print(f"无法将第二列的值 '{row[1]}' 转换为整数。")

# 计算统计量
max_value = max(second_column_values)
min_value = min(second_column_values)
average_value = sum(second_column_values) / len(second_column_values)
median_value = median(second_column_values)

# 输出结果
print(f"第二列的最大值: {max_value}")
print(f"第二列的最小值: {min_value}")
print(f"第二列的平均值: {average_value}")
print(f"第二列的中位数: {median_value}")