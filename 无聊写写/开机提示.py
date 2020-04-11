import requests
import datetime

now_time = datetime.datetime.now()
response = requests.get('https://sc.ftqq.com/SCU89901T607b07ed794689a88e14c3680fe6ab395e707e48e0e97.send?text=主人!服务器一切运行正常~&desp=报告消息的时间是： '+str(now_time))


print(str(now_time))
