from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.chat_model = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0.7,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_text_response(self, user_prompt: str):
        # LangChain ChatOpenAI works best with string messages (not rich content)
        messages = [HumanMessage(content=user_prompt)]
        llm_response = self.chat_model.invoke(messages)
        
        # Wrap in BasicPersonaResponse or your custom schema
        return llm_response.content

    def get_model_response(self, user_prompt: str, object):
        response = self.client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_prompt},
                ],
            }
        ],
        response_format=object
        )
        return response.choices[0].message.parsed


if __name__ == "__main__":
    openai = OpenAIService()

    vars = {
        "language_to_learn": "Spanish",
        "native_language": "English", 
        "current_proficiency": "Beginner"
    }
    text = """Create an engaging scene for a language learning chatbot that adapts based on the following user inputs: 

1.Desired language to learn  - {language_to_learn}.
2.User's native language  - {native_language}.
3.User's current proficiency level in the desired language {current_proficiency}.

The scene should include: - 
1. A brief introduction that establishes the context of the conversation (e.g., a café setting, a market, a travel scenario).
2. Specific vocabulary and phrases relevant to the chosen scene and language level.
3. There should be only 2 characters
    - User
    - Another person with whom the user is talking with. 

You only generate a scenario and do not have any conversation. 
Or provide any other text apart from the scenario.
"""
    ans = openai.get_text_response(user_prompt= text.format_map(vars))
    print(type(ans))