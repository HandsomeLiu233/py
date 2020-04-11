import pandas as pd

old_url=r'http://data.eastmoney.com/cjsj/grossdomesticproduct.aspx?p='


for i in range(1,4):
    url=old_url+str(i)
    data=pd.read_html(url,header=0, encoding='gbk')[0]
    print(data)
    data.to_csv('resultxxx.csv', mode='a', header=True, encoding="gbk")