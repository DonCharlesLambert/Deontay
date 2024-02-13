
import unittest
import mock
import pandas as pd
from datetime import datetime
from tsanalytics.const import Offsets
from tsanalytics.lib import BaseAnalyticCalculator
from tsanalytics.maxdrawdown import MaxDrawdownCalculator
from tsanalytics.nominalreturns import NominalReturnsCalculator
from tsanalytics.percentagereturns import PercentageReturnsCalculator
from tsanalytics.sharperatio import SharpeRatioCalculator

def mockPriceData():
    data = {'Date': ["2020-02-12", "2020-02-11", "2022-02-10", "2022-02-09"], 'Close': [10, 20, 30, 40]}
    for i, date_string in enumerate(data['Date']):
        data['Date'][i] = datetime.strptime(date_string, "%Y-%m-%d")
    return pd.DataFrame.from_dict(data)

class TestBaseTimeseriesAnalytics(unittest.TestCase):
    def test_getOffsets(self):
        baseCalc = BaseAnalyticCalculator("testStrat", {})
        offsets = baseCalc._getOffsets()
        self.assertEqual([offset.value for offset in offsets], ["All", "1Y", "6M", "1M"])

    def test_run(self):
        baseCalc = BaseAnalyticCalculator("testStrat", {})
        baseCalc._sliceEquityCurve = mock.MagicMock()
        baseCalc._run = mock.MagicMock()
        baseCalc._storeInCache = mock.MagicMock()
        numOffsets = len(baseCalc._getOffsets())

        baseCalc.run()
        self.assertEqual(baseCalc._sliceEquityCurve.call_count, numOffsets)
        self.assertEqual(baseCalc._run.call_count, numOffsets)
        self.assertEqual(baseCalc._storeInCache.call_count, 1)

    @mock.patch("tsanalytics.lib.datetime")
    def test__sliceEquityCurve(self, mockDatetime):
        curve = mockPriceData()
        mockDatetime.now.return_value = datetime(2022, 2, 12)
        baseCalc = BaseAnalyticCalculator("testStrat", curve)
        baseCalc._storeInCache = mock.MagicMock()
        res = baseCalc._sliceEquityCurve(Offsets.ONE_MONTH, curve)
        res.reset_index(drop=True, inplace=True)
        expected = pd.DataFrame.from_dict({
            'index': [2, 3],
            'Date': [datetime.strptime("2022-02-10", "%Y-%m-%d"), datetime.strptime("2022-02-09", "%Y-%m-%d")],
            'Close': [30, 40]
        })

        self.assertEqual(res.to_dict(), expected.to_dict())
        
    @mock.patch("tsanalytics.lib.open")
    def test__storeInCache(self, mockFileRead):
        curve = mockPriceData()
        baseCalc = BaseAnalyticCalculator("testStrat", curve)
        baseCalc._storeInCache(curve.to_csv(), "TestAnalytic", jsonDump=True)
        self.assertEqual(mockFileRead.call_count, 1)

class TestAnalyticCalculators(unittest.TestCase):
    def test_maxDrawdown(self):
        data = {
            'Date': ["2022-02-09","2022-02-10", "2022-02-11", "2022-02-12", "2022-02-13", "2022-02-14"],
            'Equity': [10, 20, 10, 40, 30, 21]
        }
        for i, date_string in enumerate(data['Date']):
            data['Date'][i] = datetime.strptime(date_string, "%Y-%m-%d")
        curve = pd.DataFrame.from_dict(data)
        maxDD = MaxDrawdownCalculator("", {})._run(curve)
        self.assertEqual(maxDD, -50)
        
        name = MaxDrawdownCalculator("", {})._getAnalyticName()
        self.assertEqual(name, "Max Drawdown")

    def test_nominalReturns(self):
        data = {
            'Date': ["2022-02-09","2022-02-10", "2022-02-11", "2022-02-12", "2022-02-13", "2022-02-14"],
            'Equity': [10, 20, 10, 40, 30, 21]
        }
        for i, date_string in enumerate(data['Date']):
            data['Date'][i] = datetime.strptime(date_string, "%Y-%m-%d")
        curve = pd.DataFrame.from_dict(data)
        nReturns = NominalReturnsCalculator("", {})._run(curve)
        self.assertEqual(nReturns, 11)
        
        name = NominalReturnsCalculator("", {})._getAnalyticName()
        self.assertEqual(name, "Nominal Returns")

    def test_percentageReturns(self):
        data = {
            'Date': ["2022-02-09","2022-02-10", "2022-02-11", "2022-02-12", "2022-02-13", "2022-02-14"],
            'Equity': [10, 20, 10, 40, 30, 21]
        }
        for i, date_string in enumerate(data['Date']):
            data['Date'][i] = datetime.strptime(date_string, "%Y-%m-%d")
        curve = pd.DataFrame.from_dict(data)
        pReturns = PercentageReturnsCalculator("", {})._run(curve)
        self.assertEqual(pReturns, 110)
        
        name = PercentageReturnsCalculator("", {})._getAnalyticName()
        self.assertEqual(name, "Percentage Returns")

    def test_sharpeRatio(self):
        data = {
            'Date': ["2022-02-09","2022-02-10", "2022-02-11", "2022-02-12", "2022-02-13", "2022-02-14"],
            'Equity': [10, 20, 10, 40, 30, 21]
        }
        for i, date_string in enumerate(data['Date']):
            data['Date'][i] = datetime.strptime(date_string, "%Y-%m-%d")
        curve = pd.DataFrame.from_dict(data)
        sharpeR = SharpeRatioCalculator("", {})._run(curve)
        self.assertEqual(sharpeR, 0.69)

        name = SharpeRatioCalculator("", {})._getAnalyticName()
        self.assertEqual(name, "Sharpe Ratio")


if __name__ == '__main__':
    unittest.main()