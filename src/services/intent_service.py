import re

class IntentService:
    def __init__(self, prompt):
        self.prompt = prompt

    def detect_intent(self):
        intents = {
            "schedule_delivery": [
                r"quiero agendar una entrega",
                r"necesito una caja entregada",
                r"agendar entrega",
                r"quiero agendar una caja",
                r"agendar una entrega",
            ],
            "provide_package_type": [
                r"quiero una caja de tipo (\w+)",
                r"necesito una caja de tipo (\w+)",
            ],
            "provide_delivery_time": [
                r"quiero que la entrega sea a las (\d{2}:\d{2})",
                r"necesito la entrega a las (\d{2}:\d{2})",
            ],
            "provide_address": [
                r"mi dirección es (\w+)",
                r"vivo en (\w+)",
            ],
            "provide_email": [
                r"mi email es (\w+@\w+\.\w+)",
                r"puedes contactarme en (\w+@\w+\.\w+)",
            ],
            "provide_phone": [
                r"mi teléfono es (\d+)",
                r"puedes llamarme al (\d+)",
            ],
        }

        for intent, patterns in intents.items():
            for pattern in patterns:
                match = re.search(pattern, self.prompt, re.IGNORECASE)
                if match:
                    return intent, match.groups()

        return None, None