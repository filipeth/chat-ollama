from langchain_ollama.llms import OllamaLLM
import os


def load_llm(model=os.getenv('LLM_MODEL', 'llama3.1')):
    return OllamaLLM(model=model, keep_alive=-1, base_url=os.getenv('LLM_API_URL'))