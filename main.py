from src.modules.LanguageLearner import LanguageLearnerLLM


llm = LanguageLearnerLLM()



user_vars = {
        "language_to_learn": "Spanish",
        "native_language": "English", 
        "current_proficiency": "Beginner"
    }

scenarion = llm.generate_scenario(user_vars)
conversation_data = {
    "scenario": scenarion,
    "native_language": "English",
    "language_to_learn": "Spanish",
    "current_proficiency": "Intermediate"
}

chat_history = [["Hola"]]


print(scenarion)

while True:
    user_input = input("Your response: ")
    if user_input.lower() == "stop":
        break
    if len(chat_history) == 1 and isinstance(chat_history[0], list):
        chat_history[0] = (chat_history[0][0], user_input)
    else:
        chat_history.append((chat_history[-1][1], user_input))
    conversation = llm.generate_chat(conversation_data, chat_history)
    print(conversation.character_name, ":", conversation.conversation)
    if not conversation.is_correct:
        print(conversation.mistake)
    chat_history.append((conversation.conversation, ""))
