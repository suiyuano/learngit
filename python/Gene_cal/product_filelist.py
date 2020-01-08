import sys

with open("file.list.txt") as fp1:
    list=fp1.readlines()

    outputlist=[]
    for eachline in list:
        eachline=eachline.strip('\n')
        items_list=eachline.split('\t')
        outputlist_item=items_list[0]+'_'+items_list[1]+'_'+items_list[2]+'_'+items_list[3]+'.txt'+'\n'
        outputlist.append(outputlist_item)

    outputString=''
    for eachone in outputlist:
        outputString=outputString+eachone

    data = open("filelist.txt", 'w+')
    print(outputString, file=data)
    data.close()