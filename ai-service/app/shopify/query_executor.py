from app.shopify.client import ShopifyClient

def execute_query(store_id, token, query):
    client = ShopifyClient(store_id, token)
    return client.run_query(query)
