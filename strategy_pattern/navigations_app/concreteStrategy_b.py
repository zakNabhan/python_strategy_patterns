from strategy import Strategy


class ConcreteStrategyB(Strategy):

    def __init__(self):
        pass

    def execute_strategy(self):
        print("Concrete Strategy B.....")
