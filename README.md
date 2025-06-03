
---

## 🌐 Urdu-to-English Translator Agent – Powered by Gemini Flash API

A respectful, minimal AI agent that **only translates Urdu to English** — no explanation, no extra content.

Built with:

* ⚙️ Python
* 🤖 Gemini 2.0 Flash API (OpenAI-compatible interface)
* 🧠 `agents` library (`Agent`, `Runner`, etc.)
* 🔐 `.env` config for API key

---

### 💡 Features

* Translates **only** Urdu to English
* Uses **Gemini 2.0 Flash** with OpenAI-compatible endpoint
* Ignores unrelated or non-Urdu prompts
* Fast and accurate translations
* Structured, beginner-friendly code

---

## ⚙️ Setup Instructions

> 💡 Make sure Python **3.8+** is installed.

---

### 🛠 Step-by-step Commands

#### 1. (Optional) Use `uv` to manage the environment

```bash
pip install uv
uv venv
```

#### 2. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

#### 3. Install required dependencies

```bash
uv pip install python-dotenv openai-agents
```

> Or if you're not using `uv`:

```bash
pip install python-dotenv openai-agents
```

#### 4. Create a `.env` file

```
GEMINI_API_KEY=your_gemini_api_key_here
```

#### 5. Run the script

```bash
python main.py
```

---

## 📦 Code Imports & Structure

Here's a detailed explanation of the core logic used in `main.py`:

```python
import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, RunConfig, Runner, OpenAIChatCompletionsModel
```

* `os` → Used to load environment variables.
* `load_dotenv()` → Loads `.env` file securely into the environment.
* `Agent` → Defines the behavior of the AI (translate only).
* `AsyncOpenAI` → Async client compatible with Gemini API.
* `OpenAIChatCompletionsModel` → Uses Gemini Flash with OpenAI-style interface.
* `Runner.run()` → Executes the AI with input/output management.

---

### 🧠 Code Sample

```python
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)

agent = Agent(
    name="UrduToEnglishTranslator",
    instructions="""
    Translate the given Urdu text into English. Do not explain, just provide the translation.
    Do not answer anything unrelated to Urdu-English translation.
    """
)

output = Runner.run_sync(agent, "میں Python programming سیکھ رہا ہوں تاکہ Full Stack Developer بن سکوں۔", config)

print("🔤 Translation:", output.final_output)
```

---

## 🧪 Example `.env` File

```
GEMINI_API_KEY=AIzaSyXXXXXX-Your-Gemini-API-Key
```

---

## 📋 requirements.txt (optional)

```txt
python-dotenv
openai-agents
```

Generate it with:

```bash
pip freeze > requirements.txt
```

---

## 🤖 Agent Behavior

* Name: `UrduToEnglishTranslator`
* Only does: Urdu → English translation
* Will **not** respond to:

  * English-only inputs
  * Other languages
  * Unrelated questions
* Behavior: Clear, Direct, No Explanations

---

## 👨‍💻 Created By

**Haroon Rasheed** – A focused developer building useful AI tools with modern APIs and Python.

---


