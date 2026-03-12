# 🤖 NextGen AI Course Assistant

⚡ Runs with a **free OpenRouter API key** — no paid API required for testing.

An AI-powered chatbot designed to answer student queries about coding courses in real time.  
The system uses LLM-based responses, session-based conversation memory, caching, and rate limiting to simulate a real-world AI support assistant.

This project demonstrates how modern AI chat systems are built with a clean backend architecture and a modern chat interface.


---

## ✨ Features

- 🤖 **AI-Powered Responses** – Uses LLM APIs to answer course-related queries.
- 🧠 **Session-Based Conversation Memory** – Maintains context for each user session.
- ⚡ **Response Caching** – Frequently asked questions are cached to reduce LLM calls.
- 🛡 **Rate Limiting** – Prevents spam and protects the API from abuse.
- 📊 **Analytics Dashboard** – Tracks total messages, cache hits, and LLM calls.
- 💬 **Modern Chat Interface** – Clean UI with chat bubbles, typing indicator, and smooth scrolling.
- 🎨 **Product-style Landing Page** – Includes feature highlights and a professional layout.

---

## 🏗 System Architecture
User Browser
->
Flask API (routes.py)
->
Session Manager
->
Cache Layer
->
LLM API (OpenRouter / OpenAI)


---

## 🧰 Tech Stack

### Backend
- Python
- Flask
- Flask-Limiter (rate limiting)

### AI
- OpenRouter / OpenAI API
- Prompt Engineering

### Frontend
- HTML
- CSS
- JavaScript

### System Design
- Response caching
- Session management
- API rate limiting
- Analytics tracking

---

## 📊 Analytics Dashboard

The chatbot includes a lightweight analytics system that tracks:

- Total messages
- Cache hits
- LLM API calls

This helps simulate monitoring systems used in real production AI services.

---

## 📁 Project Structure
ai-course-chatbot/
│
├── app/
│ ├── routes.py
│ ├── chatbot.py
│ ├── cache.py
│ └── analytics.py
│
├── static/
│ ├── style.css
│ └── chat.js
│
├── templates/
│ └── index.html
│
├── config.py
├── run.py
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### Clone the repository
git clone https://github.com/yourusername/ai-course-chatbot.git

### Navigate into the project
cd ai-course-chatbot

### Install dependencies
pip install -r requirements.txt

### Create `.env` file
API_KEY=your_api_key

### Run the server
python run.py

### Open in browser
http://127.0.0.1:5000

---

## 🧠 Key Engineering Concepts Demonstrated

- AI API integration
- Backend API design with Flask
- Prompt engineering
- Caching strategies for LLM applications
- Rate limiting for production APIs
- Session-based user interaction
- Frontend + backend integration

---

## 🚀 Future Improvements

- Document-based chatbot using **RAG (Retrieval Augmented Generation)**
- Redis caching for scalability
- Authentication system
- Deployment with Docker
- Cloud deployment (Render / AWS / Railway)

---

## 👩‍💻 Author

**Parul Singh**  
B.Tech Computer Science & Engineering  

Interested in **AI, Backend Development, and Intelligent Systems.**
