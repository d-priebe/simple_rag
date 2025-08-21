from langchain_mongodb.graphrag.graph import MongoDBGraphStore
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import TokenTextSplitter
import os


class Data_Loader:
    def __init__(self, data_path: str):
        self.data_path = data_path

    # https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.PyPDFDirectoryLoader.html
    def load_data(self):
        self.loader = PyPDFDirectoryLoader(self.data_path)
        docs = self.loader.load()
        return docs

    # https://www.mongodb.com/docs/atlas/ai-integrations/langchain/graph-rag/?tck=graphrag_blog_4_14_25&utm_campaign=Product+Marketing&utm_source=Docs&utm_medium=YouTube&utm_content=LHzOkwdRars&utm_term=dave.g
    # https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html
    def tokenize(self, docs):
        text_splitter = TokenTextSplitter(chunk_size=250, chunk_overlap=50)
        self.pdf_docs = text_splitter.split_documents(docs)
        return
    
    def build_knowledge_graph(self, model):
        graph_store = MongoDBGraphStore.from_connection_string(
        connection_string = os.getenv("ATLAS_CONNECTION_STRING"),
        database_name = os.getenv("ATLAS_DB_NAME"),
        collection_name = os.getenv("ATLAS_COLLECTION"),
        entity_extraction_model = model
        )
        graph_store.add_documents(self.pdf_docs)

        return graph_store