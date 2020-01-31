import random
import time

def shuffle(n):
    return random.randint(1, n)

n = int(input('참여하는 인원을 알려주세요: '))
lucky = shuffle(n)

print('■□□□□')
time.sleep(1)
print('■■□□□')
time.sleep(1)
print('■■■□□')
time.sleep(1)
print('■■■■□')
time.sleep(1)
print('■■■■■')
time.sleep(1)
print(lucky, ' 번입니다! ＼(ご▽ご*)/')