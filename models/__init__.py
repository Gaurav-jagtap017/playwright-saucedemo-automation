import random

class RandomStrategy:
    def __init__(self, seed=42):
        random.seed(seed)

    def pick_products(self, products, count):
        products.sort(key=lambda p: p.price, reverse=True)
        return random.sample(products[:5], count)
