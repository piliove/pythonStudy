'''引入随机数'''
import random

guess = str(random.randint(1,10))
print("随机数字:" + guess)

print("-------------欢迎来到我的互动小程序------------")
print("                猜数字互动游戏                 ")
guess_number = int(input("请你随意输入一个数字吧!"))
while guess_number != 5:
    guess_number = int(input("哎呀！猜错了，请你重新输入一个数字"))
    if guess_number == 8:
        print("真棒！答案正确")
        print("恭喜，恭喜~~~~~~~~")
    else:
        if guess_number > 8:
            print("猜的数字偏大")
        else:
            print("猜的数字偏小")
