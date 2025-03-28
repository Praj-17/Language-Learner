# database.py
import sqlite3
import json
from datetime import datetime


def init_db():
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  scenario TEXT,
                  chat_history TEXT,
                  timestamp DATETIME,
                  language_to_learn TEXT,
                  native_language TEXT,
                  proficiency_level TEXT)''')
    conn.commit()
    conn.close()

def save_conversation(conversation_data, chat_history):
    # Initialize database first
    init_db()
    
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    
    try:
        c.execute('''INSERT INTO conversations 
                     (scenario, chat_history, timestamp, language_to_learn, native_language, proficiency_level)
                     VALUES (?, ?, ?, ?, ?, ?)''',
                  (conversation_data.get('scenario', ''),
                   json.dumps(chat_history),
                   datetime.now().isoformat(),
                   conversation_data.get('language_to_learn', ''),
                   conversation_data.get('native_language', ''),
                   conversation_data.get('current_proficiency', '')))
        conn.commit()
    finally:
        conn.close()

# Initialize database when this module is imported
init_db()