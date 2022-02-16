class StrategyManager:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def run_strategy(self, args1):
        if self.strategy is None:
            print("Strategy not exists")
        else:
            self.strategy.run_strategy(args1)


class HdStrategy(StrategyManager):
    def run_strategy(self, args1):
        print(f"Downloading Video in {args1} quality")


def main():
    no_strategy = StrategyManager()
    no_strategy.run_strategy("")

    StrategyManager(HdStrategy().run_strategy("HD"))


if __name__ == "__main__":
    main()
