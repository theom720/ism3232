# echo_model.py
# Author: Theo Major


class EchoModel:
    def reply(self, instructions, history):
        last_message = history[-1]["content"]
        return "You said: " + last_message
