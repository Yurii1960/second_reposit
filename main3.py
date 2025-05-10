import re
def normalize_phone(phone_number):

    pattern=r"\d+"
    normal_tel=re.findall(pattern,phone_number)
    
    result="".join(normal_tel)
    if len(result)==12:
        telef="+ " +result
        
    elif len(result)==10:
        telef="+38 " +result
   


    else:
        print("Перевірте номер телефону")
    
    return telef





