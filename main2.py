import random

def get_numbers_ticket(min,max,quantity):
    if min<=0:
        print("мінімальне значення повинно бути більшим нуля")
        return []
    elif quantity<=0: 
        print("Кількість номерів повинна бути більшим нуля")
        return []

    elif max<min+quantity :

        print(f"максимальне значення повинно бути більшим {min+quantity}")
        return []
    elif max>1000:
        
        print("Максимальне значення повинно бути менше 1000")
        return []
    else:
        num=[]
        for i in range(min,max+1):
            num.append(i)
        numbers=random.sample(num,quantity)
        numbers.sort()
        return numbers
print(get_numbers_ticket(10,1005,3))
                         

