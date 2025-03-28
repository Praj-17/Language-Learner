from pydantic import BaseModel

class Scenario(BaseModel):
        scenario: str
        keywords: list[str]  # Specify the type of items in the list

