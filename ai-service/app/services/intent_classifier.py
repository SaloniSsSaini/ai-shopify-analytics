def classify_intent(question: str):
    q = question.lower()

    if "inventory" in q or "stock" in q:
        return {"intent": "inventory", "metric": "units_sold", "days": 30}

    if "top" in q or "selling" in q:
        return {"intent": "sales", "metric": "revenue", "days": 7}

    if "customer" in q:
        return {"intent": "customers", "metric": "repeat_orders", "days": 90}

    return {"intent": "sales", "metric": "units_sold", "days": 30}
