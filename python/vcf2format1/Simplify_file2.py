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
        i = i.strip('\n')
        str_split = i.split(' ')  # 把每行输入以空格切割开
        last_list_item=str_split[1]+'\t'+str_split[3]+'\t'+str_split[2]+'\n'
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


