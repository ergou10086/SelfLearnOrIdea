# CSV 文件又称为逗号分隔值文件，是一种通用的、相对简单的文件格式，用以存储表格数据，包括数字或者字符
# CSV 是电子表格和数据库中最常见的输入、输出文件格式

# CSV文件写入
# csv 模块中的 writer 类可用于读写序列化的数据，其语法格式如下
# writer(csvfile, dialect='excel', **fmtparams)
# 参数说明：
#     csvfile：必须是支持迭代(Iterator)的对象，可以是文件(file)对象或者列表(list)对象。
#     dialect：编码风格，默认为 excel 的风格，也就是使用逗号,分隔。
#     fmtparam：格式化参数，用来覆盖之前 dialect 对象指定的编码风格。

import csv
# 写
with open('eggs.csv', 'w', newline="") as csvfile:
    # delimiter 指定分隔符，默认为逗号，这里指定为空格
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|')
    spamwriter.writerow(["www.biancheng.net"] * 3 + ['how are you'])
    spamwriter.writerow(['hello world', 'web site', 'www.biancheng.net'])
    # 同时写入多行数据，使用 writerrows() 方法
    # 注意传入数据的格式为列表元组格式
    spamwriter.writerows([('hello','world'), ('I','love','you')])

# 读
# csv.reader(csvfile, dialect='excel', **fmtparams)
with open('eggs.csv','r',newline="") as csvfile:
    spamreader = csv.reader(csvfile, dialect=" ", quotechar='|')
    for row in spamreader:
        print(', '.join(row))