import random

import matplotlib.pyplot as plt

HEADS = 'HEADS'
TAILS = 'TAILS'
EXPECTED_FLIPS = [HEADS, TAILS] * 5


class Coin:
    def __init__(self):
        self.sides = [HEADS, TAILS]

    def flip(self) -> str:
        return random.choice(self.sides)


def run_trial():
    coin = Coin()
    num_flips = 0
    actual_flips = []
    while True:
        for flip in range(len(EXPECTED_FLIPS)):
            actual_flips.append(coin.flip())
            num_flips += 1
        if actual_flips == EXPECTED_FLIPS:
            return num_flips
        actual_flips = []


def simulation(num_trials: int):
    result = []
    for trial in range(num_trials):
        result.append(run_trial())
    plt.plot(result)
    plt.show()


simulation(100000)
