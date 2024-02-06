from const import STRATEGIES, StrategyResponse
    
class StrategiesBackend():
    def __init__(self):
        pass

    def getStrategies(self):
        res = {}
        for strategy in STRATEGIES:
            res[strategy.name()] = {
                StrategyResponse.IMAGE_SRC: strategy.image(),
                StrategyResponse.NAME: strategy.name(),
                StrategyResponse.DESCRIPTION: strategy.description(),
                StrategyResponse.DATA: strategy.data()
            }
        return res
