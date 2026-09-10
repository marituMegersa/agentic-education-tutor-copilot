from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.education_tutor_copilot.schemas import AgenticEducationTutorCopilotSessionCreate, AgenticEducationTutorCopilotSessionResponse
from app.domain.education_tutor_copilot.service import AgenticEducationTutorCopilotService

router = APIRouter(prefix="/api/v1/education_tutor_copilot", tags=["Agentic Education Tutor Copilot Domain"])

@router.post("/sessions", response_model=AgenticEducationTutorCopilotSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticEducationTutorCopilotSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Education Tutor Copilot.
    """
    return AgenticEducationTutorCopilotService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticEducationTutorCopilotSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticEducationTutorCopilotService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
