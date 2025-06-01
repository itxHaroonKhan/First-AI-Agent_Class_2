

# 🚀 Apna Pehla AI Agent Banayein 🤖

Ye guide aapko step-by-step batayega ke kaise aap Python aur OpenAI API ke sath apna pehla AI agent bana sakte hain. Ye guide beginners ke liye hai aur basic Python aur terminal commands ka knowledge assume karta hai.

---

## 📋 Zaroori Cheezein

- Python 3.8 ya isse zyada version installed
- Koi code editor (jaise VS Code)
- [OpenAI API key](https://platform.openai.com/signup) (agar nahi hai to sign up karein)
- (Optional) [`uv`](https://github.com/astral-sh/uv) for faster package management

---

## 🛠️ Steps to Build Your AI Agent

### 1. **Project Shuru Karein**

*(Optional)* Agar aap `uv` (ek fast Python package manager) use kar rahe hain, to project initialize karein:

```bash
uv init
```

> **Note**: `uv init` `uvicorn` ka hissa nahi hai. Ye sirf tab use karein jab `uv` installed ho.

### 2. **Project Folder Banayein**

Apne AI agent ke liye ek naya folder banayein aur usme jayein:

```bash
mkdir my_ai_agent
cd my_ai_agent
```

### 3. **Virtual Environment Banayein**

Dependencies ko alag rakhne ke liye virtual environment banayein aur activate karein:

**Windows ke liye:**

```bash
python -m venv venv
.\venv\Scripts\activate

```

**Mac/Linux ke liye:**

```bash
python3 -m venv env
source env/bin/activate
```

> **Note**: Agar aap `uv` use kar rahe hain, to virtual environment manually activate karne ki zarurat nahi. `uv` ke commands (jaise `uv run`) automatically environment handle karte hain.

### 4. **Zaroori Packages Install Karein**

AI agent ke liye required Python packages install karein:

```bash
pip install python-dotenv openai
```

Agar `uv` use kar rahe hain:

```bash
uv pip install python-dotenv openai
```

### 5. **OpenAI API Key Hasil Karein**

Apne AI agent ko OpenAI ke language models se connect karne ke liye API key chahiye:

1. [OpenAI API platform](https://platform.openai.com/signup) par sign up ya log in karein.
2. **API Keys** section mein jayein.
3. **Create new secret key** par click karein aur key copy karein.
4. Key ko safe rakhein aur publicly share na karein.

Project folder mein `.env` file banayein aur key is tarah add karein:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 6. **API Key Set Up Karein**

Confirm karein ke `.env` file mein API key sahi se add hua hai aur project mein load ho raha hai.

### 7. **AI Agent Banayein**

`openai` package ka use karke ek AI agent banayein jo user ke input ke jawab mein intelligent responses de, jaise translation, question answering, ya content generation.

### 8. **Language Model se Connect Karein**

Apne agent ko OpenAI ke language model se connect karein, jaise:

- `gpt-3.5-turbo`
- `gpt-4` (agar aapke plan mein available ho)

### 9. **Agent Chalayein**

Apne Python script ko run karke agent test karein. Do tareeke hain:

**Standard tareeka (virtual environment ke sath):**

```bash
python main.py
```

**Agar `uv` use kar rahe hain:**

```bash
uv run main.py
```

> **Note**: `uv run main.py` directly script chalata hai aur virtual environment ko automatically handle karta hai.

---

## 📝 Zaroori Baatein

- `.env` file mein `OPENAI_API_KEY` ko apni actual API key se replace karein.
- Agar `python main.py` use kar rahe hain, to pehle virtual environment activate karein. `uv run main.py` ke liye ye zaruri nahi.
- Advanced features ke liye, jaise multiple inputs ya custom prompts, OpenAI documentation dekhein.
- Koi issue aaye to API key, internet connection, ya package installations check karein.

---

## 🔧 Troubleshooting

- **API Key Error**: Ensure karein ke `.env` file project ke root mein hai aur key sahi format mein hai.
- **Module Not Found**: Check karein ke `python-dotenv` aur `openai` virtual environment mein installed hain.
- **Rate Limits**: Agar API rate limit ka issue aaye, to apna OpenAI plan check karein ya [x.ai/grok](https://x.ai/grok) ya [help.x.com](https://help.x.com/en/using-x/x-premium) par upgrade karein.

---

## 🌟 Agle Qadam

- Apne agent ko aur behtar banayein, jaise multiple languages translate karna ya complex tasks add karna.
- [OpenAI API documentation](https://platform.openai.com/docs) explore karein.
- Aur AI development ke liye [xAI API services](https://x.ai/api) check karein.

