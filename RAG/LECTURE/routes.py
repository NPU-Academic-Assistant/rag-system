from fastapi import APIRouter, Depends
from RAG.LECTURE.schemas import LectureStart
from RAG.LECTURE.schemas import LectureAction
from RAG.LECTURE.services.lecture_retriever import LectureRetriever
from RAG.LECTURE.services.lecture_session import create_session
from RAG.LECTURE.services.lecture_session import get_session
from RAG.LECTURE.services.lecture_parser import LessonParser
from RAG.LECTURE.services.answer_reviewer import AnswerReviewer
from RAG.LECTURE.services.lecture_engine import LectureEngine
from RAG.LECTURE.services.models.teaching_state import TeachingState
from SHARED.dependencies import get_collection as collection
from SHARED.dependencies import llm_client


router = APIRouter()

@router.post("/lecture")
def start(req:LectureStart,llm = Depends(llm_client), coll= Depends(collection)):
    professor = AnswerReviewer(llm.client, llm.model)
    lecture_retriever = LectureRetriever()
    parser = LessonParser()
    state = TeachingState()
    engine = LectureEngine(professor, lecture_retriever, parser, state)
    engine.start_lesson(req.course, req.lesson)
    return create_session(req.user_id, engine)

@router.post("/lecture/action")
def action(req: LectureAction):
    engine = get_session(req.user_id, req.session_id)
    return engine.handle_action(req.action)
    