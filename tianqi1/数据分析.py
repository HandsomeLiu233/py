# 这个代码是在是太乱了，我都不敢随便把某些代码扔进函数里（o(╥﹏╥)o）

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_csv(r'C:\Users\liuao\PycharmProjects\untitled\tianqi1\result.csv', usecols=['日期', 'PM2.5'], encoding='gbk')
df.plot(x='日期')
plt.title('PM2.5全年走势图')
plt.savefig('year.jpg')
df_dt = pd.to_datetime(df.日期, format="%Y/%m/%d")  # 有点不理解
s_M = df_dt.dt.month
df['月份'] = s_M
df_month = df.groupby('月份').sum()

# 为这个二维表增加一行作为月份https://blog.csdn.net/luoganttcc/article/details/77570024
df_month['month'] = '0'
for i in range(12):
    df_month.iat[i, 1] = i + 1
df_month.plot(x='month')
plt.title('PM2.5月走势图')
plt.savefig('month.jpg')

# 季度箱型图
one = df_month[:3].sum()
two = df_month[3:6].sum()
three = df_month[6:9].sum()
four = df_month[9:12].sum()
plt.boxplot([one, two, three, four], labels=['第一季度', '第二季度', '第三季度', '第四季度'], sym='o', whis=0.05)
plt.title('PM2.5季度箱型图')
plt.savefig('box.jpg')

# 饼图
df_pie = pd.read_csv(r'C:\Users\liuao\PycharmProjects\untitled\tianqi1\result.csv', usecols=['质量等级'], encoding='gbk')
df_pie['all'] = 1
df_pie = df_pie.groupby('质量等级').sum()
# plt.pie(df_pie('all'),labels=df_pie('质量等级'))

# plt.figure(figsize=(5,5))
# plt.pie(df_pie.iloc[0,:],radius=1,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['r','g','b','y'],labels=df_pie['all'])

df_pie = df_pie.assign(State=df_pie.index.get_level_values('质量等级'))  # index转换为df里的一行列表
piee = df_pie.values.tolist()  # df转换为列表的神奇操作
pieename = []
pieedt = []
for i in range(len(piee)):
    pieename.append(piee[i][1])
    pieedt.append(piee[i][0])
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 使用指定的汉字字体类型（此处为黑体）
plt.pie(pieedt, labels=pieename, autopct='%1.2f%%')
plt.title('全年空气污染情况饼图')
plt.savefig('pie.jpg')
