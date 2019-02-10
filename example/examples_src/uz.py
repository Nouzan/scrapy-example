import gzip
from sys import argv

def un_gz(file_name, output):
    """ungz zip file"""
    f_name = output
    #获取文件的名称，去掉
    g_file = gzip.GzipFile(file_name)
    #创建gzip对象
    open(f_name, "wb+").write(g_file.read())
    #gzip对象用read()打开后，写入open()建立的文件里。
    g_file.close()
    #关闭gzip对象

if __name__ == "__main__":
    path = 'output/'
    count = 0
    for file_name in argv[1:]:
        print('unzipping', file_name)
        count += 1
        output_name = path + str(count) + '.csv'
        un_gz(file_name, output_name)
        print('done', output_name)