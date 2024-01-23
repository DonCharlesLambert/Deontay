
from enum import Enum

class Coins(Enum):
    BITCOIN = "BTC"

class DateFormats():
    CSV = "%Y-%m-%d %H:%M:%S"
    API = "%Y-%m-%d"

class Params():
    SYMBOL = "symbol"
    START_DATE = "startDate"
    END_DATE = "endDate"

class MarketDataColumns:
    UNIX = "unix"
    DATE = "date"
    SYMBOL = "symbol"
    OPEN ="open"
    HIGH = "high"
    LOW = "low"
    CLOSE = "close"

MARKET_DATA_MAP = {
    Coins.BITCOIN: 'data/BTC-Daily.csv'
}