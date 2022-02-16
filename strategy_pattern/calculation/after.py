class StrategyExecutor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def execute(self, arg1, arg2):
        if self.strategy is None:
            print("Strategy not implemented")
        else:
            self.strategy.execute(arg1, arg2)


class AdditionStrategy(StrategyExecutor):
    def execute(self, arg1, arg2):
        print(arg1 + arg2)


class SubtractionStrategy(StrategyExecutor):
    def execute(self, arg1, arg2):
        print(arg1 - arg2)


def main():
    no_strategy = StrategyExecutor()
    no_strategy.execute(3, 6)
    StrategyExecutor(AdditionStrategy().execute(10, 5))
    StrategyExecutor(SubtractionStrategy().execute(90, 3))


if __name__ == "__main__":
    main()
