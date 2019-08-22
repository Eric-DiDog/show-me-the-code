import os


def read_codes(filepath):
    blank_lines = 0
    total_lines = 0
    note_lines = 0
    dir = [files for files in os.walk(filepath) if not files[0].__contains__('venv')]
    for each in dir:
        #print(each[0])
        for per in each[2]:
            if per.endswith('.py'):
                path=os.path.join(each[0],per)
                with open(path, 'rb') as w:
                    lines = w.readlines()
                    total_lines += len(lines)
                    for per in lines:
                        if per.startswith(bytes('#', encoding='utf-8')):
                            note_lines += 1
                        if per == bytes('''\r\n''', encoding='utf-8'):
                            blank_lines += 1
    print('总代码行数：', total_lines)
    print('其中,注释行数：', note_lines)
    print('\t空白行数：', blank_lines)
    # d = [j for j in os.listdir(filepath) if j.endswith('.py')]
    # for each in d:
    #     with open(filepath+'/'+each,'rb') as w:
    #         lines=w.readlines()
    #         total_lines+=len(lines)
    #         for per in lines:
    #             if per.startswith(bytes('#',encoding='utf-8')):
    #                 note_lines+=1
    #             if per==bytes('''\r\n''',encoding='utf-8'):
    #                 blank_lines+=1
    # print('总代码行数：',total_lines)
    # print('其中,注释行数：', note_lines)
    # print('\t空白行数：', blank_lines)


read_codes('E:\\Python学习之路')
#read_codes('E:\\Python学习之路\\独立完成空间爬虫')