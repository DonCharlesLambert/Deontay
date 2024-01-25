import pandas as pd
from datetime import datetime
from const import Coins, DateFormats, MARKET_DATA_MAP, MarketDataColumns

class MarketDataBackend():
    def __init__(self):
        self.marketData = {}
        for coin in Coins:
            symbol = str(coin.value)
            marketDataPath = MARKET_DATA_MAP[coin]
            self.marketData[symbol] = pd.read_csv(marketDataPath)

    def getMarketData(self, symbol, startDate=None, endDate=None):
        startDate = self._stringToDate(startDate) or datetime(2022, 2, 1)
        endDate = self._stringToDate(endDate) or datetime(2022, 3, 1)
        filteredData = self.marketData[symbol][self.marketData[symbol].apply(self._dateFilter, args=(startDate, endDate), axis=1)]
        jsonData = filteredData.to_json()
        return jsonData

    def _dateFilter(self, row, startDate, endDate):
        dateObj = self._stringToDate(row[MarketDataColumns.DATE], DateFormats.CSV)
        return startDate <= dateObj <= endDate
    
    def _stringToDate(self, dateString, dateFormat=None):
        if not dateString: return None
        dateFormat = dateFormat or DateFormats.API
        return datetime.strptime(dateString, dateFormat)
