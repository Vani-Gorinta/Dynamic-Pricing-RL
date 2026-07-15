from config import *


class FixedPriceAgent:

    def choose_price(self):
        return INITIAL_PRICE


class DiscountAgent:

    def __init__(self):
        self.price = MAX_PRICE

    def choose_price(self):
        current_price = self.price

        self.price = max(
            MIN_PRICE,
            self.price - PRICE_CHANGE
        )

        return current_price