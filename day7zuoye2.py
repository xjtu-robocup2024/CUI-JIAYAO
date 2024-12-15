import os
import random
import string

def generate_random_line(length=50):
    """生成包含ASCII标准任意非控制字符的随机行"""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def create_test_file(file_path, num_lines):
    """创建test.txt文件并生成指定数量的随机行"""
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            file.write(generate_random_line() + '\n')

def main():
    # 指定工作目录（可以修改为实际的工作目录）
    work_directory = '.'  # 当前目录
    # 询问用户要生成的行数
    num_lines = int(input("请输入要生成的行数: "))
    # 构建文件路径
    file_path = os.path.join(work_directory, 'test.txt')
    # 创建文件并生成内容
    create_test_file(file_path, num_lines)
    print(f"文件 '{file_path}' 已生成。")

if __name__ == "__main__":
    main()

import os
import shutil

def copy_file(src, dst):
    """拷贝文件"""
    shutil.copy2(src, dst)

def main():
    # 指定工作目录（可以修改为实际的工作目录）
    work_directory = '.'  # 当前目录
    # 构建源文件和目标文件路径
    src_file_path = os.path.join(work_directory, 'test.txt')
    dst_file_path = os.path.join(work_directory, 'copy_test.txt')
    # 拷贝文件
    copy_file(src_file_path, dst_file_path)
    print(f"文件 '{src_file_path}' 已拷贝到 '{dst_file_path}'。")

if __name__ == "__main__":
    main()