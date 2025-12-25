# AI Powered Shopify Analytics App

## Overview
This project is a mini AI-powered analytics system that connects to a Shopify store
and allows users to ask business questions in natural language.

The system translates questions into ShopifyQL, fetches analytics data, and returns
clear, business-friendly insights.

---

## Features
- Shopify OAuth authentication
- Rails API as secure backend gateway
- Python FastAPI-based AI service
- Agentic workflow for analytics reasoning
- ShopifyQL query generation
- Business-friendly explanations

---

## Tech Stack

### Backend Gateway
- Ruby on Rails (API-only)
- PostgreSQL (optional)
- Shopify Admin API

### AI Service
- Python
- FastAPI
- Agent-based reasoning
- Mocked LLM (interview-safe)

---

## Project Structure

ai-shopify-analytics/
│
├── rails-api/        # Shopify OAuth + API Gateway
├── ai-service/       # AI Agent + Analytics
├── docs/             # Architecture & Design Docs
└── README.md

---

## How It Works

1. Merchant connects their Shopify store via OAuth
2. User asks a business question
3. Rails API validates and forwards the request
4. Python AI agent interprets the question
5. ShopifyQL is generated and executed
6. Results are converted into simple insights

---

## Example Question

"How much inventory should I reorder for next week?"

### Example Answer

"Based on the last 30 days, you sell around 10 units per day. You should reorder at least
70 units to avoid stockouts next week."

---

## Why This Design

- Clear separation of concerns
- Scalable AI architecture
- Practical handling of real-world ambiguity
- Interview-ready system design
- Focus on reasoning over raw AI output

---

## Running the Project

### Start Rails API
cd rails-api
rails s

### Start AI Service
cd ai-service
uvicorn app.main:app --reload

---

## Notes
- Shopify API calls are mocked for interview safety
- Architecture mirrors production-ready systems
- Focus is on clarity, reasoning, and design

---

## Author
Saloni Saini
