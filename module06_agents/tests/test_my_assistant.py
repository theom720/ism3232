# tests/test_my_assistant.py
# Author: Theo Major

from change_queue import ChangeQueue
from fake_model import FakeModel
from my_assistant import PizzaAssistant
from my_tool import PizzaOrderLookup, PizzaToolbox


def make_assistant(model):
    """Build a fresh pizza assistant with its own tools and the given model."""
    orders = {
        "P100": {"status": "in the oven", "address": "14 Bay Road"},
        "P101": {"status": "out for delivery", "address": "3 Gull Lane"},
    }
    order_tool = PizzaOrderLookup(orders)
    tools = PizzaToolbox(order_tool, ChangeQueue(order_tool))
    return PizzaAssistant("Pepe", "Be friendly.", tools, model)


def ask_for_tool(name, arguments):
    """Build the decision a model returns when it wants a tool."""
    return {"tool": name, "arguments": arguments}


def test_tool_looks_up_a_known_order():
    order_tool = PizzaOrderLookup({"P100": {"status": "in the oven", "address": "x"}})
    assert order_tool.look_up_order("P100") == "Order P100 is in the oven."


def test_model_can_ask_for_the_lookup_tool():
    model = FakeModel(
        [
            ask_for_tool("look_up_order", {"order_id": "P100"}),
            {"text": "Your order P100 is in the oven."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Where is order P100?")
    assert assistant.history[1]["content"] == "Order P100 is in the oven."


def test_made_up_address_is_refused():
    model = FakeModel(
        [
            ask_for_tool(
                "request_address_change",
                {"order_id": "P100", "new_address": "123 Main St"},
            ),
            {"text": "What is the new address?"},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Please change the address on order P100")
    assert "has not given that address" in assistant.history[1]["content"]
    assert assistant.tools.change_queue.waiting() == []


def test_address_change_waits_for_a_person():
    model = FakeModel(
        [
            ask_for_tool(
                "request_address_change",
                {"order_id": "P100", "new_address": "9 Pine Street"},
            ),
            {"text": "Sent to the team."},
        ]
    )
    assistant = make_assistant(model)
    assistant.respond("Change the address on order P100 to 9 Pine Street")
    assert len(assistant.tools.change_queue.waiting()) == 1
    assert assistant.tools.order_tool.orders["P100"]["address"] == "14 Bay Road"


def test_refund_goes_to_a_human():
    assistant = make_assistant(FakeModel([]))
    assert "team member" in assistant.respond("I want a refund")
