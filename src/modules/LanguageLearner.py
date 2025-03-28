import os
from dotenv import load_dotenv
from src.services.OpenAIRunner import OpenAIService
from src.models.chat import LLChatResponse
load_dotenv()




class LanguageLearnerLLM:
    def __init__(self):
        scenario_prompt_file = os.getenv('scenario_prompt_file_name')
        chat_prompt_file = os.getenv('chat_prompt_file_name')
        self.openai_service = OpenAIService()

        with open(scenario_prompt_file, 'r') as file:
            self.scenario_prompt = file.read()

        with open(chat_prompt_file, 'r') as file:
            self.chat_prompt = file.read()
    
    def format_prompt(self, vars, type):
        if type == "scenario":
            return self.scenario_prompt.format_map(vars)
        elif type == "chat":
            return self.chat_prompt.format_map(vars)
        else:
            print("incorrect chat prompt type")
    
    def generate_scenario(self, vars):
        prompt = self.format_prompt(vars=vars, type='scenario')

        try:
            op = self.openai_service.get_text_response(prompt)
            return op.replace("`", "")
        except Exception as e:
            print("Exception: ", str(e))
            return None
    def generate_chat(self, vars, chat_history) ->LLChatResponse:
        # format chat hsitory
        history = self.format_chat_history(chat_history)
        print("-----------------------------------------------------------------------------------")
        print(history)
        print("------------------------------------------------------------------------------------")
        vars['user_response'] = history
        prompt = self.format_prompt(vars=vars, type='chat')

        try:
            return self.openai_service.get_model_response(prompt, object=LLChatResponse)
        except Exception as e:
            print("Exception: ", str(e))
            return None
    def format_chat_history(self, history):
        if not history:
            return "No chat history available."
        print("--------------------------------------------------------------------------------")
        print(history)

        formatted_history = ""
        for i in history[:-1]:
            user = i[1]
            ai = i[0]
            formatted_history += f"USER: {user}\nSYSTEM: {ai}\n\n"

        last_conv = history[-1]
        formatted_history += "Current Conversation \n"

        formatted_history += f"USER: {last_conv[1]}\nSYSTEM: {last_conv[0]}"

        return formatted_history
    
