import sys
import getopt


def main(argv):
    inputfile1 = ""
    inputfile2 = ""
    inputfile3 = ""
    inputfile4 = ""
    outputfile = ""

    try:
        # 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
        opts, args = getopt.getopt(argv, "ha:c:y:s:o:", ["infile1=", "infile2=", "infile3=", "infile4=", "outfile="])
    except getopt.GetoptError:
        print('Error: test_arg.py -a <inputfile1> -c <inputfile2> -y <inputfile3> -s <inputfile4> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print('test_arg.py -i <inputfile> -o <outputfile>')
            print('or: test_arg.py --infile=<inputfile> --outfile=<outputfile>')
            sys.exit()
        elif opt in ("-a", "--infile1"):
            inputfile1 = arg
        elif opt in ("-c", "--infile2"):
            inputfile2 = arg
        elif opt in ("-y", "--infile3"):
            inputfile3 = arg
        elif opt in ("-s", "--infile4"):
            inputfile4 = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg

    with open(inputfile1) as fp1, open(inputfile2) as fp2, open(inputfile3) as fp3, open(inputfile4) as fp4:
        list1 = fp1.readlines()
        list2 = fp2.readlines()
        list3 = fp3.readlines()
        list4 = fp4.readlines()
        # print(list1)

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

        output_list = dict(zip(output_key_list, output_val_list))
        # print(output_list)

        # print(len1,len2,len3,len4)
        doc_countlist = []
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

        last_list = []

        outputString = ''
        for eachitem in output_key_list:
            for i in output_list:
                if eachitem == i:
                    outputString = outputString + i + '\t' + str(output_list[i]) + '\n'
                    # print('outputString'+outputString)

        # for i in output_list:
        #
        #     outputString = outputString + i + '_' + str(output_list[i]) + '\n'
        #     # print('outputString'+outputString)

        # print('outputString:'+outputString)
        data = open(outputfile, 'w+')
        print(outputString, file=data)
        data.close()


if __name__ == "__main__":
    main(sys.argv[1:])
