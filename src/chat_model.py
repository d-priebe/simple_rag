from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_core.messages import SystemMessage, HumanMessage
import torch
from transformers import pipeline


class Ai_assistant:
    def __init__(self, model_id: None):
        self.model_id = model_id

    # https://python.langchain.com/api_reference/huggingface/llms/langchain_huggingface.llms.huggingface_pipeline.HuggingFacePipeline.html
    def instantiate_model(self):
        # Instantiate tokenzier + model
        tokenizer = AutoTokenizer.from_pretrained(self.model_id)
        model = AutoModelForCausalLM.from_pretrained(self.model_id)
        pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=256)
        hf_llm = HuggingFacePipeline(pipeline=pipe)
        self.ai_assistant = ChatHuggingFace(llm= hf_llm)

        return self.ai_assistant
    
    def chat_response(self, query, graph_store):

        query = "What are the different Llama-Nemotron series of models?"
        answer = graph_store.chat_response(query)
        return(answer.content)


        



























# messages = [
#     {
#         "role": "system",
#         "content": "You are a friendly chatbot who always responds in the style of a pirate",
#     },
#     {"role": "user", "content": "How many helicopters can a human eat in one sitting?"},
# ]
# prompt = pipe.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
# outputs = pipe(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)

# print(outputs[0]["generated_text"])

