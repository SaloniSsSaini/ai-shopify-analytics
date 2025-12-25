def process_data(raw_data, intent):
    daily_sales = raw_data["total_units"] / 30

    return {
        "daily_sales": int(daily_sales),
        "suggested_reorder": int(daily_sales * 7),
        "low_stock_products": raw_data.get("low_stock_products", [])
    }
