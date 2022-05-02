import random

random.random()     # 0.0 ~ 1.0사이의 값 반환,      보통 확률 지정으로 사용

random.randint(10, 100)     #argv1 ~ argv2사이의 int값 반환,    센서 예제에 사용

random.uniform(10, 100)     #위와 같지만 실수형으로 반환

msg = "message"
msg_list = msg.split(maxsplit=2)    #split 매개변수로 maxsplit사용가능
