import glob

#pickup = [39,40,41,45,46,47,48,51,52,53,60,68,80,92,104,114,115,116,117,120,121,122,129,137,149,161,173]
#pickup = [75,76,77,87,88,89,93,99,100,101,117,131,155,179,203,225,226,227,231,237,238,239,255,269,293,317,341]

pickup = [81,82,83,87,88,89,93,94,95,99,100,101,117,131,155,179,203]

for path in glob.glob('..\\Mix\\a*'):
    for folder in glob.glob(path+'\\*'):
        for filecount, file in enumerate(glob.glob(folder+'\\*.bvh')):
            print(file)
            count = 0
            output_filename = '..\\forMatlab' + file[6:-4] + '.dat'
            print(output_filename)
            output = open(output_filename,'w')
            for line in open(file):
                if 'MOTION' in line:
                    count+=1
                elif count > 203:
                    break
                elif count > 0:
                    count+=1
                if count > 4:
                    itemList = line[:-1].split(' ')
                    if count == 5:
                        print(len(itemList))
                    temppose = []
                    for i, item in enumerate(itemList):
                        if(i in pickup):
                            output.write(str(item)+' ')
                    output.write('\n')
