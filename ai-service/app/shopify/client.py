import requests

class ShopifyClient:
    def __init__(self, store_id, token=None):
        self.store_id = store_id

    def run_query(self, query):
        # DummyJSON API call
        response = requests.get("https://dummyjson.com/products")
        data = response.json()

        total_units = 0
        low_stock_products = []

        for product in data["products"]:
            total_units += product["stock"]

            if product["stock"] < 10:
                low_stock_products.append(product["title"])

        return {
            "total_units": total_units,
            "low_stock_products": low_stock_products
        }
