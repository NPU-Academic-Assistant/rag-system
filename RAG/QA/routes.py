from fastapi import APIRouter, Depends
from RAG.QA.schemas import QAStart
from RAG.QA.schemas import QAAsk
from RAG.QA.services.qa_retriever import qa_retrieve
from RAG.QA.services.qa_answerer import QAAnswerer
from RAG.QA.services.qa_engine import QAEngine 
from RAG.QA.services.qa_sessions import create_session
from RAG.QA.services.qa_sessions import get_session
from SHARED.dependencies import get_collection as collection
from SHARED.dependencies import llm_client 
from SHARED.embeddings import generate_embedding


router = APIRouter()

@router.post("/qa/start")
def start(req: QAStart,llm =Depends(llm_client) , collec = Depends(collection)):
    answerer = QAAnswerer(llm.client, llm.model)
    engine = QAEngine(qa_retrieve,answerer,generate_embedding, collec)
    engine.start_session(req.course, req.lesson)
    return create_session(req.user_id ,engine)
    


@router.post("/qa/ask")
def ask(req:QAAsk):
    engine = get_session(req.Session_id, req.user_id)
    return engine.ask(req.Question)
    