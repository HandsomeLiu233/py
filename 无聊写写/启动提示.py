import requests
import datetime

now_time = datetime.datetime.now()
response = requests.get('https://sc.ftqq.com/SCU89901T607b07ed794689a88e14c3680fe6ab395e707e48e0e97.send?text=服务器开机了，请核查原因&desp=报告消息的时间是： '+str(now_time)+'       这条提醒标志着服务器的重启，请核查是人为关闭服务器还是因为故障导致的服务器重启')


print(str(now_time))
