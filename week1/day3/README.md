# Week 1 - Day 3: Token Tracking & Control

This project demonstrates how to track token usage (input, output, and total) and manage completion limits using `max_tokens` and inspecting the model's `finish_reason`.

## 🔑 Key Concepts Covered

1. **Token Usage Metrics (`response.usage`)**:
   - **`prompt_tokens`**: Tokens representing your input text.
   - **`completion_tokens`**: Tokens representing the model's generated response.
   - **`total_tokens`**: The sum of prompt and completion tokens (critical for cost tracking and rate-limiting).
2. **Controlling Length (`max_tokens`)**:
   - Restricts the maximum size of the model's output to prevent cost overruns and control latency.
3. **Finish Reasons (`finish_reason`)**:
   - **`stop`**: The model finished generating naturally.
   - **`length`**: The model was truncated because it hit the `max_tokens` threshold.

## 📂 Project Structure

- **[tokens.py](./tokens.py)**: Python script executing multiple prompt queries and printing usage diagnostics.
- **[README.md](./README.md)**: Explains the concepts, structure, and execution steps.

## 🚀 How to Run

### 1. Navigate & Sync Dependencies
Ensure you are in the `day3` directory:
```powershell
cd "c:\Users\callm\Desktop\AI ENGINNERING\week1\day3"
uv sync
```

### 2. Setup environment variables
Verify `.env` contains your key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run
```powershell
uv run python tokens.py
```
