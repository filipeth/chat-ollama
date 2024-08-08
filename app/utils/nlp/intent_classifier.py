from langchain_core.language_models import BaseLLM
from langchain_core.prompts import ChatPromptTemplate

INTENTS = {
    "SQL_CLIENT": "When you need to answer the question using the sql database for a specific user, here you will need to know which client id you need to search for.",
    "SQL_GENERAL": "When you need to answer general questions using the sql database for a group of users.",
    "CRM_SERVICE": "When you need to answer question related to information about the user."
}
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an intent classifier responsible for giving a class for the given user text. You only answer the class name and nothing else, no need to explain or give extra information. Otherwise you will be penalized. Best answer will get $300.\n\nCLASSES:\n{classes_description}\n\nChoose one of: [{classes}]",
        ),
        ("human", "{input}"),
    ]
)
async def classify_intent(llm: BaseLLM, text: str) -> str:
    classes_description = "\n".join([f"'{x}': {y}" for x, y in INTENTS.items()])
    response = ''
    chain = prompt | llm
    while response not in INTENTS:
        response = await chain.ainvoke({
            "classes_description": classes_description,
            "classes": INTENTS.keys(),
            "input": text
        })

    
    return response
