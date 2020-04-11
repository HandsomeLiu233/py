import numpy
txtname = 'judge.txt'

fopen = open(txtname, 'r')
lines = fopen.readlines()

#read data
data=[]
for line in lines:
    line = line.strip('\n')
    line = line.split(',')

    data.append(line)


#convert data to int

for i in range(len(data)):
    for j in range(1,len(data[i])):
        data[i][j]=int(data[i][j])

#find max data and min data

max=[0,-999,-999,-999]
min=[0,999,999,999]

for i in range(len(data)):
    for j in range(1,len(data[i])):
        if data[i][j]>max[j]:
            max[j]=data[i][j]
        if data[i][j]<min[j]:
            min[j]=data[i][j]


#for average score
avg=[0,0,0,0]
for i in range(len(data)):
    for j in range(1,len(data[i])):
        avg[j]=data[i][j]+avg[j]

for i in range(1,len(avg)):
    avg[i]=avg[i]-max[i]-min[i]
    avg[i]=avg[i]/(len(data)-2)

#find max
maxguy=[0,-999]
for j in range(1,len(avg)):
    if maxguy[1]<avg[j]:
        maxguy[1]=avg[j]
        maxguy[0]=j

print(maxguy)

print("分数最高的是",str(maxguy[0]),"号选手，分数是",str(maxguy[1]),"分")
