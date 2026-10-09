import RAG1.tools as t1
from .prompts import system_agent_prompt
from langchain_openai import ChatOpenAI
from .tools import collection_info
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from .objects import Answer


llm = ChatOpenAI(model = "gpt-4o", temperature = 0)

agent =  create_agent(
    model = llm,
    tools = [collection_info],
    system_prompt = system_agent_prompt,
    response_format = Answer
)


def ask(question) -> dict:
    """
    This function takes a question as input and uses the agent to generate an answer based on the information retrieved from the pdf documents in the RAG1 project.
    """
    t1.last_retrieved_context = []
    
    result = agent.invoke(
    {
        "messages": [HumanMessage(content=question)]
    }
    )
    
    structured_response = result["structured_response"]
    
    return {
        "answer": structured_response.answer,
        "context": structured_response.context,
    }
    
    
print(ask("what are these penguins?"))
