from typing import Dict
from RAG.LECTURE.services.lecture_engine import LectureEngine

sessions: Dict[str, dict] = {}

import uuid

def create_session(user_id: int, engine: LectureEngine) -> str:
    session_id = str(uuid.uuid4()) 

    sessions[session_id] = {
        "user_id": user_id,
        "engine": engine,
    }

    return session_id


def get_session(session_id: str, user_id: int) -> LectureEngine:
    session = sessions.get(session_id)

    if session is None:
        raise ValueError("Invalid or expired session")

    if session["user_id"] != user_id:
        raise PermissionError("Session does not belong to this user")

    return session["engine"]