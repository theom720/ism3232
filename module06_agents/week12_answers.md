# Week 12 answers

## Exercise 1
1. "I want to change my shipping address", "It's order A102", "9 Pine Street, Tampa"

2. Two were refused. The first invented the order ID A100, which the customer never typed, so customer_said rejected it. The second had a real order ID (A102) but a made-up address (123 Main St), so it was rejected on the address. The third used A102 and 9 Pine Street, Tampa — both typed by the customer — so it passed and was filed for staff.

3. 14. The history holds 10 entries (the 9 shown plus "thanks"). decide() adds the system message and turns each of the 3 tool entries into 2 messages: 1 system + 4 user + 3 assistant + (3 tool × 2) = 14.

4. The handoff rule looks for "card" anywhere in the message, and "gift cards" contains "card", so it goes to a human before the model sees it. That's acceptable because a false alarm only costs a short wait, while matching only the whole word "card" would miss "Can I pay by card?" and could put real payment details in front of the model. For a rule that protects payments, the cheap mistake is better.

## Exercise 3
With `return True` added as the first line of `customer_said`, the check was
turned off. I ran `python3 main.py` and only typed "I want to change my
shipping address" — I never gave an order ID or a new address. Output:

You: I want to change my shipping address
Sunny: Your request to change the shipping address for order A100 has been submitted and will require staff approval.
You: quit
Messages in this conversation: 3
Staff review
Request 1: A100 to 123 Main St, Anytown, AN 12345

With the check off, the model invented both the order ID (A100) and the address
(123 Main St, Anytown, AN 12345) and filed a request for details I never typed.
After the exercise I removed the `return True` line so `customer_said` works
normally again, and all 35 tests pass.
