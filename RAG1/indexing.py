from dotenv import load_dotenv
from .file_reader import extract_paragraphs
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai.embeddings import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(model = "text-embedding-3-large")
vectorstore = InMemoryVectorStore(embeddings)


chunks = extract_paragraphs(r"D:\Projects\RAG_Evaluation\pdfs\Penguins.pdf")
vectorstore.add_texts(chunks)
print(f"Number of chunks added to the vectorstore: {len(chunks)}")