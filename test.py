import datetime as dt
from typing import Optional

class Record:
    """This module provedes more conveniently create records."""
    
    def __init__(self, amount: int, comment: str, date:Optional[str]=None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%M.%Y').date()

def add_record(Record):
    print(Record.amount)


add_record(Record(amount=145, comment='кофе'))