from strategy import Strategy


class ConcreteStrategyA(Strategy):

    def __init__(self):
        pass

    def execute_strategy(self):
        print("Concrete Strategy A.....")
