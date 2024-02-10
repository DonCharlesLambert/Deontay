from enum import Enum

class Offsets(Enum):
    ALL = "All"
    ONE_YEAR = "1Y"
    SIX_MONTHS = "6M"
    ONE_MONTH = "1M"

class TimePeriod:
    YEARS = "years"
    MONTHS = "months"
