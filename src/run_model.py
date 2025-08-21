from data_loading import Data_Loader
from chat_model import Ai_assistant




def main():

    # Load in data
    pdf_loader = Data_Loader("src/data/")
    Documents = pdf_loader.load_data()
    # Tokenize data
    pdf_loader.tokenize(Documents)


    # https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    
    # Instantiate llm
    llm = Ai_assistant(model_id)
    model = llm.instantiate_model()

    # Build Knowledge Graph

    pdf_loader.build_knowledge_graph(model)







if __name__ == "__main__":
    main()
