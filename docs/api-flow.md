# API Flow – Request & Response Lifecycle

---

## API Endpoint

POST /api/v1/questions

---

## Request Example

{
  "store_id": "example-store.myshopify.com",
  "question": "What were my top selling products last week?"
}

---

## Flow Steps

1. Client sends request to Rails API
2. Rails validates store and access token
3. Rails forwards request to Python AI service
4. AI agent processes the question
5. ShopifyQL query is generated and executed
6. AI agent returns a human-readable answer
7. Rails formats and returns final response

---

## Response Example

{
  "answer": "Last week, T-Shirts and Hoodies were your top sellers, with T-Shirts selling the most.",
  "confidence": "high"
}

---

## Error Handling

- Invalid store → 404
- Invalid token → 401
- No data → Graceful explanation
- Invalid query → Safe fallback message
