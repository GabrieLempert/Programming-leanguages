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
        value=func(*args,**kwargs)
        wrapper.calls+=1
        if args.__len__() >1:
             print(func.__name__+"("+str(args)+")"+f" returns {value}")
        if args.__len__()==1 and kwargs.__len__()==0:
            print(func.__name__ + "(" + str(args[0]) + ")"+f" returns {value}")
        if kwargs.__len__()>1:
            print(func.__name__ + "(" + str(kwargs) + ")"+f" returns {value}")
        if args.__len__()==0 and kwargs.__len__()<1:
            print(func.__name__ + "(" + str(kwargs[0]) + ")"+f" returns {value}")
        return func(*args,**kwargs)
    wrapper.calls = 0
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

#Question Number 7
class Twitter:
    def __init__(self,name):
        self.name=name
        self.followers=set()
        self.follows= set()
    def update(self,tweet,name):
        print('Sent Tweet To {} the message is "{}"'.format(name,tweet))
    def follow(self,follows):
        self.follows.add(follows)
        follows.followers.add(self.name)
        return follows
    def tweet(self,tweet):
        for followers in self.followers:
          self.update(tweet,followers)

#Question Number 8:
""""""""
#In f1 you can't enter None value to pass through the arguments and in f2
#You can pass and append an None argument into the function
""""""""
def f1(x, y=[]):
    y.append(x)
    return sum(y)


def f2(x, y=None):

    if y is None:
        y = []
    y.append(x)
    return sum(y)

#Question9
class a:
    def __init__(self, y):
        self.y = y

    def __call__(self, z):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z


class b(a):
    def __call__(self, z=-2):
        if z > self.y:
            return z - self.y
        else:
            return self.y - z



def q_10_a(func):
    q_10_a.number_passed=0
    def wrapper(*args,**kwargs):
        wrapper.count+=args.__len__()+kwargs.__len__()
        wrapper.calls+=1
        counter=wrapper.count
        calls=wrapper.calls
        q_10_a.number_passed +=1
        print(f"This function was called {calls}\nand number of argunmets passed is:{counter}\n Number of functions passed in decorator {q_10_a.number_passed}")

    wrapper.count=0
    wrapper.calls=0
    return  wrapper

def q_10_b(func):
    q_10_b.number_passed=0
    q_10_b.args_type=dict()
    def wrapper(*args,**kwargs):
        wrapper.count+=args.__len__()+kwargs.__len__()
        wrapper.calls+=1
        counter=wrapper.count
        calls=wrapper.calls
        q_10_a.number_passed +=1
        value=func(*args,**kwargs)
        if q_10_b.args_type.keys().__contains__(type(value)):
            q_10_b.args_type[type(value)]+=1
        else:
            q_10_b.args_type[type(value)]=1
        for type_of in q_10_b.args_type:
            print("Type", type_of.__name__, ",Used:",q_10_b.args_type.get(type_of))
        print(f"This function was called {calls}\nand number of argunmets passed is:{counter}\n Number of functions passed in decorator {q_10_a.number_passed}")

    wrapper.count=0
    wrapper.calls=0
    return  wrapper
"""""""""
In java functions arent objects so you can't use them .
So, in it can't be implemented in java.
"""""""""

@q_10_b
def succ(x):
    return x + 1
@q_10_b
def gabi(y=4):
    return 15+y
@q_10_b
def roni(y):
    return y+4
@q_10_b
def func(*args):
    return 3 + len(args)
@q_10_a
def func1(**kwargs):
    return 3 + len(kwargs)

if __name__ == '__main__':
    succ(2)
    succ(2)
    gabi(3)
    roni(2)
    func(5,2,3)
    func1(y=5,c=2)
    print(a(5)(b(6)()))
    print(a(6)(b(5)(6)))
    a = Twitter('Alice')
    k = Twitter('King')
    q = Twitter('Queen')
    h = Twitter('Mad Hatter')
    c = Twitter('Cheshire Cat')
    a.follow(c).follow(h).follow(q)
    k.follow(q)
    q.follow(q).follow(h)
    h.follow(a).follow(q).follow(c)
    print(f'==== {q.name} tweets ====')
    q.tweet('Off with their heads!')
    print(f'\n==== {a.name} tweets ====')
    a.tweet('What a strange world we live in.')
    print(f'\n==== {k.name} tweets ====')
    k.tweet('Begin at the beginning, and go on till you come to the end: then stop.')
    print(f'\n==== {c.name} tweets ====')
    c.tweet("We're all mad here.")
    print(f'\n==== {h.name} tweets ====')
    h.tweet('Why is a raven like a writing-desk?')







