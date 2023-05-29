from datetime import datetime, timedelta

users = [{'Marina':datetime(year = 1995, month = 6, day = 1)},
         {'Bohdan':datetime(year = 1995, month = 3, day = 21)},
         {'Anna':datetime(year = 1997, month = 6, day = 4)},
         {'Valera':datetime(year = 1995, month = 6, day = 3)},
         {'Daria':datetime(year = 1996, month = 5, day = 28)},
         {'Daniil':datetime(year = 1996, month = 5, day = 27)},
         {'Damir':datetime(year = 2022, month = 4, day = 13)}
        ]

days = {'Monday':[],
        'Tuesday':[],
        'Wednesday':[],
        'Thursday':[],
        'Friday':[],
        'Saturday':[],
        'Sunday':[]}

delta = timedelta(weeks = 1)


def get_birthdays_per_week(users):
    
    result = []
    c_day = datetime.now().date()
    week_ahead = c_day + delta
    week_before = c_day - delta
    
    for user in users:
        
        for name, birthday in user.items():
            birthday_in_current_year = datetime(year = c_day.year, month=birthday.month, day=birthday.day).date()
            birthday_weekday = birthday_in_current_year.strftime('%A')
            
            if birthday_in_current_year >= c_day and birthday_in_current_year <= week_ahead:
                days[f'{birthday_weekday}'].append(f'{name}')
            
            
            if birthday_in_current_year < c_day and birthday_in_current_year >= week_before:
                if birthday_weekday == 'Saturday' or birthday_weekday == 'Sunday':
                    days['Monday'].append(f'{name}')
                        
    result.append(days)
    
    for i in result:
        for key, value in i.items():
            if len(value) > 0:
                print (key,':', ', '.join(value))
    
                        
get_birthdays_per_week(users)