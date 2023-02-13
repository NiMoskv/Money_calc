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
        self.records.append(record)
        print(self.records, 'It is records')
    
    def get_today_stats(self):
        for item in self.records:
            if item.date == dt.datetime.now().date():
                amount_sum += item.amount
        
        return amount_sum

    def get_week_stats(self):
        for day in range (len(self.records)-1, len(self.records)-8):
            summary_value += day.amount
        
        return summary_value


class CaloriesCalculator(Calculator):
    """///"""
    def __init__(self, limit: int) -> None:
        super().__init__(limit)

    def get_calories_remained(self):
        if self.get_today_stats()<self.limit:
            return f'Сегодня можно съесть что-нибудь еще, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал'
        
        return 'Хватит есть!'


class CashCalculator:
    """"""
    def __init__(self, limit) -> None:
        super().__init__(limit)
    
    def get_today_cash_remainder(self, currency:str = 'rub'):
        remaining_money = self.limit - self.get_today_stats()
        usd=73
        eur=78
        if currency =='usd':
            remaining_money = round((remaining_money / usd),2)
        elif currency == 'eur':
            remaining_money = round((remaining_money / eur),2)

        if self.get_today_stats()<self.limit:
            return f'На сегодня осталось {remaining_money} {currency}'
        elif self.get_today_stats() == self.limit:
            return 'Денег нет, держись брат'
        else:
            return f'Денег нет, держись: Твой долг {remaining_money}{currency}'

            



# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
# # должно напечататься
# # На сегодня осталось 555 руб 