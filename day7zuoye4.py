def read_file_lines(file_path):
    """读取文件内容，并返回按行分割的列表"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()


def compare_files(file1_path, file2_path):
    """比较两个文件的内容，输出不同的行的编号"""
    lines1 = read_file_lines(file1_path)
    lines2 = read_file_lines(file2_path)

    # 获取两个文件中行数较多的那个，以便后续遍历
    max_length = max(len(lines1), len(lines2))

    # 用于记录不同行的编号的集合（避免重复输出）
    different_lines = set()

    # 遍历每一行进行比较
    for i in range(max_length):
        line1 = lines1[i].rstrip() if i < len(lines1) else ''
        line2 = lines2[i].rstrip() if i < len(lines2) else ''

        if line1 != line2:
            different_lines.add(i + 1)  # 行编号从1开始

    # 输出不同的行的编号
    for line_num in sorted(different_lines):
        print(f"Line {line_num} is different.")


# 指定文件路径
file1_path = 'test.txt'
file2_path = 'copy_test.txt'

# 调用函数进行比较
compare_files(file1_path, file2_path)