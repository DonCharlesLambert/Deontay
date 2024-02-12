from enum import Enum

# repeated -- switch occurrences to use base.const
class Assets():
    BITCOIN = "BTC-USD"
    
class DataEnum():
    OFFSETS = "offsets"
    ANALYTICS = "analytics"
    TIMESERIES = "timeseries"
    TRADES = "trades"

    NOMINAL_RETURNS = "nominalReturns"
    PERCENTAGE_RETURNS = "percentageReturns"
    SHARPE_RATIO = "sharpeRatio"
    MAX_DRAWDOWN = "maxDrawdown"