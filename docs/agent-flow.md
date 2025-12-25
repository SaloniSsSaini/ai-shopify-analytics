# Agentic Workflow – AI Reasoning Flow

This document explains how the AI agent processes a user question end-to-end.

---

## Step 1: Question Understanding
The agent receives a natural-language question such as:
"How much inventory should I reorder for next week?"

---

## Step 2: Intent Classification
The agent determines:
- Intent: inventory
- Metric: units sold
- Time window: last 30 days
- Forecast period: next 7 days

---

## Step 3: Planning
The agent decides:
- Which Shopify dataset to use (orders, inventory)
- Which metrics are required
- Whether forecasting logic is needed

---

## Step 4: ShopifyQL Generation
The agent generates a valid ShopifyQL query using structured rules.

Example:
FROM orders
SHOW sum(line_items.quantity)
WHERE created_at >= -30d

---

## Step 5: Validation
The agent validates:
- Query syntax
- Required clauses
- Time filters

Invalid queries are rejected safely.

---

## Step 6: Execution
The agent executes the query via Shopify Admin API (mocked in this project).

---

## Step 7: Post Processing
Raw data is converted into:
- Daily sales velocity
- Reorder recommendations
- Stock risk insights

---

## Step 8: Explanation
The agent converts analytics into simple business language that a store owner can
understand without technical knowledge.
