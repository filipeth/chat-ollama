from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.v1.helpers import call_agent, crm_add_documents, crm_search_documents
from app.api.v1.models import ChatRequest, CRMAddRequest, CRMSearchRequest


router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    resp = await call_agent(request)
    return resp

@router.post("/crm/add")
async def crm_add(request: CRMAddRequest):
    crm_add_documents(request)
    return JSONResponse(content="Documents added")

@router.post("/crm/search")
async def crm_search(request: CRMSearchRequest):
    documents = crm_search_documents(request)
    return JSONResponse(content=documents)