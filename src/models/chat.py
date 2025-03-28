from pydantic import BaseModel
from enum import Enum

class MistakeType(Enum):
    GRAMMATICAL = "grammatical"
    CONTEXTUAL = "contextual"
    SPELLING = "spelling"

class Mistake(BaseModel):
    corrected_version: str
    mistake_types: list[MistakeType]
    explaination: str

    def __repr__(self):
        mistake_types_str = ", ".join(mt.value for mt in self.mistake_types)
        return (
            f" correction: '{self.corrected_version}', \n "
            f"mistake_typeS: {mistake_types_str}, \n "
            f"explaination: '{self.explaination}') \n"
        )



class LLChatResponse(BaseModel):
    conversation: str
    character_name: str
    is_correct: bool
    mistake: Mistake

