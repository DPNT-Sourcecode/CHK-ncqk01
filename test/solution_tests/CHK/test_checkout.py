from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_solution_handles_illegal_input(self):
        assert checkout_solution.checkout(1) == -1
        assert checkout_solution.checkout("a") == -1

    def test_checkout_solution_without_offers(self):
        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_solution_with_offers(self):
        assert checkout_solution.checkout("ABCDAA") == 195
        assert checkout_solution.checkout("ABCDAAAA") == 265
        assert checkout_solution.checkout("ABCDAAAAB") == 280

    def test_checkout_solution_with_special_offers(self):
        assert checkout_solution.checkout("ABCDEE") == 165
        assert checkout_solution.checkout("ACDEE") == 165
        assert checkout_solution.checkout("ABBCDEE") == 195
        assert checkout_solution.checkout("ABBCDEEFFFFFF") == 235

    def test_checkout_solution_with_group_discount(self):
        assert checkout_solution.checkout("STY") == 45
        assert checkout_solution.checkout("STYX") == 62
        assert checkout_solution.checkout("STXSTX") == 90
        assert checkout_solution.checkout("ABCDEFGHIJKLMNOPQRSTUVW") == 795

