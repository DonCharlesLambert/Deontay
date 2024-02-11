from enum import Enum
from strategies.logos import SOL_IMAGE, BITCOIN_IMAGE, ETH_IMAGE, USDT_IMAGE
from tsanalytics.nominalreturns import NominalReturnsCalculator
from tsanalytics.sharperatio import SharpeRatioCalculator
from tsanalytics.percentagereturns import PercentageReturnsCalculator
from tsanalytics.maxdrawdown import MaxDrawdownCalculator
from strategies.alphazero import AlphaZero
from strategies.retraceentry import RetraceEntry
from strategies.earlybird import EarlyBird


class Assets(Enum):
    BITCOIN = "BTC-USD"
    ETHEREUM = "ETH-USD"
    SOLANA = "SOL-USD"
    TETHER = "USDT-USD"

ASSET_IMAGE_MAP = {
    Assets.SOLANA: SOL_IMAGE,
    Assets.BITCOIN: BITCOIN_IMAGE,
    Assets.ETHEREUM: ETH_IMAGE,
    Assets.TETHER: USDT_IMAGE,
}

ASSET_NAME_MAP = {
    Assets.SOLANA: "SOL",
    Assets.BITCOIN: "BTC",
    Assets.ETHEREUM: "ETH",
    Assets.TETHER: "UST",
}


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
    DETAILS = "details"
    DATA = "data"
    
STRATEGIES = [AlphaZero, RetraceEntry, EarlyBird]
ANALYTICS = [
    NominalReturnsCalculator,
    SharpeRatioCalculator,
    PercentageReturnsCalculator,
    MaxDrawdownCalculator
]
