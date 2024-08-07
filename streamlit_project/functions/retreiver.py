from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader

from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter

def retreiver(url):
    loader = WebBaseLoader(url)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

# create the open-source embedding function
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# load it into Chroma
    db = Chroma.from_documents(docs, embedding_function)

# query it
    query = "What did the president say about Ketanji Brown Jackson"
    docs = db.similarity_search(query)