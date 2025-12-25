from fastapi import APIRouter
from app.schemas.request import QuestionRequest
from app.schemas.response import AnswerResponse
from app.agent.agent import AnalyticsAgent

router = APIRouter()

@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    agent = AnalyticsAgent(
        store_id=request.store_id,
        token=request.token
    )
    return agent.run(request.question)
