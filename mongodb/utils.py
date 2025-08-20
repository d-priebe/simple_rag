x = "mongodb+srv://drewpriebe6:<db_password>@cluster0.kpqhp9e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


import os

os.environ["OPENAI_API_KEY"] = "<api-key>"
ATLAS_CONNECTION_STRING = "<connection-string>"
ATLAS_DB_NAME = "langchain_db"    # MongoDB database to store the knowledge graph
ATLAS_COLLECTION = "wikipedia"    # MongoDB collection to store the knowledge graph