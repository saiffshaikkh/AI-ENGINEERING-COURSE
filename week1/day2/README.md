# Week 1 - Day 2: System Prompts & Temperature

This project demonstrates how to steer LLM behavior using **System Instructions** and control creativity via the **Temperature** hyperparameter.

## 🔑 Key Concepts Covered

1. **System Prompt (`role: "system"`)**:
   - Gives the LLM a persona (e.g., "You are a brand manager who suggests names...").
   - Enforces formatting rules (e.g., "name should be in one word, suggest one name only").
2. **Temperature (`temperature: 2.0`)**:
   - Controls randomness. Lower values (e.g., `0.2`) make outputs deterministic, while higher values (up to `2.0`) make outputs more creative and diverse.

## 📂 Project Structure

- **[sys_temp.py](file:///c:/Users/callm/Desktop/AI%20ENGINNERING/week1/day2/sys_temp.py)**: Main python script demonstrating the system persona and temperature configurations.
- **[README.md](file:///c:/Users/callm/Desktop/AI%20ENGINNERING/week1/day2/README.md)**: Current file explaining the concept and execution details.

## 🚀 How to Run

### 1. Setup Dependencies
Make sure you are in the `day2` directory:
```powershell
cd "c:\Users\callm\Desktop\AI ENGINNERING\week1\day2"
uv sync
```

### 2. Environment Variables
Ensure a `.env` file exists in the directory (or the parent directory) containing:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Execute the Script
Run the script using `uv`:
```powershell
uv run python sys_temp.py
```
