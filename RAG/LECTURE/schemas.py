from pydantic import BaseModel
from RAG.LECTURE.services.models.student_action import StudentAction

class LectureStart(BaseModel):
    course: str
    lesson: str
    concept: str
    user_id: str

class LectureAction(BaseModel):
    user_id: str
    session_id: str
    action: StudentAction
