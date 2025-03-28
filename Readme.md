

# 🌍 Language Learner - Interactive Language Chat App

Welcome to **Language Learner** — an AI-powered, interactive chat platform designed to help you **practice real-life conversations** in multiple languages with real-time feedback on grammar, vocabulary, and sentence structure.

---

## 🚀 Live Demo

Try out the app right now:  
**👉 [LIVE APP](https://language-learner-kkf7.onrender.com/)**  

Explore the source code:  
**🔗 [GitHub Repository](https://github.com/Praj-17/Language-Learner)**  

Pull the Docker image:  
**🐳 [Docker Hub](https://hub.docker.com/repository/docker/prajwal1717/language-learner/general)**  

---


## 📌 Features

- 🗣️ **Conversational Practice** in Spanish, French, German, or Italian or any other
- 🌐 **Native Language Support** for English, Spanish, French, and German or any other
- 📊 **Proficiency-Based Scenarios**: Beginner, Intermediate, or Advanced
- ✨ **Scenario Generation** for realistic dialogue situations
- 📚 **Real-Time Mistake Detection & Feedback** with correction suggestions
- 🧠 **Conversation Summary & Mistake Analysis**
- 🗂️ **Chat History Saving** to track progress
- 💬 **Beautiful Streamlit UI** with multi-tab experience

---

## 🧪 Tech Stack

- **Frontend & App UI**: [Streamlit](https://streamlit.io)
- **LLM Engine**: Custom LLM wrapper via `LanguageLearnerLLM` module
- **Data Persistence**: SQLite (via `database.py`)
- **Containerization**: Docker
- **Deployment**: Render

---

## 🐳 Docker Support

The app is fully Dockerized and easy to run in any environment.

### 📦 Docker Image

Available on Docker Hub:  
**🔗 [language-learner Docker Hub](https://hub.docker.com/repository/docker/prajwal1717/language-learner/general)**

### 🔧 Docker Run Instructions

```bash
# Build the image
docker build -t language-learner .

# Run the container
docker run -p 8501:8501 language-learner
```

---

## 📂 Project Structure

```
.
├── src/
│   └── modules/
│       └── LanguageLearner.py  # Core logic for chat generation and analysis
├── database.py                 # DB initialization & conversation saving
├── main.py                     # Streamlit app file (provided above)
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 📥 Installation (Without Docker)

```bash
# Clone the repository
git clone https://github.com/Praj-17/Language-Learner.git
cd Language-Learner

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run main.py
```

---

## 📇 Contact

Feel free to reach out with questions or contributions:

- 📧 **Email**: [pwaykos1@gmail.com](mailto:pwaykos1@gmail.com)  
- 🔗 **GitHub**: [Praj-17/Language-Learner](https://github.com/Praj-17/Language-Learner)  
- 📄 **Resume**: [Google Drive Resume](https://drive.google.com/file/d/1_V82Ub4f0OV1WPnw2EMR0SbD1tRCWQX9/view?usp=drive_link)

---

## 🙌 Contributing

Contributions are welcome!  
If you'd like to add features or fix bugs, please fork the repository and open a pull request.

---

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for more info.

---
