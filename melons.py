"""Classes for melon orders."""


class AbstractMelonOrder:
    """An abstract base class that domestic & international melon orders will 
    inherit from"""

    def __init__(self, species, qty, country_code=None):
        """Initialize base melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = .08

    # def __init__(self):
    #     """Initialize melon order attributes."""
    #     super().__init__()


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
    #     super().__init__(country_code)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
