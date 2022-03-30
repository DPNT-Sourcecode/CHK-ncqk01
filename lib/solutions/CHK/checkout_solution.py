# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter


ITEM_PRICES = {
    "A": [(5, 200), (3, 130), (1, 50)],
    "B": [(2, 45), (1, 30)],
    "C": [(1, 20)],
    "D": [(1, 15)],
    "E": [(1, 40)],
}

# items with special offers
SPECIAL_OFFERS = {"E": (2, "B")}


def checkout(skus):
    if skus == "":
        return 0

    if (
        not skus
        or not isinstance(skus, str)
        or any(sku for sku in skus if sku not in ITEM_PRICES.keys())
    ):
        return -1

    item_counts = Counter(skus)
    special_offer_items = set(sku for sku in skus if sku in SPECIAL_OFFERS.keys())
    total_cost = 0

    for item in special_offer_items:
        item_count = item_counts[item]
        item_count_for_offer, free_item = SPECIAL_OFFERS[item]
        offer_items_count = min(
            item_count // item_count_for_offer, item_counts[free_item]
        )
        item_counts[free_item] -= offer_items_count

    for item, unaccounted_items in item_counts.items():
        while unaccounted_items:
            for item_count, item_price in ITEM_PRICES[item]:
                if unaccounted_items >= item_count:
                    unaccounted_items -= item_count
                    total_cost += item_price
                    break

    return total_cost








