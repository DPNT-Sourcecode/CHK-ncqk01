# noinspection PyUnusedLocal
# skus = unicode string

from collections import Counter


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


def grouped_items_combinations(grouped_items, current=[]):



    


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

    group_discount_items = [item for item in GROUP_DISCOUNTS if item in item_counts]
    group_item_counts = Counter(item for item in item_counts if item in GROUP_DISCOUNTS)
    discount_group = set()
    while (sum(group_item_counts[item] for item in GROUP_DISCOUNTS) >= 3):
        group_combinations = []
        input_str = ""
        for char in group_item_counts.keys():
            inputstr += char * group_item_counts[char]
        # for item in list(group_discount_items):
        #     if item in item_counts:
        #         discount_group.add(item)
        #         group_item_counts[item] -= 1
        #         if group_item_counts[item] == 0:
        #             del group_item_counts[item]
        #             group_discount_items.remove(item)

        #     if len(discount_group) == 3:
        #         regular_price = sum(ITEM_PRICES[item][0][1] for item in discount_group)
        #         group_discount += regular_price - 45
        #         discount_group = set()

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
