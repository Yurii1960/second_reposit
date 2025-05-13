from datetime import *

    


    
def get_days_from_today(date):
     
    try:


       data_time=datetime.strptime(date, '%Y-%m-%d')
     
       today=datetime.today()
       difference_days=(today-data_time)
    
        
        
       result=difference_days.days

       print(f"До вашої дати залишилось  {-result} дні ")
       return difference_days.days
    except ValueError:
         print("Введіть дату згідно формату YYYY-MM-DD   ")  

     


                          

