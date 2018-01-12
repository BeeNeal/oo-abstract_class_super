"""Classes for melon orders."""

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        # attributes in dunder init are instance attributes, and are on the instance itself

        self.species = species
        self.qty = qty
        self.shipped = False


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "Christmas":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price


        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17


    def __init__(self, species, qty, country_code):
        """Initialize International melon order attributes."""

        self._country_code = country_code
        super(InternationalMelonOrder, self).__init__(species, qty)


    def get_country_code(self):
        """Return the country code."""

        return self._country_code


    def get_total(self):
        """Calculate price, including tax, for international orders."""

        total = super(InternationalMelonOrder, self).get_total()

        if self.qty < 10:
            total += 3

        return total


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order"""

    order_type = "government"
    tax = 0.0
    passed_inspection = False


    def mark_inspection():
        pass
