import sys

with open('file.list.txt') as fp :
    file_list=fp.readlines()

    outputlist=[]

    for eachline in file_list:
        eachline=eachline.strip('\n')
        populations_list=eachline.split('\t')
        current_population=''
        for each_population in populations_list:
            current_population=each_population
            outputlist_item=populations_list[0]+'_'+populations_list[1]+'_'+populations_list[2]+'_'+populations_list[3]+'.txt.'+current_population+'.vcf.countinput'+'\n'
            outputlist.append(outputlist_item)

    outputString=''
    for eachone in outputlist:
        outputString=outputString+eachone
    data = open("countinput_filelist.txt", 'w+')
    print(outputString, file=data)
    data.close()

