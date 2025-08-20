from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.messages import BaseMessage, AIMessage
from langchain_core.outputs import ChatResult
from typing import Any, Dict, List, Optional

class TinyLlama(BaseChatModel):

    model_name: str = "TinyLlama"

    def __init__(self, model_path, model_name):
        self.model_path = model_path
        self.model_name = model_name

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> ChatResult:


        tokens = last_message.content[: self.parrot_buffer_length]
        
        message = AIMessage(
            content=tokens,
            additional_kwargs={},  # Used to add additional payload to the message
            response_metadata={  # Use for response metadata
                "time_in_seconds": 3,
                "model_name": self.model_name,
            },
            usage_metadata={
                "input_tokens": ct_input_tokens,
                "output_tokens": ct_output_tokens,
                "total_tokens": ct_input_tokens + ct_output_tokens,
            },
        )
        ##

        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])


        return super()._generate(messages, stop, run_manager, **kwargs)

    




