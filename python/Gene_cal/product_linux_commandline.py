import sys

with open('countinput_filelist.txt') as fp:
    file_list=fp.readlines()

    outputlist=[]

    i=1
    output_item = ''
    for each_para in file_list:

        each_para=each_para.strip('\n')
        if i==1 :
            output_item=output_item+'/asnas/chenhua_group/Software/BIG_Software_DIR/python/python3/bin/python SNP_statistics_with_paras.py '+'-a '+each_para
            i=2
            continue
        if i==2:
            output_item=output_item+' -c '+each_para
            i=3
            continue
        if i==3:
            output_item=output_item+' -y '+each_para
            i=4
            continue
        if i==4:
            output_item=output_item+' -s '+each_para+' -o '+each_para.split('.txt')[0]+'_OutputFile.afs'+'\n'
            # output_item=output_item+' -o '+each_para.split('.txt')[0]+'_OutputFile.afs'+'\n'
            outputlist.append(output_item)
            output_item=''
            i=1
            continue
        else:
            continue

    outputString=''
    for eachone in outputlist:
        outputString=outputString+eachone
    data = open("linux_commandline.txt", 'w+')
    print(outputString, file=data)
    data.close()
