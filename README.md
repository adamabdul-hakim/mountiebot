# 🧠 MountieBot

MountieBot is an AI-powered chatbot built with TensorFlow, NLTK, Flask, and React. It is designed to answer questions related to Berea College, offering an engaging and visually appealing chat interface.

## 🚀 Features

### Backend (Flask + TensorFlow)

- Intent classification with neural network (TensorFlow/Keras)
- Preprocessing with NLTK (tokenization, lemmatization)
- Trainable on custom intents via JSON
- API endpoint `/chat` to receive and respond to messages

### Frontend (React + Tailwind CSS)

- Fully responsive design
- Light/Dark theme toggle with persistence
- Background image with a blurred chat window
- Animated message loading
- Styled chat bubbles for user and bot

## 🛠️ Project Structure

```
mountiebot/
├── backend/               # Python backend with chatbot logic
│   ├── data/              # Pickled model and metadata
│   ├── intents/           # JSON file with chatbot intents
│   ├── mountiebot/        # Core logic
│   ├── tests/             # Unit tests
│   └── requirements.txt   # Python dependencies
│
├── frontend/              # React frontend
│   ├── public/            # Static assets (e.g. images)
│   ├── src/               # Application source code
│   ├── package.json       # Project metadata and scripts
│   └── tailwind.config.js # Tailwind CSS config
│
├── .gitignore             # unversioned files
└── README.md              # Project overview and instructions
```

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/adamabdul-hakim/mountiebot.git
```

### 2. Backend Setup (Python)

> ⚠️ Use Python 3.8–3.12. Python 3.13 is not supported due to NLTK compatibility.

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m nltk.downloader punkt wordnet
python mountiebot/main.py   # Train the model
python mountiebot/app.py    # Start API server
```

### 3. Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

## 🧪 Example Prompt

> "I'm an international student. Can I apply?"

**Response:**

> "Yes, Berea College welcomes international students and provides full tuition scholarships..."

## 📚 Learnings & Limitations

- 🧠 Great intro to ML: Built custom intent classification model using simple NLP pipeline
- ⚠️ Not very robust to paraphrased or novel input
- 📈 Could be improved with:
  - Embedding-based models (e.g., sentence-transformers)
  - Retrieval-augmented generation (RAG)
  - Larger dataset of questions and answers

## 🏫 About

This project was created for learning purposes to help students learn more about Berea College using an interactive chatbot interface.

---

Made with ❤️ by Abdul
