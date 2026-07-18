# Week 1 - Day 4: Structured Outputs with Pydantic

This project demonstrates how to enforce structured JSON outputs from LLMs using **Pydantic Schemas** and the Groq client's **JSON Mode**.

## 🔑 Key Concepts Covered

1. **Pydantic Schemas (`BaseModel`)**:
   - Establish strict type-safe schemas in Python to represent LLM outputs.
   - Automatically generate JSON schemas using `model_json_schema()` to feed into system instructions.
2. **Groq JSON Mode (`response_format`)**:
   - Forcing the model to output a valid, parseable JSON string using `"type": "json_object"`.
3. **Data Parsing & Validation**:
   - Converting the raw output to a Python dictionary via `json.loads()`.
   - Re-instantiating the dictionary into a Pydantic object `Ticket(**data)` to validate inputs at runtime.

## 📂 Project Structure

- **[json_pydantic.py](./json_pydantic.py)**: Python script showing schema generation, JSON Mode execution, and Pydantic validation.
- **[README.md](./README.md)**: Current documentation.

## 🚀 How to Run

### 1. Navigate & Setup
```powershell
cd "c:\Users\callm\Desktop\AI ENGINNERING\week1\day4"
uv sync
```

### 2. Configure Credentials
Verify that your `.env` contains your key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Execute
```powershell
uv run python json_pydantic.py
```
