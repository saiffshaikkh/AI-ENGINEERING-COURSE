# Week 1 - Day 1: Hello LLM

A simple starter project demonstrating how to interact with Large Language Models (LLMs) using the Groq SDK and Python.

## 🛠️ Tech Stack & Dependencies

- **Runtime**: Python `>=3.14`
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **SDK**: `groq` (Llama-3.3-70b-versatile)
- **Configuration**: `python-dotenv`

## 📂 Project Structure

- **[hello_llm.py](./hello_llm.py)**: Demonstrates connection to Groq API, message payload preparation, and synchronous completion query.
- **[main.py](./main.py)**: Entrypoint starter script.
- **[.gitignore](./.gitignore)**: Prevents staging credential files (`.env`) and local environments (`.venv`).

## 🚀 Getting Started

### 1. Navigate to Project Directory
```powershell
cd "c:\Users\callm\Desktop\AI ENGINNERING\week1\day1"
```

### 2. Install Dependencies
This project uses `uv` for lightning-fast dependency resolution.
```powershell
# Create a virtual environment and install dependencies
uv sync
```

### 3. Environment Setup
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 4. Run the Script
Run the hello LLM script to send a prompt to Llama-3.3-70b:
```powershell
uv run python hello_llm.py
```

## 🛡️ Security Note
Never commit your `.env` file to version control. The [.gitignore](file:///c:/Users/callm/Desktop/AI%20ENGINNERING/week1/day1/.gitignore) file is configured to exclude `.env` and `.venv` automatically.
