import re
import glob
import numpy as np

cycle = False
once = False
term = True

'''
--cycle--

this function can generate two cycle motions.
you should ready txt file that consists the list of one cycle time stamp.

format of txt file as following

150
358
565
755
976
1204
1376
1556
1830
2044


it generates data as following.
150 - 564
358 - 754
565 - 975
...

'''

if cycle:
    for bvh in glob.glob('*.bvh'):
        print(bvh)
        bvh_name = bvh[:-10]

        header = []
        data = []

        count = 0
        for line in open(bvh):
            if 'Frame Time' in line:
                count+=1
                header.append(line)
            elif 'Frames:' in line:
                continue
            elif count > 0:
                count+=1
                data.append(line)
            else:
                header.append(line)
            
        count = 0;
        for segment in glob.glob('segment\\*.txt'):
            print(segment)
        
            frame_list = []
            for line in open(segment):
                frame_list.append(int(line))

            for index, frame in enumerate(frame_list):
                if index < 1:
                    continue
                output = open('output\\'+bvh_name+"{0:02}".format(count)+'.bvh','w')
                count+=1
                for l in header:
                    if 'Frame Time' in l:
                        output.writelines('Frames: '+str(frame_list[index]-frame_list[index-2])+'\n')
                        output.writelines(l)
                    else:
                        output.writelines(l)

                for l in data[frame_list[index-2]:frame_list[index]]:
                    output.writelines(l)


'''
--once--

this function can generate one cycle motions.
you should ready txt file that consists the list of one cycle time stamp.

format of txt file as following

150
358
565
755
976
1204
1376
1556
1830
2044


it generates data as following.
150 - 357
358 - 564
565 - 754
...

'''


if once:
    for bvh in glob.glob('*.bvh'):
        print(bvh)
        bvh_name = bvh[:-10]

        header = []
        data = []

        count = 0
        for line in open(bvh):
            if 'Frame Time' in line:
                count+=1
                header.append(line)
            elif 'Frames:' in line:
                continue
            elif count > 0:
                count+=1
                data.append(line)
            else:
                header.append(line)
            
        count = 0;
        for segment in glob.glob('segment\\*.txt'):
            print(segment)
        
            frame_list = []
            for line in open(segment):
                frame_list.append(int(line))

            for index, frame in enumerate(frame_list):
                if index < 0:
                    continue
                output = open('output\\'+bvh_name+"{0:02}".format(count)+'.bvh','w')
                count+=1
                for l in header:
                    if 'Frame Time' in l:
                        output.writelines('Frames: '+str(frame_list[index]-frame_list[index-1])+'\n')
                        output.writelines(l)
                    else:
                        output.writelines(l)

                for l in data[frame_list[index-1]:frame_list[index]]:
                    output.writelines(l)


'''
--term--

this function can generate one motions segmented by you.
you should ready txt file that consists the list of pair of first and last time stamp for segmentation.

format of txt file as following

  99	 315
 341	 590
 703	 990
1012	1269
1269	1566
1579	1846
1846	2079
2080	2273
2274	2489
2490	2770
2771	3031
3032	3273


it generates data as following.
99 - 315
341	- 590
703 - 990
...

'''

if term:
    print('Term')
    for bvh in glob.glob('..\\Mix\\original\\*.bvh'):
        print('FileName: '+bvh)
        bvh_name = bvh[16:-8]
        print(bvh_name)

        header = []
        data = []

        count = 0
        for line in open(bvh):
            if 'Frame Time' in line:
                count+=1
                header.append(line)
            elif 'Frames:' in line:
                continue
            elif count > 0:
                count+=1
                data.append(line)
            else:
                header.append(line)
            
        count = 0;
        for segment in glob.glob('..\\Mix\\Frames.txt'):
            print(segment)
                        
            for line in open(segment):
                itemList = line[:-1].split('\t')
                print(itemList)

                output = open('..\\Mix\\segment\\'+bvh_name+"{0:02}".format(count)+'.bvh','w')
                count+=1
                for l in header:
                    if 'Frame Time' in l:
                        output.writelines('Frames: '+str(int(itemList[1])-int(itemList[0]))+'\n')
                        output.writelines(l)
                    else:
                        output.writelines(l)

                for l in data[int(itemList[0]):int(itemList[1])]:
                    output.writelines(l)
        
