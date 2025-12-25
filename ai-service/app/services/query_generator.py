def generate_shopifyql(plan: dict):
    return f"""
    FROM orders
    SHOW sum(line_items.quantity)
    WHERE created_at >= -{plan['days']}d
    """
