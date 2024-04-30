import random
def randInt(min= 'test'  , max=  'test' ):
    if min == 'test' and max == 'test':
        num = round(random.random() * 100)
        return num
    elif min == 'test':
        num = round(random.random() * max)
        return num
    elif max == 'test':
        num = round(random.random() * 100 + min)
        return num
    elif max>min and max>0:
        num = round(random.random() * (max - min) + min)
        return num
    
print(randInt(min = 33, max = 14))


