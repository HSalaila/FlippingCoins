import random

HEADS = 'HEADS'
TAILS = 'TAILS'
EXPECTED_FLIPS = [HEADS, TAILS] * 5


class Coin:
    def __init__(self):
        self.sides = [HEADS, TAILS]

    def flip(self) -> str:
        return random.choice(self.sides)


def run_trial() -> int:
    coin = Coin()
    current_flips = []
    number_flips = 0
    while current_flips != EXPECTED_FLIPS:
        number_flips += 1
        current_flips.append(coin.flip())
        if current_flips != EXPECTED_FLIPS[:len(current_flips)]:
            current_flips = []
    return number_flips


def run(num_trials: int) -> list:
    return [run_trial() for _ in range(num_trials)]


random.seed(100000)  # 100000 subscribers
result = run(1024)  # 1/1024 is the chance
