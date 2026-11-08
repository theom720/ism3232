# tests/test_chatbot.py
# Author: Theo Major

from chatbot import SupportChatbot
from echo_model import EchoModel
from mock_model import MockModel
from order_tool import OrderLookup
from stock_tool import StockLookup


class SilentModel:
    """A model that never has an answer. It stands in for Ollama being switched off."""

    def reply(self, instructions, history):
        return None


def make_bot():
    """Build a fresh chatbot with its own tools and a mock model for each test."""
    order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
    stock_tool = StockLookup({"rain jacket": 12, "day pack": 0})
    return SupportChatbot("Sunny", "Be friendly.", order_tool, stock_tool, MockModel())


def make_bot_with_silent_model():
    """Build a chatbot whose model never answers."""
    order_tool = OrderLookup({"A100": "shipped", "A101": "processing"})
    stock_tool = StockLookup({"rain jacket": 12, "day pack": 0})
    return SupportChatbot(
        "Sunny", "Be friendly.", order_tool, stock_tool, SilentModel()
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
    assert bot.respond("hello") == "Hello! How can I help you today?"


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


def test_other_messages_go_to_the_model():
    bot = make_bot()
    assert bot.respond("hello") == "Hello! How can I help you today?"


def test_safe_reply_when_the_model_has_no_answer():
    bot = make_bot_with_silent_model()
    assert "try again" in bot.respond("hello")


def test_order_rule_does_not_need_the_model():
    bot = make_bot_with_silent_model()
    assert bot.respond("Where is order A100?") == "Order A100 is shipped."


def test_handoff_rule_does_not_need_the_model():
    bot = make_bot_with_silent_model()
    assert "human" in bot.respond("Please change my shipping address")


def test_echo_model_repeats_last_message():
    order_tool = OrderLookup({})
    stock_tool = StockLookup({})
    bot = SupportChatbot(
        "Echo", "Repeat the user.", order_tool, stock_tool, EchoModel()
    )
    assert bot.respond("good morning") == "You said: good morning"
