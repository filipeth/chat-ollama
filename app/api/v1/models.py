from typing import Optional
from pydantic import BaseModel

class ChatRequest(BaseModel):
    client_id: Optional[str] = None
    text: str

class CRMAddRequest(BaseModel):
    client_id: str
    documents: list[str]

class CRMSearchRequest(BaseModel):
    client_id: str
    query: str