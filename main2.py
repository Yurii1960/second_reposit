import random


def get_numbers_ticket(min,max,quantity):
    if min<=0:
        print("мінімальне значення повинно бути більшим нуля")
    elif quantity<=0: 
        print("Кількість номерів повинна бути більшим нуля")
    elif max<=min+quantity:
        print(f"максимальне значення повинно бути більшим {min+quantity}")
    else:

       

        num=[]
        for i in range(min,max+1):
            num.append(i)
        numbers=random.sample(num,quantity)
        numbers.sort()
        return numbers


