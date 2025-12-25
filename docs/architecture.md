# System Architecture – AI Powered Shopify Analytics App

This system is designed using a clean microservice-style architecture with a clear
separation of concerns between business logic, AI reasoning, and third-party integrations.

---

## High-Level Components

1. Rails API (Gateway Layer)
2. Python AI Service (Agentic Intelligence Layer)
3. Shopify Store (Data Source)

---

## Architecture Overview

User → Rails API → Python AI Agent → Shopify API → Python AI Agent → Rails API → User

---

## Component Responsibilities

### 1. Rails API (Gateway)
- Handles Shopify OAuth authentication
- Stores Shopify access tokens securely
- Validates incoming requests
- Acts as a secure gateway between frontend and AI service
- Logs questions and responses (optional)

### 2. Python AI Service
- Interprets natural language questions
- Classifies user intent (sales, inventory, customers)
- Plans required analytics steps
- Generates ShopifyQL queries
- Executes queries via Shopify Admin API
- Converts raw data into business-friendly explanations

### 3. Shopify Store
- Provides Orders, Products, Inventory, and Customer data
- Supports ShopifyQL for analytics queries

---

## Key Design Principles

- Separation of concerns
- Agent-based reasoning instead of single-prompt AI
- Secure token handling
- Scalable and extensible architecture
- Interview-ready and production-inspired design
