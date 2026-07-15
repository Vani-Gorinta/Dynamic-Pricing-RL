import numpy as np
from config import *


class DynamicPricingEnvironment:

    def __init__(self):
        self.max_inventory = MAX_INVENTORY
        self.max_days = MAX_DAYS
        self.reset()

    def reset(self):
        self.inventory = self.max_inventory
        self.days_left = self.max_days
        self.price = INITIAL_PRICE

        return [
            self.inventory,
            self.days_left,
            self.price
        ]

    def step(self, action):
        """
        Actions:
        0 = Decrease Price
        1 = Keep Price Same
        2 = Increase Price
        """

        # Update Price
        if action == 0:
            self.price -= PRICE_CHANGE

        elif action == 2:
            self.price += PRICE_CHANGE

        # Keep price within limits
        self.price = max(
            MIN_PRICE,
            min(MAX_PRICE, self.price)
        )

        # -----------------------------
        # Improved Demand Model
        # -----------------------------

        base_demand = 25

        # Price effect
        price_effect = max(0, (self.price - 100) // 10)

        # More demand when fewer days are left
        time_effect = (self.max_days - self.days_left) // 5

        # Random customer behaviour
        random_effect = np.random.randint(-2, 3)

        demand = (
            base_demand
            - price_effect
            + time_effect
            + random_effect
        )

        demand = max(1, demand)

        # Units Sold
        sold = min(
            demand,
            self.inventory
        )

        self.inventory -= sold

        # Revenue
        reward = sold * self.price

        # One day passes
        self.days_left -= 1

        # Check if finished
        done = (
            self.inventory == 0 or
            self.days_left == 0
        )

        next_state = [
            self.inventory,
            self.days_left,
            self.price
        ]

        return next_state, reward, done