from .indexing import vectorstore
from langchain.tools import tool

last_retrieved_context = []

@tool
def collection_info(query: str) -> str:
    
    """ 
    search the pdf knowledge base for relevant information based on the query and return the most relevant information.
    For the user's question.
    """
    
    global last_retrieved_context
    
    docs = vectorstore.similarity_search(query, k=3)
    
    last_retrieved_context = [doc.page_content for doc in docs]
    
    return "\n\n".join(last_retrieved_context)