<<<<<<< HEAD

# 🧠 Mental Health Chatbot – FastAPI Backend

This FastAPI service exposes a single `/chat` endpoint that proxies user
messages to the OpenAI Chat Completion API, using a system prompt tuned
for compassionate mental‑health support.

## Running Locally

```bash
# 1. Create virtual env (optional)
python -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your OpenAI key
export OPENAI_API_KEY=sk-...

# 4. Start the dev server
uvicorn app:app --reload
```

The interactive docs are then available at http://localhost:8000/docs
=======
# mental-health-chatbot-main
>>>>>>> 22c48a0b1870814e05adfde7fa5e65bb52c3eadb
