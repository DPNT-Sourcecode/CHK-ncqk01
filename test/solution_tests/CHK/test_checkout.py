from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_solution_handles_illegal_input(self):
        assert checkout_solution.checkout("") == -1
        assert checkout_solution.checkout(1) == -1

    def test_checkout_solution_without_offers(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_solution_with_offers(self):

        assert checkout_solution.checkout("ABCDAA") == 195
        assert checkout_solution.checkout("ABCDAAAA") == 295
        assert checkout_solution.checkout("ABCDAAAAB") == 310


