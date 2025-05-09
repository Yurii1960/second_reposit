import random


def get_numbers_ticket(min,max,quantity):

    num=[]
    for i in range(min,max+1):
        num.append(i)
    numbers=random.sample(num,quantity)
    numbers.sort()
    return numbers

print(f"Ваші лоторейні числа : {get_numbers_ticket(1,49,6)}")
