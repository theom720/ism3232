# my_main.py
# Author: Theo Major

from change_queue import ChangeQueue
from my_assistant import PizzaAssistant
from my_tool import PizzaOrderLookup, PizzaToolbox
from ollama_model import OllamaModel

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Pepe, a friendly pizza-order assistant for Tony's Pizza.
Answer in one short sentence.
Tony's Pizza is open from 11 am to 10 pm every day.
Gluten-free crust is available in medium size only.
Only state facts that appear in these instructions or in tool results.
If the customer only says hello, greet them and ask how you can help.
If you do not know, say you do not know and offer to pass the customer to a team member."""

ORDERS = {
    "P100": {"status": "in the oven", "address": "14 Bay Road"},
    "P101": {"status": "out for delivery", "address": "3 Gull Lane"},
    "P102": {"status": "delivered", "address": "88 Pier Street"},
}

order_tool = PizzaOrderLookup(ORDERS)
change_queue = ChangeQueue(order_tool)
tools = PizzaToolbox(order_tool, change_queue)
model = OllamaModel(MODEL_NAME)
assistant = PizzaAssistant("Pepe", INSTRUCTIONS, tools, model)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

print("Team review")
for request in change_queue.waiting():
    number = request["number"]
    print(f"Request {number}: {request['order_id']} to {request['new_address']}")
    answer = input("Approve? yes or no: ")
    if answer == "yes":
        print(change_queue.approve(number))
    else:
        print(change_queue.reject(number))

for order_id in ORDERS:
    print(order_id, ORDERS[order_id]["address"])
