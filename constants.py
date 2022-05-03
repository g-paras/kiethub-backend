import datetime
from typing import List

def year_choces() -> List[int]:
    _cy = datetime.date.today().year
    return [i for i in range(1998, _cy+1)]

DATE_CHOICES = [(i, j) for i, j in enumerate(year_choces())]