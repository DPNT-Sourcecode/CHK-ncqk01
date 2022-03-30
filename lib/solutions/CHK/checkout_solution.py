# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter
from itertools import combinations


ITEM_PRICES = {
    "A": [(5, 200), (3, 130), (1, 50)],
    "B": [(2, 45), (1, 30)],
    "C": [(1, 20)],
    "D": [(1, 15)],
    "E": [(1, 40)],
    "F": [(1, 10)],
    "G": [(1, 20)],
    "H": [(10, 80), (5, 45), (1, 10)],
    "I": [(1, 35)],
    "J": [(1, 60)],
    "K": [(2, 120), (1, 70)],
    "L": [(1, 90)],
    "M": [(1, 15)],
    "N": [(1, 40)],
    "O": [(1, 10)],
    "P": [(5, 200), (1, 50)],
    "Q": [(3, 80), (1, 30)],
    "R": [(1, 50)],
    "S": [(1, 20)],
    "T": [(1, 20)],
    "U": [(1, 40)],
    "V": [(3, 130), (2, 90), (1, 50)],
    "W": [(1, 20)],
    "X": [(1, 17)],
    "Y": [(1, 20)],
    "Z": [(1, 21)],
}

# items with special offers
SPECIAL_OFFERS = {
    "E": (2, "B"),
    "F": (3, "F"),
    "U": (4, "U"),
    "N": (3, "M"),
    "R": (3, "Q"),
}

GROUP_DISCOUNTS = ("Z", "S", "T", "Y", "X")

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
    group_discount = 0

    group_item_counts = Counter(item for item in item_counts if item in GROUP_DISCOUNTS)
    if (sum(group_item_counts.values()) >= 3):
        grouped_items = [char for char in skus if char in GROUP_DISCOUNTS]
        grouped_items_count = len(grouped_items) // 3 * 3
        group_combinations = combinations(grouped_items, grouped_items_count)
        max_discount = 0
        for i in range(len(group_combinations)):
            combintation = group_combinations[i]
            combination_price = sum(ITEM_PRICES[item][-1][-1] for item in combintation)
            combination_discount = combination_price - (grouped_items_count//3 * 45)
            max_discount = max(max_discount, )

        # def grouped_items_combinations(grouped_items, combinations, current_combination=[]):
        #     if len(combinations) == len(grouped_items) // 3:
        #         group_combinations.append(combinations)

        #     for char in grouped_items:
        #         current_combination.append(char)
        #         grouped_items_combinations(grouped_items.remove(char), )
        #         current_combination.remove(char)

        # grouped_items_combinations(grouped_items, group_combinations)

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

    print('totalcost, group discount',total_cost, group_discount)
    return total_cost - group_discount

