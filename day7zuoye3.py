def prepend_and_append_to_file(file_path, prepend_str, append_str):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 在开头和结尾追加字符串
    modified_content = prepend_str + content + append_str

    # 将修改后的内容写回文件（这里会覆盖原始内容）
    # 如果你不想覆盖原始内容，可以将内容写到一个新文件中
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modified_content)

    # 或者，将内容写到一个新文件中，保留原始文件
    # new_file_path = 'modified_test.txt'
    # with open(new_file_path, 'w', encoding='utf-8') as file:
    #     file.write(modified_content)


# 指定文件路径
file_path = 'test.txt'
# 要追加的字符串
prepend_str = ''
append_str = 'python'
# 调用函数
prepend_and_append_to_file(file_path, prepend_str, append_str)