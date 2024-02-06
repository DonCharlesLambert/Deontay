
from quant.alphazero import AlphaZero
from quant.retraceentry import RetraceEntry
from quant.earlybird import EarlyBird

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

class StrategyResponse():
    IMAGE_SRC = "imagesrc"
    NAME = "name"
    DESCRIPTION = "description"
    DATA = "data"
    
STRATEGIES = [AlphaZero, RetraceEntry, EarlyBird]
