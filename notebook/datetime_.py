import datetime
print(datetime.timedelta(days=5, hours=17, minutes=30))

today = datetime.date.today()
print(today)


import time

time.time()         #UTC기준 경과시간
time.ctime          #경과시간 문자열 변환

time.sleep()        #delay_second 함수