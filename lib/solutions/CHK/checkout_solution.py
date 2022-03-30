# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter


OFFERS = {
    "A": [(5, 200), (3, 130)],
    "B": (2, 45),
}

ITEM_PRICES = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
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
    special_offer_items = [sku for sku in skus if sku in SPECIAL_OFFERS.keys()]
    total_cost = 0

    for item in special_offer_items:
        item_count = item_counts[item]
        item_count_for_offer, free_item = SPECIAL_OFFERS[item]
        offer_items = min(item_count // item_count_for_offer, item_counts[free_item])
        item_counts[free_item] -= offer_items

    for item, count in item_counts.items():
        unaccounted_items = count

        while unaccounted_items:

            if item in OFFERS and count >= OFFERS[item][0]:
                offer_count, offer_price = OFFERS[item]
                normal_items_count = count % offer_count
                total_cost += (normal_items_count * ITEM_PRICES[item]) + (
                    (count - normal_items_count) / offer_count
                ) * offer_price
            else:
                total_cost += count * ITEM_PRICES[item]

    return total_cost
