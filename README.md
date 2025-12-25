# AI Powered Shopify Analytics App

## Overview
This project is a mini AI-powered analytics application designed to work with a Shopify
store and answer business questions using natural language.

The system interprets user questions, converts them into ShopifyQL-style analytics logic,
fetches relevant data, and returns insights in simple, business-friendly language.

---

## Features
- Shopify OAuth-based authentication (mocked for development)
- Rails API as a secure backend gateway
- Python FastAPI-based AI analytics service
- Agentic workflow (intent → plan → query → validate → explain)
- ShopifyQL-style query generation
- Clear, non-technical explanations for store owners

---

## Tech Stack

### Backend Gateway
- Ruby on Rails (API-only)
- PostgreSQL (optional, for logs)
- Shopify Admin API (mocked)

### AI Service
- Python
- FastAPI
- Agent-based reasoning architecture
- Mocked LLM (interview-safe)

---

## Project Structure

ai-shopify-analytics/
│
├── rails-api/ # Shopify OAuth + API Gateway
├── ai-service/ # AI Agent + Analytics Logic
├── docs/ # Architecture, Agent Flow, API Flow
└── README.md

yaml
Copy code

---

## How It Works

1. Merchant connects their Shopify store via OAuth
2. User asks a business question in natural language
3. Rails API validates input and forwards the request
4. Python AI agent classifies intent and plans analytics steps
5. ShopifyQL-style query logic is generated and validated
6. Results are post-processed and explained in simple language

---

## Example Question

**Question:**  
“How much inventory should I reorder for next week?”

**Answer:**  
“Based on the last 30 days, you sell around 10 units per day. You should reorder at least
70 units to avoid stockouts next week.”

---

## Why This Design

- Clean separation of concerns (Rails vs AI service)
- Scalable and extensible AI architecture
- Agent-based reasoning instead of single-prompt AI
- Practical handling of ambiguity and incomplete data
- Designed to be interview- and production-inspired

---

## Running the Project

### Start the AI Service
```bash
cd ai-service
uvicorn app.main:app --reload
Start the Rails API
bash
Copy code
cd rails-api
rails s
Notes
Shopify API interactions are mocked for development and interview purposes

The architecture allows easy replacement with real ShopifyQL execution

Focus is on system design, agent reasoning, and clarity of insights

Author
Saloni Saini
