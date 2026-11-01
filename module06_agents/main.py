# main.py
# Author: Theo Major

from order_tool import OrderLookup
from chatbot import SupportChatbot

order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
bot = SupportChatbot("Sunny", "You are a friendly support assistant.", order_tool)

print(bot.respond("hello"))
print(bot.respond("Where is order A100?"))
print(bot.respond("Please change my shipping address"))
