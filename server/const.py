
from tsanalytics.nominalreturns import NominalReturnsCalculator
from tsanalytics.sharperatio import SharpeRatioCalculator
from tsanalytics.percentagereturns import PercentageReturnsCalculator
from tsanalytics.maxdrawdown import MaxDrawdownCalculator
from strategies.alphazero import AlphaZero
from strategies.retraceentry import RetraceEntry
from strategies.earlybird import EarlyBird

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
ANALYTICS = [
    NominalReturnsCalculator,
    SharpeRatioCalculator,
    PercentageReturnsCalculator,
    MaxDrawdownCalculator
]
