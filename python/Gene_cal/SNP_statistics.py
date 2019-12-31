import sys

# 读入文件，自动把每个文件按行数生成列表，共4个列表
with open("pop1.txt") as fp1, open("pop2.txt") as fp2, open("pop3.txt") as fp3, open("pop4.txt") as fp4:
    list1 = fp1.readlines()
    list2 = fp2.readlines()
    list3 = fp3.readlines()
    list4 = fp4.readlines()
    # print(list1)

    # 统计每个群体样本数，好生成最后的列表
    len1 = len("".join(list1[0].split()))
    len2 = len("".join(list2[0].split()))
    len3 = len("".join(list3[0].split()))
    len4 = len("".join(list4[0].split()))

    output_key_list = []

    for i in range(0, len1 + 1):
        for a in range(0, len2 + 1):
            for b in range(0, len3 + 1):
                for c in range(0, len4 + 1):
                    output_key_list.append(str(i) + str(a) + str(b) + str(c))
    # print(output_list)
    # print(len(output_key_list))

    output_val_list = []
    for i in range(0, len(output_key_list)):
        output_val_list.append(0)

    # print(len(output_val_list))
    # print(output_val_list)

    output_list = dict(zip(output_key_list, output_val_list))  # 两个列表合成一个字典
    # print(output_list)

    # print(len1,len2,len3,len4)
    doc_countlist = []  # 计数数组，每一个SNP对应的数字都会加入进来，例如SNP1：2321
    for i in range(len(list1)):
        num1 = list1[i].count("1")
        num2 = list2[i].count('1')
        num3 = list3[i].count('1')
        num4 = list4[i].count('1')
        element = str(num1) + str(num2) + str(num3) + str(num4)
        # print(element)
        doc_countlist.append(element)

    # print(doc_countlist)

    for each_element in doc_countlist:
        for each in output_list:
            if each_element == each:
                output_list[each] = output_list[each] + 1

    # print('output_list:')
    # print(output_list)

    last_list=[]

    outputString = ''
    for eachitem in output_key_list:
        for i in output_list:
            if eachitem==i:
                outputString = outputString + i + '\t' + str(output_list[i]) + '\n'
                # print('outputString'+outputString)

    # for i in output_list:
    #
    #     outputString = outputString + i + '_' + str(output_list[i]) + '\n'
    #     # print('outputString'+outputString)

    # print('outputString:'+outputString)
    data = open("output.txt", 'w+')
    print(outputString, file=data)
    data.close()
