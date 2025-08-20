from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.outputs import ChatGeneration
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatResult
from typing import Any, Dict, List, Optional
from pathlib import Path

class TinyLlama(BaseChatModel):

    model_name: str = "TinyLlama"
    model_path: Path

    def __init__(self, model_path: str, model_name: str):
        super().__init__(model_path = Path(model_path), model_name = model_name)

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:


        tokens = messages[-1].content
        ct_input_tokens = sum(len(message.content) for message in messages)
        ct_output_tokens = len(tokens)

        message = AIMessage(
            content=tokens,
            response_metadata={ 
                "time_in_seconds": 3,
                "model_name": self.model_name,
            },
            usage_metadata={
                "input_tokens": ct_input_tokens,
                "output_tokens": ct_output_tokens,
                "total_tokens": ct_input_tokens + ct_output_tokens,
            },
        )
        

        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])
    
    @property
    def _llm_type(self) -> str:
        return "custom-TinyLlama-chat"

    




