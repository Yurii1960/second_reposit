from datetime import *
while True:
    

    date=input('Введіть дату в форматі :YYYY-MM-DD   ')

    
    def get_days_from_today(date):

        data_time=datetime.strptime(date, '%Y-%m-%d')
        today=datetime.today()
        difference_days=(today-data_time)
    
        return int(difference_days.days)
    try:
        result=get_days_from_today(date)
        print(f"До вашої дати залишилось = {-result} дні ")
        break
    except ValueError:
        print("Введіть правильно дату   ")    



