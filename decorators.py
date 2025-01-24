"""

def myDecorator(func):
    def wrapper(name):
        print('fonksiyondan önceki işlemler')
        func(name)
        print('fonksiyondan sonraki işlemler')
    return wrapper

@myDecorator #say helloyu mydc'ye götürüyor.
def sayHello(name):
    print('hello',name)

sayHello('ali')

"""

import math
import time

def calculateTime(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)

        func(*args, **kwargs)

        finish = time.time()
        print('fonksiyon ' + func.__name__ +str(finish - start) + 'saniye sürdü.')
    
    return inner

@calculateTime
def usalma(a,b):
     # 1 saniye beklesin öyle baslasın
    print(math.pow(a,b))

    
@calculateTime
def faktoriyel(num):
    print(math.factorial(num))

@calculateTime
def toplama(a,b):
    print(a+b)


usalma(2,3)
faktoriyel(5)
toplama(13,20)
