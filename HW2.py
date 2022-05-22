import collections.abc
from functools import  reduce
def composeStr(L1,L2):
    return [L1[x-1] for x in L2]
def composeLst(L):
    return [dict(L)[n1] if n1 in dict(L).keys() else n2 for n1,n2 in enumerate([-1000 for u in range(reduce(max,[x for x ,y in L])+1)])]
def newLst(L):
    return [reduce(min,[y for x,y in L]) for  u in range (reduce(max,[x for x,y in L])+1)]
def newLst2(L):
    return [int(y/2)  if x%2==0 and y%2==0 else [y,y] if y%2==1 or x%2==1  else y for x,y in enumerate(L) ]
def newFunc(n):
    return [reduce(lambda i, j: i + j, map(lambda i: list(
        filter(None, map(lambda j: (j % 2 == 0 and j + 5) or (j % 3 == 0 and j // 2) or (j % 5 == 2 and j), range(i)))),range(n)))]

def sum_div(number):
    divisors = [1]
    for i in range(2, number):
        if (number % i)==0:
            divisors.append(i)
    return True if sum(divisors)>number else False

def generate_Q6_A(list):
    yield [i for i in list if sum_div(i) is True]

def genrate_Q6_B(list):
    return (i for i in list if sum_div(i) is True)

class genrate_Q6_C:
       def __init__(self,List):
           self.List=list
           self.i=0
       def __next__(self,List):
           if(sum_div(self.List[self.i])):
               self.i+=1
               return self.List[self.i]
           else:
               raise StopIteration


def generate_Q7_A(tup1,tup2,tup3):
    hours=tup1[0]
    minutes=tup[1]
    sec=tup[2]
    while(hours<tup2[0] and minutes<tup2[1] and sec<tup2[2]):

        def gen(tup1, tup2, tup3):
            hour = tup1[0]
            min = tup1[1]
            sec = tup1[2]
            while (hour < tup2[0] or (hour == tup2[0] and min < tup2[1]) or (
                    hour == tup2[0] and min == tup2[1] and sec == tup2[2])):
                if (hour >= 24):
                    hour -= 24
                if (min >= 60):
                    min -= 60
                if (sec >= 100):
                    sec -= 100
                yield (hour, min, sec)
                hour += tup3[0]
                min += tup3[1]
                sec += tup3[2]
            yield tup2

        class Gen(collections.abc.Iterator):

            def __init__(self, tup1, tup2, tup3):
                self.hour = tup1[0]
                self.min = tup1[1]
                self.sec = tup1[2]
                self.tup1 = tup1
                self.tup2 = tup2
                self.tup3 = tup3

            def __iter__(self):
                return self

            def __next__(self):
                if (self.hour < self.tup2[0] or (self.hour == self.tup2[0] and self.min < self.tup2[1]) or (
                        self.hour == self.tup2[0] and self.min == self.tup2[1] and self.sec == self.tup2[2])):
                    self.hour += self.tup3[0]
                    self.min += self.tup3[1]
                    self.sec += self.tup3[2]
                    return (self.hour, self.min, self.sec)
                else:
                    raise StopIteration
def Question8(m, n):
    if m < n:
        return lambda : funcA(m + 1, n - 1)
    elif m == n:
        return lambda : print("m == n")
    else:
        return lambda : lambda : print(m + n)
def Question9(n):
    if n == 0:
        print("the end")
    else:
        return lambda : funcB(n - 1)



if __name__ == '__main__':
    print(sum_div.__code__.co_argcount)
    L=[(4,9),(0,2),(1,4),(3,2)]
    L2=[10,12,34,36]
