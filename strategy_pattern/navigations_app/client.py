from concreteStrategy_a import ConcreteStrategyA
from strategy import Strategy
from concreteStrategy_b import ConcreteStrategyB


def main():
    print("__________________Client__for__Strategies_____________________")

    none_str = Strategy()
    none_str.execute_strategy()

    str_a = Strategy(ConcreteStrategyA())
    str_a.execute_strategy()

    str_b = Strategy(ConcreteStrategyB())
    str_b.execute_strategy()


if __name__ == "__main__":
    main()
