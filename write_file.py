# -*- coding: utf-8 -*-

import os

file_name = 'result.txt'

# 初始化
def file_init(new_file_name=''):
    global file_name
    if new_file_name != '':
        file_name = new_file_name
    file_name = './result/' + file_name
    if not os.path.exists('./result/'):
        os.mkdir('./result/')
    with open(file_name, 'w+') as f:
        pass

# 写文件
def write(*args):
    s = ''
    for v in args:
        s += str(v).strip() + ' '
    s += '\n'
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(s)

