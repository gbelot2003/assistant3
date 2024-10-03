import re

class IntentService:
    def __init__(self, prompt):
        self.prompt = prompt

    def detect_intent(self):
        intents = [
            r"quiero agendar una entrega",
            r"necesito una caja entregada",
            r"agendar entrega",
            r"quiero agendar una caja",
            r"agendar una entrega",
        ]

        for intent in intents:
            if re.search(intent, self.prompt, re.IGNORECASE):
                return "schedule_delivery"

        return None