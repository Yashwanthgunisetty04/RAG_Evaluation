from pydantic import BaseModel, Field

class Answer(BaseModel):
    answer: str = Field(description="The answer to the question based on the retrieved information from the pdf documents.")
    context: str = Field(description="This is the context that the agent used to reply to the user's question")

