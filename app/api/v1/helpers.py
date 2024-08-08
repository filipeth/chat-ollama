from fastapi import HTTPException

from app.api.v1.models import ChatRequest, CRMAddRequest, CRMSearchRequest
from app.services.llms import load_llm
from app.utils.nlp.intent_classifier import classify_intent
from app.services.sql_agent.sql_agent import get_sql_agent
from app.services.retriever import retriever
from langchain_core.prompts import ChatPromptTemplate

llm = load_llm()
sql_agent = get_sql_agent(llm)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that will use the DOCUMENTS provided to answer the user QUESTION",
        ),
        ("human", "# QUESTION: {input}\n\n# DOCUMENTS\n{documents}"),
    ]
)
chain = prompt | llm


async def call_agent(request: ChatRequest):
    intent = await classify_intent(llm, request.text)

    documents = None
    if intent == 'CRM_SERVICE':
        documents = retriever.search(
            collection_name=request.client_id, 
            text=request.text
        )
    elif intent == 'SQL_CLIENT':
        documents = await sql_agent.arun(request.text + f"\nClient id: {request.client_id}")
    else:
        documents = await sql_agent.arun(request.text)

    if not documents:
        raise HTTPException(status_code=500, detail="Error searching documents")
    response = await chain.ainvoke({
        "input": request.text,
        "documents": documents
    })
    return response

def crm_add_documents(request: CRMAddRequest):
    try:
        retriever.add_documents(request.client_id, request.documents)
    except Exception:
        raise HTTPException(status_code=500, detail="Error adding documents")
    
def crm_search_documents(request: CRMSearchRequest):
    try:
        response = retriever.search(
            collection_name=request.client_id, 
            text=request.query
        )
        return [r.document for r in response]
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Error searching documents")