from fastapi import APIRouter, Depends
from RAG.LECTURE.schemas import LectureStart
from RAG.LECTURE.schemas import LectureAction
from RAG.LECTURE.services.lecture_retriever import lecture_retrieve
from RAG.LECTURE.services.lecture_session import create_session
from RAG.LECTURE.services.lecture_session import get_session
from RAG.LECTURE.services.answer_reviewer import AnswerReviewer
from RAG.LECTURE.services.lecture_engine import LectureEngine
from SHARED.dependencies import get_collection as collection
from SHARED.dependencies import llm_client


router = APIRouter()

@router.post("/lecture")
def start(req:LectureStart,llm = Depends(llm_client), coll= Depends(collection)):
    professor = AnswerReviewer(llm.client, llm.model)
    engine = LectureEngine(professor, lecture_retrieve, )
    
    
    