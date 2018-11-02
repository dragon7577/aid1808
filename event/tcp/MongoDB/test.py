import re
import sys

def get_address(port):
    f = open('./1.txt')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        #说明已经读到文件结尾了
        if not data:
            return 'Not Found the port'
            break
        #匹配出首单词
        try:
            PORT = re.match(r'\S+',data).group()
        except Exception as e:
            print(e)
            continue
        if port == PORT:
            # pattern = r'address is (\w{4}\.\W{4}\.\w{4})'
            pattern = r'address is ((\d\.){3}\d+)'
            address = re.search(pattern,data).group(1)
            return address

if __name__ =='__main__':
    port = sys.argv[1]
    print(get_address(port))
