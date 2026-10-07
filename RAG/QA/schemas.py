from pydantic import BaseModel

class QAStart(BaseModel):
    course: str
    lesson: str
    user_id : str

class QAAsk(BaseModel):
    user_id : str
    session_id : str
    question : str
    
