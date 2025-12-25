def build_plan(intent: dict):
    return {
        "intent": intent["intent"],
        "metric": intent["metric"],
        "days": intent.get("days", 30)
    }
