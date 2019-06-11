import xlwt

# 声明文件名称，方便用
txtname = 'f1.txt'
excelname = 'test.xls'

# 读取txt文件
fopen = open(txtname, 'r')
lines = fopen.readlines()

file = xlwt.Workbook(encoding='utf-8', style_compression=0)
# 新建一个sheet并命名
sheet = file.add_sheet('武汉市2019年高考成绩')

# 增加表头
sheet.write(0, 0, '考号')
sheet.write(0, 1, '姓名')
sheet.write(0, 2, '性别')
sheet.write(0, 3, '成绩')

# 开始写数据咯
i = 1
for line in lines:
    line = line.strip('\n')
    line = line.split(' ')
    number1 = line[0]
    name1 = line[1]
    sex1 = line[2]
    score1 = int(line[3])

    sheet.write(i, 0, number1)
    sheet.write(i, 1, name1)
    sheet.write(i, 2, sex1)
    sheet.write(i, 3, score1)
    i = i + 1
#末尾的函数
sheet.write(i, 3, xlwt.Formula('average(D2:D1001)'))

file.save(excelname)
