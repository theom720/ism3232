# my_main.py
# Author: Theo Major

from my_assistant import PizzaAssistant
from my_tool import PizzaOrderLookup

ORDERS = {
    "P100": "in the oven",
    "P101": "out for delivery",
    "P102": "delivered",
}

order_tool = PizzaOrderLookup(ORDERS)
assistant = PizzaAssistant(
    "Pepe",
    "You are a friendly pizza order assistant for Tony's Pizza.",
    order_tool,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
