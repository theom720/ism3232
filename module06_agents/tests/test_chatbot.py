# tests/test_chatbot.py
# Author: Theo Major

from chatbot import SupportChatbot
from order_tool import OrderLookup
from stock_tool import StockLookup


def make_bot():
    """Build a chatbot with known order and stock tools for testing."""
    order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
    stock_tool = StockLookup({"rain jacket": 12})
    return SupportChatbot(
        "Sunny", "You are a friendly support assistant.", order_tool, stock_tool
    )


def test_find_order_id_found():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_order_id("where is a100?") == "A100"


def test_find_order_id_missing():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_order_id("where is my order?") is None


def test_find_status_found():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A100") == "shipped"


def test_find_status_missing():
    tool = OrderLookup({"A100": "shipped"})
    assert tool.find_status("A999") is None


def test_hello_reply():
    bot = make_bot()
    assert (
        bot.respond("hello") == "Hello! I'm Sunny. I can check an order status for you."
    )


def test_order_status_reply():
    bot = make_bot()
    assert bot.respond("Where is order A100?") == "Order A100 is shipped."


def test_handoff_reply():
    bot = make_bot()
    assert (
        bot.respond("Please change my shipping address")
        == "I can't help with that here. I'm passing you to a human agent."
    )


def test_history_grows_by_two():
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2


def test_count_user_messages():
    bot = make_bot()
    bot.respond("hello")
    bot.respond("Where is order A100?")
    assert bot.count_user_messages() == 2


def test_stock_question_uses_the_tool():
    bot = make_bot()
    assert (
        bot.respond("Is the rain jacket in stock?")
        == "We have 12 of the rain jacket in stock."
    )
