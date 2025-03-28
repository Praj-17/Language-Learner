import streamlit as st
from src.modules.LanguageLearner import LanguageLearnerLLM
from database import save_conversation, init_db

# Initialize components
llm = LanguageLearnerLLM()
init_db()

# Language greetings mapping
GREETINGS = {
    "Spanish": "¡Hola!",
    "French": "Bonjour !",
    "German": "Hallo!",
    "Italian": "Ciao!"
}

# =============== Sidebar Configuration ===============
st.sidebar.title("Settings & Scenario")

# Language Selection
language_to_learn = st.sidebar.selectbox("Select Language to Learn", ["Spanish", "French", "German", "Italian"])
native_language = st.sidebar.selectbox("Select Your Native Language", ["English", "Spanish", "French", "German"])
current_proficiency = st.sidebar.selectbox("Select Your Proficiency Level", ["Beginner", "Intermediate", "Advanced"])

# Scenario Generation Section
st.sidebar.markdown("---")
st.sidebar.subheader("Scenario Controls")

# Initialize session state
if 'conversation_data' not in st.session_state:
    st.session_state.update({
        'conversation_data': {},
        'chat_history': [["Hola"]],
        'chat_active': True,
        'mistakes': [],
        'conversation_objects': []
    })

# Generate scenario button
if st.sidebar.button("Generate New Scenario"):
    user_vars = {
        "language_to_learn": language_to_learn,
        "native_language": native_language,
        "current_proficiency": current_proficiency
    }
    scenario = llm.generate_scenario(user_vars)
    st.session_state.conversation_data = {
        "scenario": scenario,
        "native_language": native_language,
        "language_to_learn": language_to_learn,
        "current_proficiency": current_proficiency
    }
    st.session_state.chat_history = [[GREETINGS[language_to_learn]]]
    st.session_state.chat_active = True
    st.session_state.mistakes = []
    st.session_state.conversation_objects = []

# Display current scenario
if st.session_state.conversation_data.get('scenario'):
    st.sidebar.markdown("---")
    st.sidebar.subheader("Current Scenario")
    st.sidebar.markdown(f"`{st.session_state.conversation_data['scenario']}`")

# =============== Main Chat Interface ===============
tab_chat, tab_contact = st.tabs(["Chat", "📞 Contact Me"])

with tab_chat:
    st.title(f"Interactive Language Chat - {language_to_learn}")

    # Chat controls header
    with st.container():
        cols = st.columns([3, 1])
        with cols[1]:
            if st.session_state.chat_active and st.button("End Chat ▶️"):
                if st.session_state.conversation_data:
                    save_conversation(st.session_state.conversation_data, st.session_state.chat_history)
                st.session_state.chat_active = False
                st.rerun()

    # Conversation display
    chat_container = st.container()
    with chat_container:
        if st.session_state.chat_history:
            conv_obj_index = 0  # Track conversation objects
            for pair in st.session_state.chat_history:
                if isinstance(pair, list):  # Initial greeting
                    st.chat_message("assistant").markdown(pair[0])
                else:
                    if pair[1]:  # User message
                        st.chat_message("user").markdown(pair[1])
                    if pair[0]:  # Assistant message
                        st.chat_message("assistant").markdown(pair[0])
                        # Show inline warning if mistake exists
                        if conv_obj_index < len(st.session_state.conversation_objects):
                            conv_obj = st.session_state.conversation_objects[conv_obj_index]
                            if not conv_obj.is_correct:
                                st.warning(f"Did you mean: **{conv_obj.mistake.corrected_version}**")
                            conv_obj_index += 1

    # Chat statistics
    if not st.session_state.chat_active:
        st.subheader("📊 Conversation Summary")
        
        if st.session_state.mistakes:
            st.metric("Total Mistakes", len(st.session_state.mistakes))
            st.subheader("🧐 Mistake Analysis")
            
            for i, mistake in enumerate(st.session_state.mistakes, 1):
                with st.expander(f"Mistake #{i}", expanded=True):
                    st.markdown(f"""
                    **Correct Version**:  
                    `{mistake.corrected_version}`  
                    
                    **Error Types**:  
                    {', '.join(mt.value for mt in mistake.mistake_types)}  
                    
                    **Explanation**:  
                    {mistake.explaination}
                    """)
        else:
            st.success("🌟 Perfect conversation! No mistakes found!")

        if st.button("Start New Conversation"):
            st.session_state.chat_active = True
            st.rerun()

    # Active chat input
    if st.session_state.chat_active:
        user_input = st.chat_input("Type your response here...")
        if user_input:
            # Update chat history
            if len(st.session_state.chat_history) == 1 and isinstance(st.session_state.chat_history[0], list):
                st.session_state.chat_history[0] = (st.session_state.chat_history[0][0], user_input)
            else:
                st.session_state.chat_history.append((st.session_state.chat_history[-1][1], user_input))

            # Generate response
            with st.spinner("Analyzing response..."):
                if st.session_state.conversation_data:
                    conversation = llm.generate_chat(
                        st.session_state.conversation_data,
                        st.session_state.chat_history
                    )
                    st.session_state.conversation_objects.append(conversation)
                    
                    if not conversation.is_correct:
                        st.session_state.mistakes.append(conversation.mistake)
                    
                    st.session_state.chat_history.append((conversation.conversation, ""))
                    st.rerun()

# Contact Tab
with tab_contact:
    st.header("📞 Contact Information")
    st.write("Feel free to reach out through any of the following platforms 😊:")

    # Email
    st.markdown("### Email")
    st.markdown("[pwaykos1@gmail.com](mailto:pwaykos1@gmail.com)")

    # Phone
    st.markdown("### Phone")
    st.markdown("[7249542810](tel:+17249542810)")

    # LinkedIn / Resume
    st.markdown("### LinkedIn / Resume")
    st.markdown("[![Resume](https://img.icons8.com/doodle/48/000000/resume.png)](https://drive.google.com/file/d/1OiSCu4e_1R7cawKSU80cr63Cd2-4OVq7/view?usp=drivesdk)")

    # GitHub
    st.markdown("### GitHub")
    st.markdown("[![GitHub](https://img.icons8.com/nolan/64/github.png)](https://github.com/praj-17)")