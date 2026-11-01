# tests/test_my_assistant.py
# Author: Theo Major

from my_assistant import PizzaAssistant
from my_tool import PizzaOrderLookup


def make_assistant():
    """Build a fresh pizza assistant with its own tool for each test."""
    orders = {"P100": "in the oven", "P101": "out for delivery"}
    return PizzaAssistant("Pepe", "Be friendly.", PizzaOrderLookup(orders))


def test_tool_finds_known_status():
    tool = PizzaOrderLookup({"P100": "in the oven"})
    assert tool.find_status("P100") == "in the oven"


def test_tool_returns_none_for_unknown_order():
    tool = PizzaOrderLookup({"P100": "in the oven"})
    assert tool.find_status("P999") is None


def test_order_question_uses_the_tool():
    assistant = make_assistant()
    assert assistant.respond("Where is order P100?") == "Order P100 is in the oven."


def test_order_question_without_an_id_asks_for_one():
    assistant = make_assistant()
    assert "order ID" in assistant.respond("Where is my order?")


def test_refund_goes_to_a_human():
    assistant = make_assistant()
    assert "team member" in assistant.respond("I want a refund")


def test_unknown_request_gets_a_safe_reply():
    assistant = make_assistant()
    assert "not sure" in assistant.respond("What is the weather today?")


def test_respond_records_both_messages():
    assistant = make_assistant()
    assistant.respond("hello")
    assert len(assistant.history) == 2
