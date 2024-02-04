
from enum import Enum
from media.logos import ALPHA_LOGO, RETRACE_LOGO, BIRD_LOGO

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

STRATEGIES = {
    "Alpha Zero": {
        "imagesrc": ALPHA_LOGO,
        "name": "Alpha Zero",
        "description": "Dollar-cost average strategy for a bitcoin believer.",
        "data": {
            "offsets": ["All", "1Y", "6M", "1M"],
            "analytics": {
                "nominalReturns": {"All": 17585.15, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "percentageReturns": {"All": -0.25, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "sharpeRatio": {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "maxDrawdown": {"All": 9.84, "1Y": 27.2, "6M": 2.0, "1M": 0}
            },
            "timeseries": { "All": [
                ["Day", "", "", "", ""],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
              ]
            }
        },
        #need another key "data" which is a dict with keys
            # offsets: [All, 1Y, 6M, 1M]
            # analytics: {sharpeRatio: {All: a, 1Y: x, 6M: y, 1M: z}, maxDrawdown: {All: a, 1Y: x, 6M: y, 1M: z}}
            # trades: [{direction: BUY, entryTime: today, exitTime: yesterday, size: 1.0, returns: 0.2},...]
            # timeseries: timeseries of price changes with high, low, open and close
    },
    "Retrace Entry": {
        "imagesrc": RETRACE_LOGO,
        "name": "Retrace Entry",
        "description": "Trend-following strategy entering on retracement.",
        "data": {
            "offsets": ["All", "1Y", "6M", "1M"],
            "analytics": {
                "nominalReturns": {"All": 22493.48, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "percentageReturns": {"All": 0.25, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "sharpeRatio": {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "maxDrawdown": {"All": 9.1, "1Y": 27.2, "6M": 2.0, "1M": 0}
            },
            "timeseries": { "All": [
                ["Day", "", "", "", ""],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
              ]
            }
        }
    },
    "Early Bird": {
        "imagesrc": BIRD_LOGO,
        "name": "Early Bird",
        "description": "Anticipates trends through reversal patterns.",
        "data": {
            "offsets": ["All", "1Y", "6M", "1M"],
            "analytics": {
                "nominalReturns": {"All": 19577.01, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "percentageReturns": {"All": -0.14, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "sharpeRatio": {"All": 3.7, "1Y": 6.5, "6M": 9.1, "1M": 9.4},
                "maxDrawdown": {"All": 9.1, "1Y": 27.2, "6M": 2.0, "1M": 0}
            },
            "timeseries": { "All": [
                ["Day", "", "", "", ""],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
                ["Mon", 20, 28, 38, 45],
                ["Tue", 31, 38, 55, 66],
                ["Wed", 50, 55, 77, 80],
                ["Thu", 77, 77, 66, 50],
                ["Fri", 68, 66, 22, 15],
              ]
            }
        }
    }
}
