# liste = [1,2,3,4,5]

# iterator = iter(liste) # for eyerine tek tek elemanlara ulaşma
# print(next(iterator)) # eelemanlar karşımıza teek tek geelir
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# # print(next(iterator)) # 6. eleman olmadıgı ıcın hata verir.

# for i in liste:
#     print(i)

"""
liste = [1,2,3,4,5] 
iterator = iter(liste)

while True :
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

"""

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
list = MyNumbers(20,50)

myIter = iter(list)
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter)) # kaç tane yazarsak o kadar yazar

while True:
    try:
        element = next(myIter)
        print(element)
    except StopIteration:
        break

# for x in list:
#     print(x)