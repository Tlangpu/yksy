import time

# 输入倒计时时间
t = int(input("Enter the time in seconds: "))

# 开始倒计时
while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

# 倒计时结束，提示音
print('Time is up!')
