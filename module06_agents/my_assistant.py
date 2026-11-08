# my_assistant.py
# Author: Theo Major

HANDOFF_WORDS = ["refund", "cancel", "complaint"]


class PizzaAssistant:
    """A pizza assistant. Rules handle what must be right. A model handles the rest."""

    def __init__(self, name, instructions, order_tool, model):
        """Set up the assistant with its name, instructions, tool, model, and history."""
        self.name = name
        self.instructions = instructions
        self.order_tool = order_tool
        self.model = model
        self.history = []

    def respond(self, user_message):
        """Record the user's message, choose a reply, record it, and return it."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Use a rule when one applies. Otherwise ask the model."""
        text = user_message.lower()
        if self.needs_human(text):
            return "I can't help with that here. I'm passing you to a team member."
        if "order" in text:
            return self.order_reply(user_message)
        return self.model_reply()

    def model_reply(self):
        """Ask the model for a reply. Give a safe answer if the model has none."""
        reply = self.model.reply(self.instructions, self.history)
        if reply is None:
            return "Sorry, I can't answer that right now. Please try again in a moment."
        return reply

    def needs_human(self, text):
        """Return True if the message is about something a person must handle."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def order_reply(self, user_message):
        """Use the order tool to answer a question about a pizza order."""
        order_id = self.order_tool.find_order_id(user_message)
        if order_id is None:
            return "Which order? Please send an order ID like P100."
        status = self.order_tool.find_status(order_id)
        return f"Order {order_id} is {status}."
