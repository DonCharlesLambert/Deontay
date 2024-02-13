import unittest
import mock
import pandas as pd
from datetime import datetime
from base.backend import StrategiesBackend, BacktestBackend, AssetBackend

def mockStrat():
    mockStrategy = mock.MagicMock()
    mockStrategy.image.return_value = "base64"
    mockStrategy.name.return_value = "Test Strategy"
    mockStrategy.description.return_value = "This is a strategy for testing"
    mockStrategy.detail.return_value = []
    mockStrategy.data.return_value = {}

    backtestResult = mock.MagicMock()
    backtestResult._equity_curve = {"tuesday": 0, "wednesday": 9999}
    mockStrategy.backtest.return_value = backtestResult
    return lambda : mockStrategy

def mockPriceData():
    data = {'Dates': ["2022-02-12", "2022-02-11", "2022-02-10", "2022-02-09"], 'Close': [10, 20, 30, 40]}
    return pd.DataFrame.from_dict(data)

class TestStrategiesBackend(unittest.TestCase):
    def test_getStrategies(self):
        strategies = [mockStrat()]
        with mock.patch("base.backend.STRATEGIES", strategies):
            res = StrategiesBackend().getStrategies()
            self.assertEqual(type(res), dict)
            self.assertEqual("Test Strategy" in res.keys(), True)
            self.assertEqual(res["Test Strategy"]["description"], "This is a strategy for testing")


class TestBacktestBackend(unittest.TestCase):
    def test_dailyBacktest(self):
        strategies = [mockStrat()]
        with mock.patch("base.backend.STRATEGIES", strategies):
            with mock.patch("tsanalytics.lib.BaseAnalyticCalculator.run") as runAnalytic:
                res = BacktestBackend().dailyBacktest()
                self.assertEqual(runAnalytic.call_count, 4) # once for each ts analytic


class TestAssetBackend(unittest.TestCase):
    @mock.patch("base.backend.yfinance.download", return_value=mockPriceData())
    @mock.patch("base.backend.open")
    @mock.patch("base.backend.datetime")
    def test_getAssets_noCache(self, mockDatetime, mockStoreInCache, mockFinanceApi):
        mockDatetime.now.return_value = datetime(2022, 2, 12)

        backend = AssetBackend()
        backend._getFromCache = mock.MagicMock()
        backend._getFromCache.return_value = None

        res = backend.getAssets()
        self.assertEqual(type(res), dict)
        self.assertEqual(res["BTC-USD"]["price"], 30)

    @mock.patch("base.backend.pd.read_csv")
    @mock.patch("base.backend.datetime")
    def test_getAssets_useCache(self, mockDatetime, mockCacheRead):
        mockCacheRead.return_value = mockPriceData()
        mockDatetime.now.return_value = datetime(2022, 2, 12)

        backend = AssetBackend()
        res = backend.getAssets()
        self.assertEqual(mockCacheRead.call_count, 4) # once for each asset
        self.assertEqual(type(res), dict)
        self.assertEqual(res["BTC-USD"]["price"], 30)


if __name__ == '__main__':
    unittest.main()