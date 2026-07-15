import gymnasium as gym
from gymnasium import spaces
import numpy as np
from config import *


class DynamicPricingGymEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.max_inventory = MAX_INVENTORY
        self.max_days = MAX_DAYS

        # State:
        # [remaining inventory, days left]
        self.observation_space = spaces.Box(
            low=np.array([0, 0]),
            high=np.array([MAX_INVENTORY, MAX_DAYS]),
            dtype=np.float32
        )

        # Actions:
        # 0 = Decrease
        # 1 = Same
        # 2 = Increase
        self.action_space = spaces.Discrete(3)

        self.reset()

    def reset(self, seed=None, options=None):

        super().reset(seed=seed)

        self.inventory = MAX_INVENTORY
        self.days_left = MAX_DAYS
        self.price = INITIAL_PRICE

        state = np.array(
            [self.inventory, self.days_left],
            dtype=np.float32
        )

        return state, {}

    def step(self, action):

        if action == 0:
            self.price -= PRICE_CHANGE

        elif action == 2:
            self.price += PRICE_CHANGE

        self.price = max(
            MIN_PRICE,
            min(MAX_PRICE, self.price)
        )

        demand = max(
            1,
            20 - (self.price // 10)
        )

        sold = min(demand, self.inventory)

        self.inventory -= sold

        reward = sold * self.price

        self.days_left -= 1

        terminated = (
            self.inventory == 0 or
            self.days_left == 0
        )

        truncated = False

        state = np.array(
            [self.inventory, self.days_left],
            dtype=np.float32
        )

        return (
            state,
            reward,
            terminated,
            truncated,
            {}
        )