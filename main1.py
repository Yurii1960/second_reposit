from datetime import *

    


    
def get_days_from_today(date):
     while True:
        date=input('Введіть дату в форматі :YYYY-MM-DD   ')


        data_time=datetime.strptime(date, '%Y-%m-%d')
        today=datetime.today()
        difference_days=(today-data_time)
    
        
        try:
           result=int(difference_days.days)

           print(f"До вашої дати залишилось = {-result} дні ")
           return int(difference_days.days)

           break
        except ValueError:
            print("Введіть правильно дату    ")    



                          

