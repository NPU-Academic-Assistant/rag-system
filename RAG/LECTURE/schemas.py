from pydantic import BaseModel

class LectureStart(BaseModel):
    course: str
    lesson: str
    concept: str
    user_id: str

class LectureAction(BaseModel):
    user_id: str
    session_id: str
