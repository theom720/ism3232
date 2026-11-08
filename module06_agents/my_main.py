# my_main.py
# Author: Theo Major

from my_assistant import PizzaAssistant
from my_tool import PizzaOrderLookup
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Pepe, a friendly pizza-order assistant for Tony's Pizza.
Answer in one short sentence.
Tony's Pizza is open from 11 am to 10 pm every day.
Gluten-free crust is available in medium size only.
Only state facts that appear in these instructions.
If you do not know, say you do not know and offer to pass the customer to a team member."""

ORDERS = {
    "P100": "in the oven",
    "P101": "out for delivery",
    "P102": "delivered",
}

order_tool = PizzaOrderLookup(ORDERS)
model = OllamaModel(MODEL_NAME)

assistant = PizzaAssistant(
    "Pepe",
    INSTRUCTIONS,
    order_tool,
    model,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")
