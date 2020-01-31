import random
import time


def shuffle(n):
    return random.randint(1, n)


print("===================================================")
print("=============_(≥∇≤)ノ 경 품 추 첨 =================")
print("===================================================")
time.sleep(1)

n = int(input('참여하는 인원을 알려주세요: '))
lucky = 0
while True:
    print("셔")
    time.sleep(1)
    print("　플")
    time.sleep(1)
    print("　　링")
    time.sleep(1)
    print("　　　중")
    time.sleep(1)
    print("　　　　.")
    time.sleep(1)
    print("　　　　　.")
    time.sleep(1)
    print("　　　　　　.")
    time.sleep(1)
    lucky = shuffle(n)

    again = input('다시 섞을까요? [y/n]')

    if again != "y":
        break
    else:
        print("""
            ╭┈┈┈┈╯   ╰┈┈┈╮

             ╰┳┳╯    ╰┳┳╯
            """, end = '')
        time.sleep(1)
        print("""
              N 　    　N
        """, end = '')
        time.sleep(1)
        print("""
             ○  　    　○
        """, end = '')
        time.sleep(1)
        print("""
                 ╰┈┈╯
        """, end = '')
        time.sleep(1)
        print("""
              O ╭━━━━━╮　 O
        """, end = '')
        time.sleep(1)
        print("""
                  ┈┈┈┈
        """, end = '')
        time.sleep(1)
        print("""
            　o     　　 o
        """)

print('경품 당첨자는')
time.sleep(1)
print("두")
time.sleep(1)
print("　구")
time.sleep(1)
print("　　두")
time.sleep(1)
print("　　　구")
time.sleep(1)

print("""
...Λ＿Λ
（ㆍωㆍ)つ━☆*。
⊂　　 ノ 　　　.바
　し-Ｊ　　　°。로 *´¨)""", end='')
time.sleep(1)
print("""
　　　　　　..　.· ´¸.·바*´¨) ¸.·*¨)
　　　　　　　　　　(¸.·´ (로¸.'*
""", end='')
time.sleep(1)
print("""
                             ＿人人人人＿
                            ＞ {} 번!!! ＜
                             ￣Y^Y^Y^Y￣
""".format(str(lucky)))