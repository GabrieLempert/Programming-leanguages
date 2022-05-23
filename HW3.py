from functools import  reduce
import math

def q_1(list_of_functions):
    return  list(filter(lambda fun:func.__code__.co_argcount <=1,list_of_functions))
def q_2(list_of_numbers):
    return reduce((lambda x,y:x+y),list_of_numbers)
def q_3(num):
   return (list(filter(lambda x: (pow(x,2) == num), [i for i in range(num + 1)])))[0] if len((list(filter(lambda x: (pow(x,2) == num), [i for i in range(num + 1)])))) > 0 else 0
def q_4(sentences):
    return len(list(filter(lambda x:"Sam" in x,sentences)))
def q_5_a(func):
    my_tuple = []
    def wrapper(*args,**kwargs):
        number=args[0]
        result=func(*args,**kwargs)
        if len(my_tuple)==0:
            my_tuple.append(number)
            my_tuple.append(result)
        else:
            my_tuple[0]=(my_tuple[0]+number)/2
            my_tuple[1]=(my_tuple[1]+result)/2
        tuple(my_tuple)
        print("The avg arg in is "+str(my_tuple[0])+'\n'+"The avg results are "+str(my_tuple[1]))
    return wrapper
def q_5_b(func):
    def wrapper(*args, **kwargs):
        print()
    return wrapper

def q_6(func):
    q_6.func_list = []
    def wrapper(*args,**kwargs):
        just_list=q_6.func_list
        if len(just_list) < 2:
            just_list.append(func.__name__)
        if len(just_list) >= 2:
            just_list.append(func.__name__)
            print(str(just_list)+" Those are the last 3 functions that ran")
            just_list.pop()
            return func(*args,**kwargs)

    return wrapper
@q_6
def succ(x):
    return x + 1
@q_6
def gabi(y=4):
    return 15+y
@q_6
def roni(y):
    return y+4

if __name__ == '__main__':
    succ(4)
    succ(3)
    succ(2)
    gabi()
    roni(14)


