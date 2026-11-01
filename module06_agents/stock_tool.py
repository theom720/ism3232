# stock_tool.py
# Author: Theo Major


class StockLookup:
    """A tool that knows product stock counts. It knows nothing about chatting."""

    def __init__(self, stock):
        """Store the stock counts this tool can look up."""
        self.stock = stock

    def find_product(self, text):
        """Return the first known product named in the text, or None."""
        for product in self.stock:
            if product in text.lower():
                return product
        return None

    def count_for(self, product):
        """Return the count for one product, or None if it is not stocked."""
        if product in self.stock:
            return self.stock[product]
        return None
