from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from models import db, Expense
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///expenses.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "fintrack-secret-key"

db.init_app(app)

with app.app_context():
    db.create_all()

def get_currency():
    return session.get("currency", "USD")

def get_symbol():
    return "₱" if get_currency() == "PHP" else "$"

@app.route("/")
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    total = sum(e.amount for e in expenses)
    return render_template("index.html", expenses=expenses, total=total,
                           currency=get_currency(), symbol=get_symbol())

@app.route("/set-currency", methods=["POST"])
def set_currency():
    session["currency"] = request.form.get("currency", "USD")
    return redirect(url_for("index"))

@app.route("/add", methods=["POST"])
def add_expense():
    expense = Expense(
        description=request.form["description"],
        amount=float(request.form["amount"]),
        category=request.form["category"],
        date=request.form["date"]
    )
    db.session.add(expense)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    expenses = Expense.query.all()
    category_totals = {}
    for e in expenses:
        category_totals[e.category] = category_totals.get(e.category, 0) + e.amount
    return render_template("dashboard.html", category_totals=category_totals,
                           currency=get_currency(), symbol=get_symbol())

@app.route("/insights")
def insights():
    expenses = Expense.query.all()
    if not expenses:
        return jsonify({"insight": "No expenses yet. Add some to get insights!"})

    symbol = get_symbol()
    summary = "\n".join(
        f"{e.date} | {e.category} | {e.description} | {symbol}{e.amount:.2f}"
        for e in expenses
    )

    api_key = os.getenv("GEMINI_API_KEY")
    models = [
        "gemini-2.0-flash-001",
        "gemini-2.0-flash",
        "gemini-2.5-flash",
        "gemini-2.0-flash-lite-001",
    ]

    prompt = (
        f"Here are my recent expenses:\n{summary}\n\n"
        "Give me 3 short, practical insights about my spending habits. "
        "Be friendly, specific, and use emojis."
    )

    for model in models:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        try:
            response = requests.post(url, json=payload, timeout=10)
            result = response.json()
            print(f"Tried {model}:", result.get("error", {}).get("message", "OK"))
            if "candidates" in result:
                insight = result["candidates"][0]["content"]["parts"][0]["text"]
                return jsonify({"insight": insight})
        except Exception as e:
            print(f"Error with {model}: {e}")
            continue

    return jsonify({"insight": "AI is currently unavailable. Please try again in a moment. ⏳"})

if __name__ == "__main__":
    app.run(debug=True)