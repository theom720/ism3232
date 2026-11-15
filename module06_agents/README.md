# Module 6 — Pizza Order Assistant (Mini-Project)

Pepe is a mock support assistant for Tony's Pizza. It answers one kind of question — the status of a pizza order — by looking the order ID up in a separate tool (`PizzaOrderLookup`), and it records every message in a conversation history. It is a mock in two ways: its replies come from simple keyword `if` rules instead of an AI model, and its order data is a small dictionary typed into the file instead of a real ordering system. Requests about refunds, cancellations, or complaints are passed to a human team member, because those actions move money or change an order and should not be done automatically by a bot. If this used real customer data, the history would store everything a customer types — including something like an address or phone number typed by accident — so that history would need to be protected and not kept longer than necessary.

## Week 11 — Local Model

The model answered the closing-time question well by saying Tony's Pizza closes at 10 pm.
It also correctly stated that gluten-free crust is available in medium size only.
When asked whether the restaurant delivers outside five miles, it said it did not know because that fact was not provided.
I kept order status in the order tool because it must come from current order data.
I kept refund requests in code because they can change business records and should be handled by a team member.

## Week 12 — Pepe with tools, guardrails, and approval

Pepe now lets the model choose when to use a tool instead of relying on keyword
rules. One request the model handled well: "Where is order P100?" — the model
asked for the look_up_order tool and answered "Order P100 is in the oven" from
the tool result. One request the door refused: when I said "I want to change my
delivery address" with no details, the model tried to file a change with an
order ID and address I had never typed, and the PizzaToolbox refused it until I
gave the real values, which then waited in the queue for staff approval. The one
instruction I had to add was "If the customer only says hello, greet them and
ask how you can help," because without it the model sometimes tried to use a
tool on a plain greeting. Refund, cancel, and complaint messages still go
straight to a team member before the model ever sees them.
