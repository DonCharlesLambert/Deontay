from datetime import datetime
from dateutil.relativedelta import relativedelta
from .const import Offsets, TimePeriod
import json
from copy import deepcopy
import os.path

# Make a better way to communicate with cache
PATH = os.path.split(os.path.dirname(__file__))[0]

class BaseAnalyticCalculator:
    def __init__(self, stratName, stratCurve):
        self.stratName = stratName
        self.stratCurve = stratCurve

    def _getAnalyticName(self):
        return NotImplementedError("Cannot call getAnalyticName from BaseAnalyticCalculator, implement method in subclass")

    def _getOffsets(self):
        return [offset for offset in list(Offsets)]

    def _storeInCache(self, analyticsResult):
        resultJson = json.dumps(analyticsResult)
        analyticName = self._getAnalyticName()
        cacheFolder = "cache/{}/{}.json".format(self.stratName, analyticName)
        with open(os.path.join(PATH, cacheFolder), "w") as resultFile:
            resultFile.write(resultJson)

    def _run(self, equityCurve):
        return NotImplementedError("Cannot call run from BaseAnalyticCalculator, implement method in subclass")
    
    def run(self):
        res = {}
        for offset in self._getOffsets():
            equityCurve = BaseAnalyticCalculator._sliceEquityCurve(offset, deepcopy(self.stratCurve))
            offsetRes = self._run(equityCurve)
            res[offset.value] = offsetRes
        self._storeInCache(res)

    @staticmethod
    def _sliceEquityCurve(offset, curve):
        slicedCurve = curve
        timePeriod = BaseAnalyticCalculator._offsetToTimePeriod(offset)
        if timePeriod[TimePeriod.YEARS] is not None and timePeriod[TimePeriod.MONTHS] is not None:
            periodStart = (datetime.now() - relativedelta(years=timePeriod[TimePeriod.YEARS], months=timePeriod[TimePeriod.MONTHS]))
            curve['Date'] = curve['Date'].apply(lambda dateString: datetime.strptime(dateString, "%Y-%m-%d"))
            slicedCurve = curve.loc[curve['Date'] > periodStart]
        return slicedCurve
    
    @staticmethod
    def _offsetToTimePeriod(offset):
        timePeriodMap = {
            Offsets.ALL: (None, None),
            Offsets.ONE_YEAR: (1, 0),
            Offsets.SIX_MONTHS: (0, 6),
            Offsets.ONE_MONTH: (0, 1),
        }
        timeperiod = timePeriodMap[offset]
        return {TimePeriod.YEARS: timeperiod[0], TimePeriod.MONTHS: timeperiod[1]}
