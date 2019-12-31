import sys,getopt

def main(argv):
    inputfile = ""
    outputfile = ""

    try:
        # 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
        opts, args = getopt.getopt(argv, "hi:o:", ["infile=", "outfile="])
    except getopt.GetoptError:
        print('Error: test_arg.py -i <inputfile> -o <outputfile>')
        print( '   or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print('test_arg.py -i <inputfile> -o <outputfile>')
            print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg



    with open(inputfile) as fp1:
        list1 = fp1.readlines()

    last_list = []
    for i in list1:
        if i[0] == "#":
            if i[1] == "#":
                continue
            else:
                # 输出行第一行的生成
                i = i.strip('\n')  # 去掉每行输入的最后的换行符
                str_split = i.split('\t')  # 把每行输入以空格切割开
                # print(str_split)
                str_split = str_split[9:]  # 根据原vcf文件的格式，取第9个元素之后的内容
                # print(str_split)
                last_list_item = 'CHR:POS'+'\t'+'CHR'+'\t'+'GeneticPos'+'\t'+'POS'+'\t'+'REF'+'\t'+'ALT'+'\n'
                last_list.append(last_list_item)
        else:
            i = i.strip('\n')
            str_split = i.split('\t')
            last_list_item = str_split[2]+'\t'+str_split[0]+'\t'+'0'+'\t'+str_split[1]+'\t'+str_split[3]+'\t'+str_split[4]+'\n'

            # print(str_split)

            last_list.append(last_list_item)

    outputString = ''
    for eachone in last_list:
        outputString = outputString + eachone
    data = open(outputfile, 'w+')
    print(outputString, file=data)
    data.close()

if __name__ == "__main__":
    main(sys.argv[1:])
# print(last_list)


