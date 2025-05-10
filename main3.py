import re
phone_number="    +38 (050)A789988"
pattern=r"\d+"
normal_tel=re.findall(pattern,phone_number)
print(normal_tel)
result="".join(normal_tel)
if len(result)==12:
    telef="+ " +result
    print(telef)
elif len(result)==10:
    telef="+38  " +result
    print(telef)


else:
      print("Перевірте номер телефону")



print(result,len(result))
