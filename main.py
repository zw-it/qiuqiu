# class Solution(object):
#     def multiply(self, num1, num2):
#         """
#         :type num1: str
#         :type num2: str
#         :rtype: str
#         """
#         n,m=len(num1),len(num2)
#         result=[0]*(n+m)
#         for j in range(m-1,-1,-1):
#             n1=int(num2[j])
#             for i in range(n-1,-1,-1):
#                 n2=int(num1[i])
#                 now=n1*n2+result[i+j+1]
#                 result[i+j+1]=now%10
#                 result[i+j]+=now//10
#         i=0
#         while i<len(result) and result[i]==0:
#             i+=1
#         return ''.join(map(str,result[i:]))
# num1='3'
# num2='2'
# A=Solution()
# product=A.multiply(num1,num2)
# print(product)
import time


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1
#         elif l1.val < l2.val:
#             l1.next = self.mergeTwoLists(l1.next, l2)
#             return l1
#         else:
#             l2.next = self.mergeTwoLists(l1, l2.next)
#             return l2
#
# l1 = []
# l2 = [0]
# A=Solution()
# B=A.mergeTwoLists(l1,l2)

# aa=[]
# def Da(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     a,b=0,1
#     for _ in range(2,n+1):
#         a,b=b,a+b
#         aa.append(b)
#     return aa
# print(Da(10))
#
# from random import randint
# def allin(n):
#     number=0
#     for _ in range(n):
#         number+=randint(1,6)
#     return number
# print(allin(6))

# def add(*args):
#     number=0
#     for numbers in args:
#         number+=numbers
#     return number
# print(add(1,3,5,4,6))

# s1 = 'hello, world!'
# s2 = "hello, world!"
# # 以三个双引号或单引号开头的字符串可以折行
# s3 = """
# hello,
# world!
# """
# print(s1, s2, s3, end='')

# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')

# b=[]
# def aa(n):
#     a,b=0,1
#     for _ in range(n):
#         a,b=b,a+b
#         yield b
#
# def main():
#     for val in aa(20):
#         print(val)
# if __name__=='__main__':
#     main()
#
# import os
# import time
# #
# #
# # def main():
# #     content = '北京欢迎你为你开天辟地…………'
# #     while True:
# #         # 清理屏幕上的输出
# #         os.system('cls')  # os.system('clear')
# #         print(content)
# #         # 休眠200毫秒
# #         time.sleep(1)
# #         content = content[1:] + content[0]
# #
#
# # if __name__ == '__main__':
# #     main()
# #
#
# # def main():
# #     val='秋秋大王驾到，通通闪开!!!!'
# #     while True:
# #         os.system('cls')
# #         print(val)
# #         time.sleep(0.2)
# #         val=val[1:]+val[0]
# # if __name__=='__main__':
# #     main()
# import random
# def aa(code_len=4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     code=''
#     for _ in range(code_len):
#         index=random.randint(0,len(all_chars)-1)
#         code+=all_chars[index]
#     return code
#
# print(aa())


# def main():
#     persons=[True]*30
#     count,index,number=0,0,0
#     while count<15:
#         if persons[index]:
#             number+=1
#             if number==9:
#                 count+=1
#                 persons[index]=False
#                 number=0
#         index+=1
#         index%=30
#     for person in persons:
#         print('基督教信徒' if person else '非基督教信徒',end=',')
# if __name__=='__main__':
#     main()


class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def study(self,book):
        print('%s正在学习%s'%(self.name,book))
    def watch_movie(self):
        if self.age<18:
            print('%s未满十八岁只可以观看《熊出没》'% self.name)
        else:
            print('%s已满十八岁可以观看《羞羞小电影》'%self.name)

def main():
    study1=Student('秋秋',0.5)
    study2=Student('姗姗',18)
    study1.study('《如何烹饪狗界美食》')
    study2.study('《如何运营好keep账号》')
    study1.watch_movie()
    study2.watch_movie()

if __name__=='__main__':
    main()
from time import time,sleep,localtime
class Olock(object):
    @classmethod
    def now(cls):
        ctime=localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min,ctime.tm_sec)
    def __init__(self,h,m,s):
        self.s=s
        self.m=m
        self.h=h
    def run(self):
        self.s+=1
        if self.s==60:
            self.s=0
            self.m+=1
            if self.m==60:
                self.m=0
                self.h+=1
                if self.h==24:
                    self.h=0
    def show(self):
        return '%02d:%02d:%02d' %\
            (self.h,self.m,self.s)


def main():
    t=Olock.now()
    while True:
        print(t.show())
        time.sleep(1)
        t.run()
if __name__ == '__main__':
    main()




from math import sqrt

class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def move_to(self,x,y):
        self.x+=x
        self.y+=y
    def move_by(self,dx,dy):
        self.x+=dx
        self.y+=dy
    def move_len(self,other):
        dx=other.x-self.x
        dy=other.x-self.y
        return sqrt(dx**2+dy**2)
    def __str__(self):
        return'(%s,%s)'%(str(self.x),str(self.y))
def main():
    p1=Point(1,1)
    p2=Point()
    print(p1)
    print(p2)
    p2.move_by(3,-10)
    print(p2)
    print(p1.move_len(p2))

if __name__ == '__main__':
    main()

class Play():
    def __init__(self,name,age):
        self._name=name
        self._age=age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,age):
        self._age=age
    def paly(self):
        if self.age<=18:
            print('%s在玩斗地主'% self.name)
        else:
            print('%s在玩飞行棋'% self.name)

def main():
    p1=Play('qq',0.5)
    p2=Play('ss',18)
    p1.paly()
    p2.paly()
    p1.age=25
    p1.paly()
if __name__ == '__main__':
     main()

