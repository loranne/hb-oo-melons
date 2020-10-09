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

        if self.species == "Christmas Melon":
            base_price = base_price * 1.5

        
        fee = 0
        if self.order_type == "international" and self.qty < 10:
            fee += 3

 
        total = ((1 + self.tax) * self.qty * base_price) + fee

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = .08

    # def __init__(self):
    #     """Initialize melon order attributes."""
    #     super().__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty, country_code)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the US Govt"""
    order_type = "domestic"
    tax = 0
    passed_inspection = False
    

    def mark_inspection(self):
        self.passed_inspection = True

