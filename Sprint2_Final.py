"""This project was created for calculated cash or callories."""

from typing import Optional
import datetime as dt


class Record:
    """This module provedes more conveniently create records."""
    
    def __init__(self, amount: int, comment: str, date: Optional[str]=None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%M.%Y').date()


class Calculator:
    """This module takes a calorie/cash limit and stores it."""
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.records = []
  
    def add_record(self, record):
        print(self.record)
    
    def get_today_stats(self):
        print(self.records)


        
        


# class CaloriesCalculator(Calculator):
#     """
#     This is a calorie calculator. Module can keep a record of meals, Count
#     calories eaten,determine the calories left for today, sum up the calories
#     for the last week.
#     """
    
#     def __init__(self, limit) -> None:
#         super().__init__(limit)
       
        
        
#     def get_today_stats():
#         pass
#     def get_calories_remained():
#         pass
#     def get_week_stats():
#         pass

r1 = Record(amount=691, comment='Катание на такси', date='08.03.2019')
r=Calculator(1000)
f=Calculator.add_record(691)

# class CashCalculator:
#     ...

# # создадим калькулятор денег с дневным лимитом 1000
# cash_calculator = CashCalculator(1000)

# # дата в параметрах не указана,
# # так что по умолчанию к записи
# # должна автоматически добавиться сегодняшняя дата
# cash_calculator.add_record(Record(amount=145, comment='кофе'))
# # и к этой записи тоже дата должна добавиться автоматически
# cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# # а тут пользователь указал дату, сохраняем её
# cash_calculator.add_record(Record(amount=3000,
#                                   comment='бар в Танин др',
#                                   date='08.11.2019'))

# print(cash_calculator.get_today_cash_remained('rub'))
# # должно напечататься
# # На сегодня осталось 555 руб 