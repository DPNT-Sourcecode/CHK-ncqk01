from solutions.CHK import checkout_solution


class TestCheckout:
    def test_checkout_solution_handles_illegal_input(self):
        assert checkout_solution.checkout("") == -1
        assert checkout_solution.checkout(1) == -1
