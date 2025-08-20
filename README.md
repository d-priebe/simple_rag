# simple_rag
Repository demonstrates a RAG system capable of processing technical documents, extracting key information and answering complex reasoning based questions 


---------------------------------------------------------------------------------------------------------------------------------------------------------------

This repo is a modification of a graphRAG tutorial utilizing Langchains MongoDbGraphStore to develop a knowledge graph for a GraphRAG.
Traditional RAG approachs have been shown to have porr perforamnce across multi-hop reasoning problems - Thus the apporach is to align the assignment
of entity extraction with a system/modeling approach inductively aligned with the problem at hand.


Below you will find the sources to the tutorial as well as a breakdown of any modifications/deviations from the traditional apporach.


Tutorial approach: https://www.mongodb.com/docs/atlas/ai-integrations/langchain/graph-rag/?tck=graphrag_blog_4_14_25&utm_campaign=Product+Marketing&utm_source=Docs&utm_medium=YouTube&utm_content=LHzOkwdRars&utm_term=dave.g


Multi-hop reasoning & GraphRAG apporachs: https://neo4j.com/blog/genai/knowledge-graph-llm-multi-hop-reasoning/#:~:text=Most%20RAG%20systems%20today%20use,and%20the%20connections%20between%20them.


---------------------------------------------------------------------------------------------------------------------------------------------------------------

The modifications and approach for this project is discussed below:

1. A deviation away from utilizing openai model and prompting the model though an API and instead moved towards a lightweight opensource llm model. While this approach has a downside of a poorer performance than a better LLM - utilizing opensource handles data restrctions often found with sensitive data. The selection of a model was done by going through the following: https://python.langchain.com/docs/how_to/local_llms/

While utilizing ollama was an approach considered as its ease of setup is quite simple - The apporach opted for utilizing hugging face llamafile setup.

Here we simply followed the below approach for implementation:

# Download a llamafile from HuggingFace
Invoke-WebRequest -Uri " https://huggingface.co/jartine/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile" -OutFile "TinyLlama.exe" 

# Start the model server. Listens at http://localhost:8080 by default.
.\TinyLlama.exe --server --nobrowser