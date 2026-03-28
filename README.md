# 🚀 Finlactics AI (Phidata + Groq)

An AI-powered multi-agent financial assistant built using **Phidata**, **Groq LLMs**, and **FastAPI Playground**.

This project combines:

* 📈 Financial data analysis (stocks, recommendations, fundamentals)
* 🌐 Real-time web search
* 🤖 Multi-agent orchestration

---

## 🧠 Features

* 🔍 **Web Search Agent** – Fetches latest information from the web
* 💰 **Finance Agent** – Retrieves:

  * Stock prices
  * Analyst recommendations
  * Company news
  * Fundamentals
* 🧩 **Multi-Agent System** – Combines both agents intelligently
* 🎮 **Phidata Playground UI** – Interactive interface to test agents

---

## 📂 Project Structure

```
finlactics_phidata/
│
├── src/
│   ├── Agents/
│   │   ├── __init__.py
│   │   ├── web_agent.py
│   │   ├── finance_agent.py
│   │   └── multi_agent.py
│   │
│   ├── main.py
│   ├── play_ground.py
│   └── test.py
│
├── .env
├── .env.example
├── requirements.txt
├── pyproject.toml
└── README.md
```

---

## ⚙️ Prerequisites

Make sure you have:

* Python **3.10+**
* Git installed
* Internet connection (for APIs)

---

## 🔑 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd finlactics_phidata
```

---

### 2️⃣ Create virtual environment (UV recommended)

```bash
uv venv
```

Activate it:

**Windows:**

```bash
.venv\Scripts\activate
```

**Mac/Linux:**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

Using UV:

```bash
uv add -r requirements.txt
```

Or using pip:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Install required FastAPI extras

```bash
pip install python-multipart
```

---

### 5️⃣ Setup environment variables

Create a `.env` file in root:

```
GROQ_API_KEY=your_groq_api_key_here
MODEL_ID=llama-3.3-70b-versatile
```

You can copy from:

```
.env.example
```

---

## ▶️ Running the Project

Start the Playground server:

```bash
python src/main.py
```

---

## 🌐 Access the App

Once running, open:

```
http://localhost:7777
```

OR use the Phidata Playground link shown in terminal.

---

## 🧪 Example Query

Try asking:

```
Summarize analyst recommendation and latest news for NVIDIA
```

---

## ⚠️ Important Notes

* Avoid using weak models like:

  ```
  llama-3.1-8b-instant
  ```

  for multi-agent workflows

* Recommended model:

  ```
  llama-3.3-70b-versatile
  ```

* Streaming (`stream=True`) may break tool calls — keep it OFF

---

## 🐞 Troubleshooting

### ❌ API Key Error

```
GroqError: api_key must be set
```

✔ Ensure `.env` is loaded and correct

---

### ❌ Missing dependency

```
python-multipart not installed
```

✔ Run:

```bash
pip install python-multipart
```

---

### ❌ Import errors

✔ Ensure consistent function names across modules

---

### ❌ Token limit errors

✔ Reduce:

* number of agents
* tool outputs
* prompt size

---

## 🛠 Tech Stack

* **Phidata** – Agent framework
* **Groq** – LLM inference
* **FastAPI** – Backend
* **DuckDuckGo** – Web search
* **YFinance** – Financial data

---

## 🚀 Future Improvements

* Add caching for API responses
* Deploy using FastAPI (Railway/AWS)
* Add authentication
* Improve agent reasoning pipeline

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first.

---

## 📜 License

MIT License

---

## 👨‍💻 Author

Samarth Adsare
