import random
import math

def redpacket(people_num, money):
    allocation = []
    money = money * 100
    remain_money = money
    for i in range(people_num - 1):
        # up=math.ceil((remain_money-(people_num-i))/2)   #剩余所有（/2），给别人留一分钱
        up = min(math.ceil(remain_money / (people_num - i) * 2), remain_money - (people_num - i))  # 剩余均值*2
        x = random.randint(1, up)
        remain_money -= x
        allocation.append(x)
    allocation.append(remain_money)
    allocation = [i / 100 for i in allocation]
    print(allocation)

redpacket(10, 10)
redpacket(10, 100)
