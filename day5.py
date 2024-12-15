import os
import random
import string
import shutil
def calculate(*args):
    total = sum(args)
    average = total / len(args)
    indices_above_average = [index for index, value in enumerate(args) if value > average]
    return (int(average), indices_above_average)
result = calculate(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(result)


def get_odd_index_elements(input_list):
    odd_index_elements = [input_list[i] for i in range(len(input_list)) if i % 2 != 0]
    return odd_index_elements
example_list = [10, 20, 30, 40, 50, 60, 70]
result = get_odd_index_elements(example_list)
print(result)


def day5_zuoye3():
    import random
    filename = 'data.txt'
    num_lines = 100000
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            random_number = random.randint(1, 100)
            file.write(f"{random_number}\n")
    print(f"已生成 {num_lines} 行随机数并写入 {filename}")

def day5_zuoye4():
    directory_name = 'img'
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    def generate_filename():
        letters = ''.join(random.choices(string.ascii_uppercase, k=4))
        digits = ''.join(random.choices(string.digits, k=5))
        return f"{letters}{digits}.jpg"
    for _ in range(100):
        filename = generate_filename()#先生成一个随机的filename（1）
        while os.path.exists(os.path.join(directory_name, filename)):#如果os.path.join(directory_name, filename（1）存在，
            filename = generate_filename()
            # 那么os.path.exists(os.path.join(directory_name, filename))将返回ture。循环再次执行，让filename再次生成一个filename（2）
            #再次进入循环，如果filename（2）不存在，那么退出循环继续执行下一句
        shutil.copy2(r"C:\Users\ASUS\Desktop\b715e87b56468c7f0dc9e09a285a207.jpg", os.path.join(directory_name, filename))
    print(f"在 {directory_name} 目录中创建了100个JPG文件")


import os
import shutil
import random
import string

def day5_zuoye5():
    directory_name = 'img'
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    def generate_filename():
        letters = ''.join(random.choices(string.ascii_uppercase, k=4))
        digits = ''.join(random.choices(string.digits, k=5))
        return f"{letters}{digits}.jpg"

    # 存储已复制文件的完整路径
    copied_files = []

    for _ in range(100):
        filename = generate_filename()
        while os.path.exists(os.path.join(directory_name, filename)):
            filename = generate_filename()
        file_path = os.path.join(directory_name, filename)
        shutil.copy2(r"C:\Users\ASUS\Desktop\b715e87b56468c7f0dc9e09a285a207.jpg", file_path)
        copied_files.append(file_path)

    # 随机选择50个文件进行重命名
    files_to_rename = random.sample(copied_files, 50)
    for file_path in files_to_rename:
        # 获取文件名（不带路径）
        base_name = os.path.basename(file_path)
        # 去掉.jpg扩展名并添加.png
        new_base_name = os.path.splitext(base_name)[0] + '.png'
        # 构建新的完整路径
        new_file_path = os.path.join(directory_name, new_base_name)
        # 重命名文件
        os.rename(file_path, new_file_path)

    print(f"在 {directory_name} 目录中创建了100个JPG文件，并随机将50个文件改名为.png结尾")
