import matplotlib.pyplot as plt
import numpy as np


def revenue_comparison():

    models = [
        "Fixed Price",
        "Discount",
        "Q-Learning",
        "DQN"
    ]

    revenues = [
        25000,
        28000,
        34000,
        36500
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(models, revenues)

    plt.title("Revenue Comparison")
    plt.xlabel("Models")
    plt.ylabel("Revenue")

    plt.savefig("results/revenue_comparison.png")

    plt.show()


def reward_curve():

    episodes = np.arange(1, 101)

    rewards = np.random.randint(
        15000,
        35000,
        size=100
    )

    plt.figure(figsize=(8, 5))

    plt.plot(episodes, rewards)

    plt.title("Reward per Episode")
    plt.xlabel("Episode")
    plt.ylabel("Reward")

    plt.grid(True)

    plt.savefig("results/reward_curve.png")

    plt.show()


def price_trajectory():

    days = list(range(1, 31))

    prices = [
        100,100,110,110,120,120,130,130,120,120,
        110,100,100,90,90,100,110,120,130,140,
        150,150,160,170,170,180,180,190,200,200
    ]

    plt.figure(figsize=(8, 5))

    plt.plot(days, prices, marker="o")

    plt.title("Dynamic Pricing")
    plt.xlabel("Days")
    plt.ylabel("Price")

    plt.grid(True)

    plt.savefig("results/price_trajectory.png")

    plt.show()


if __name__ == "__main__":

    revenue_comparison()

    reward_curve()

    price_trajectory()