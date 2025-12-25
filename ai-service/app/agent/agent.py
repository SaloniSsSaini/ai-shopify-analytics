from app.services.intent_classifier import classify_intent
from app.agent.planner import build_plan
from app.services.query_generator import generate_shopifyql
from app.agent.validator import validate_query
from app.shopify.query_executor import execute_query
from app.services.post_processor import process_data
from app.services.explanation_service import explain_result

class AnalyticsAgent:
    def __init__(self, store_id, token):
        self.store_id = store_id
        self.token = token

    def run(self, question: str):
        intent = classify_intent(question)
        plan = build_plan(intent)
        query = generate_shopifyql(plan)

        if not validate_query(query):
            return {
                "answer": "Sorry, I could not generate a valid query.",
                "confidence": "low"
            }

        raw_data = execute_query(
            store_id=self.store_id,
            token=self.token,
            query=query
        )

        insights = process_data(raw_data, intent)
        explanation = explain_result(insights)

        return {
            "answer": explanation,
            "confidence": "medium"
        }
