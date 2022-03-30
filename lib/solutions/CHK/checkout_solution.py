

# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter


OFFERS = {
    'A': (3, 130),
    'B': (2, 45),
}

ITEM_PRICES = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

def checkout(skus):
    if not skus:
        return -1

    item_counts = Counter(skus)
    total_cost = 0

    for item, count in item_counts.items():
        if item in OFFERS and count >= OFFERS[item][0]:
            offer_count, offer_price = OFFERS[item]
            normal_items_count = count % offer_count
            total_cost += (normal_items_count * ITEM_PRICES[item]) + ((count - normal_items_count) / offer_count) * offer_price
        else:
            total_cost += count * ITEM_PRICES[item]



    return total_cost

