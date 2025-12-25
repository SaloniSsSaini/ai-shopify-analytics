def explain_result(insights):
    message = (
        f"You sell around {insights['daily_sales']} units per day. "
        f"You should reorder at least {insights['suggested_reorder']} units for next week."
    )

    if insights.get("low_stock_products"):
        message += (
            " Products at risk of stockout soon: "
            + ", ".join(insights["low_stock_products"])
        )

    return message
