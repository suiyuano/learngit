#!/usr/bin/env python3.4
# coding=utf-8
import sys
import string

keywards = {}

# 关键字部分
keywards['if'] = 1
keywards['else'] = 2
keywards['int'] = 3
keywards['return'] = 4
keywards['void'] = 5
keywards['while'] = 6

# 符号
keywards['+'] = 7
keywards['-'] = 8
keywards['*'] = 9
keywards['/'] = 10
keywards['<'] = 11
keywards['<='] = 12
keywards['>'] = 13
keywards['>='] = 14
keywards['=='] = 15
keywards['!='] = 16
keywards['='] = 17
keywards[';'] = 18
keywards[','] = 19
keywards['('] = 20
keywards[')'] = 21
keywards['['] = 22
keywards[']'] = 23
keywards['{'] = 24
keywards['}'] = 25
keywards['/*'] = 26
keywards['*/'] = 27


# 变量
# keywards['var'] = 301

# 常量
# keywards['const'] = 401

# Error
# keywards['const'] = 501

signlist = {}
signals = []  # 专用符号
reserves = []  # 保留字
varys = []  # 变量
numbers = []  # 常量


# 预处理函数，将文件中的空格，换行等无关字符处理掉
def pretreatment(file_name):
    try:
        fp_read = open(file_name, 'r')
        fp_write = open('file.tmp', 'w')
        sign = 0
        while True:
            read = fp_read.readline()
            if not read:
                break
            length = len(read)
            i = -1
            while i < length - 1:
                i += 1
                if sign == 0:
                    if read[i] == ' ':
                        continue
                if read[i] == '#':
                    break
                elif read[i] == ' ':
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write(' ')
                elif read[i] == '\t':
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write(' ')
                elif read[i] == '\n':
                    if sign == 1:
                        continue
                    else:
                        fp_write.write(' ')
                        sign = 1
                elif read[i] == '"':
                    fp_write.write(read[i])
                    i += 1
                    while i < length and read[i] != '"':
                        fp_write.write(read[i])
                        i += 1
                    if i >= length:
                        break
                    fp_write.write(read[i])
                elif read[i] == "'":
                    fp_write.write(read[i])
                    i += 1
                    while i < length and read[i] != "'":
                        fp_write.write(read[i])
                        i += 1
                    if i >= length:
                        break
                    fp_write.write(read[i])
                else:
                    sign = 3
                    fp_write.write(read[i])
    except Exception:
        print(file_name, ': This FileName Not Found!')


def save(string):
    if string in keywards.keys():
        if string not in signlist.keys():
            signlist[string] = keywards[string]
            # print("signlist:"+signlist)
        else:
            pass
    else:
        try:
            float(string)
            save_const(string)
        except ValueError:
            save_var(string)


def savesigns(string):
    if string in keywards.keys():
        if string not in signals:
            signals.append(string)
        else:
            pass
    else:
        pass


def save_var(string):
    if string not in signlist.keys():
        if len(string.strip()) < 1:
            pass
        else:
            if is_signal(string) == 1:
                signlist[string] = 301
            else:
                signlist[string] = 501


def save_const(string):
    if string not in signlist.keys():
        signlist[string] = 401


def save_error(string):
    if string not in signlist.keys():
        signlist[string] = 501


def is_signal(s):
    if s[0] == '_' or s[0] in string.ascii_letters:
        for i in s:
            if i in string.ascii_letters or i == '_' or i in string.digits:
                pass
            else:
                return 0
        return 1
    else:
        return 0


def recognition(filename):
    try:
        fp_read = open(filename, 'r')  # 该文件对象只能用一次么？于是在main函数中重新定义了一个文件对象
        string = ""
        sign = 0

        while True:
            read = fp_read.read(1)
            if not read:
                break

            if read == ' ':
                if len(string.strip()) < 1:
                    sign = 0
                    pass
                else:
                    if sign == 1 or sign == 2:
                        string += read
                    else:
                        save(string)
                        string = ""
                        sign = 0
            elif read == '(':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    savesigns('(')
            elif read == ')':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    savesigns(')')
            elif read == '[':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    savesigns('[')
            elif read == ']':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    savesigns(']')
            elif read == '{':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    savesigns('{')
            elif read == '}':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    savesigns('}')
            # elif read == '<':
            #     save(string)
            #     string = ""
            #     savesigns('<')
            # elif read == '>':
            #     save(string)
            #     string = ""
            #     savesigns('>')
            elif read == ',':
                save(string)
                string = ""
                savesigns(',')

            elif read == ';':
                save(string)
                string = ""
                savesigns(';')

            elif read == '+':
                save(string)
                string = ""
                savesigns('+')

            elif read == '-':
                save(string)
                string = ""
                savesigns('-')

            elif read == '*':
                save(string)
                string = ""
                savesigns('*')

            elif read == '/':
                save(string)
                string = ""
                savesigns('/')


            # elif read == '=':
            #     save(string)
            #     string = ""
            #     savesigns('=')
            elif read == '=':
                readnext = fp_read.read(1)
                if readnext == '=':
                    save(string)
                    string = ""
                    savesigns('==')
                else:
                    save(string)
                    string = "{}".format(readnext)
                    savesigns('=')

            elif read == '<':
                readnext = fp_read.read(1)
                if readnext == '=':
                    save(string)
                    string = ""
                    savesigns('<=')
                else:
                    save(string)
                    string = "{}".format(readnext)
                    savesigns('<')

            elif read == '>':
                readnext = fp_read.read(1)
                if readnext == '=':
                    save(string)
                    string = ""
                    savesigns('>=')
                else:
                    save(string)
                    string = "{}".format(readnext)
                    savesigns('>')


            elif read == '!':
                readnext = fp_read.read(1)
                save(string)
                string = ""
                savesigns('!=')

            else:
                string += read

    except Exception as e:
        print(e)


def main():
    if len(sys.argv) < 2:  # sys.argv[0]代表的是本文件的url,[1],[2]等外部参数需要在运行时设置，具体参考csdn收藏夹！
        print("Please Input FileName")
    else:
        pretreatment(sys.argv[1])  # sys.argv[1]为自己设置的外部参数，表示打开文件的目录名
    recognition('file.tmp')  # 对临时文件进行分析，然后将结果输出打印

    fp_read = open('file.tmp', 'r')  # 该文件对象只能用一次么？于是在main函数中重新定义了一个文件对象
    sourcestring = fp_read.read()  # 转化后的原始字符串
    # print("sourcestring:"+sourcestring)

    # print(signals)

    for res in ['int', 'if', 'else', 'return', 'void', 'while']:
        if res in signlist.keys():
            reserves.append(res)
    # print(reserves)

    for i in signlist.keys():
        # print("(", signlist[i], ",", i, ")")
        if signlist[i] == 301:
            varys.append(i)
        elif signlist[i] == 401:
            numbers.append(i)

    # print(varys)
    # print(numbers)

    for i in reserves:
        print("reserve word:" + i)
    for i in varys:
        print("ID,name=" + i)
    for i in numbers:
        print("NUM,val=" + i)
    for i in signals:
        print("Signals:" + i)


if __name__ == '__main__':
    main()
