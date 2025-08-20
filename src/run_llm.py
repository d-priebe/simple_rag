from base_model import TinyLlama

llm = TinyLlama(model_path= ".\TinyLlama.exe", model_name = "TinyLlama")

print(llm.invoke("Test this model response"))