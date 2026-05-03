# 💰 fin.track — AI-Powered Finance Tracker

A full-stack web application for tracking personal expenses with AI-generated spending insights. Built with Python, Flask, and the Gemini API.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-green)
![Gemini](https://img.shields.io/badge/Gemini-AI-orange)

## 🌐 Live Demo
[https://finance-tracker-m3kc.onrender.com]

## ✨ Features
- **Add & delete expenses** with description, amount, category, and date
- **Dashboard** with interactive doughnut and bar charts (Chart.js)
- **AI Spending Insights** powered by Google Gemini API
- **Currency toggle** between USD ($) and PHP (₱)
- **Responsive dark UI** with modern design

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | SQLite, SQLAlchemy |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| AI | Google Gemini API |
| Deployment | Render |

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- A Google Gemini API key ([get one free here](https://aistudio.google.com))

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/huweewee/finance-tracker.git
   cd finance-tracker
```

2. **Create a virtual environment**
```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Mac/Linux
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up environment variables**

   Create a `.env` file in the project root:

GEMINI_API_KEY=AIzaSyCLrgKGx7-0IAMGfwEB_RhsnDqkRtb8D-o   

5. **Run the app**
```bash
   python app.py
```

6. **Visit** `http://127.0.0.1:5000` in your browser

## 📁 Project Structure
finance-tracker/
├── app.py              # Main Flask app — routes and API logic
├── models.py           # SQLAlchemy database models
├── templates/
│   ├── index.html      # Homepage — expense form and table
│   └── dashboard.html  # Charts and spending breakdown
├── static/
│   └── style.css       # Custom dark theme styles
├── requirements.txt    # Python dependencies
└── README.md

## 📸 Screenshots
<img width="1349" height="673" alt="image" src="https://github.com/user-attachments/assets/44a5a325-6a94-4c89-bb4b-fa6ebcd3527d" />
<img width="1366" height="668" alt="image" src="https://github.com/user-attachments/assets/9351b0ba-daf7-4d66-83e0-c60b67646277" />

## 🔮 Future Improvements
- User authentication (login/register)
- Export expenses to CSV
- Monthly budget goals
- Mobile app version

## 👤 Author
**huweewee** — [GitHub](https://github.com/huweewee)
