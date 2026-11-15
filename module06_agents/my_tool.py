# my_tool.py
# Author: Theo Major


class PizzaOrderLookup:
    """A tool that knows pizza order statuses. It knows nothing about chatting."""

    def __init__(self, orders):
        """Store the pizza orders this tool can look up."""
        self.orders = orders

    def find_order_id(self, text):
        """Return the first known order ID mentioned in text, or None."""
        for order_id in self.orders:
            if order_id in text.upper():
                return order_id
        return None

    def find_status(self, order_id):
        """Return the status of one order, or None if there is no such order."""
        if order_id in self.orders:
            return self.orders[order_id]["status"]
        return None

    def look_up_order(self, order_id):
        """Look up the status of one pizza order.

        Args:
            order_id: The order ID, like P100.
        """
        found = self.find_order_id(order_id)
        if found is None:
            return "No order with that ID was found. Order IDs look like P100."
        return f"Order {found} is {self.find_status(found)}."

    def change_address(self, order_id, new_address):
        """Change the delivery address on one order. Only an approval calls this."""
        self.orders[order_id]["address"] = new_address


class PizzaToolbox:
    """Every tool request from the model comes through here and is checked."""

    def __init__(self, order_tool, change_queue):
        """Hold the tools the model is allowed to ask for."""
        self.order_tool = order_tool
        self.change_queue = change_queue

    def tool_list(self):
        """Return the tools the model may ask for. They are not called here."""
        return [
            self.order_tool.look_up_order,
            self.change_queue.request_address_change,
        ]

    def run(self, name, arguments, history):
        """Check one tool request. Run the tool only if every check passes."""
        if name == "look_up_order":
            order_id = self.clean(arguments, "order_id")
            if order_id == "":
                return "The order ID is missing. Ask the customer for it."
            if not self.customer_said(history, order_id):
                return "The customer has not given that order ID. Ask them for it."
            return self.order_tool.look_up_order(order_id)
        if name == "request_address_change":
            order_id = self.clean(arguments, "order_id")
            new_address = self.clean(arguments, "new_address")
            if order_id == "" or new_address == "":
                return "The order ID and the new address are both needed."
            if not self.customer_said(history, order_id):
                return "The customer has not given that order ID. Ask them for it."
            if not self.customer_said(history, new_address):
                return "The customer has not given that address. Ask them for it."
            return self.change_queue.request_address_change(order_id, new_address)
        return f"There is no tool named {name}."

    def clean(self, arguments, key):
        """Return one argument as text without extra spaces, or "" if it is missing."""
        return str(arguments.get(key, "")).strip()

    def customer_said(self, history, text):
        """Return True if text appears in a message the customer typed."""
        for message in history:
            if message["role"] == "user" and text.lower() in message["content"].lower():
                return True
        return False
