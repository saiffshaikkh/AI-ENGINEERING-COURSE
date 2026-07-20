# Week 1 - Day 5: AI Resume Parser & Candidate Matcher

An automated recruitment pipeline that extracts structured data from candidate resumes (`.pdf` and `.docx`), parses Job Descriptions into Pydantic models, and evaluates candidate alignment using LLMs.

## 🔑 Key Concepts Covered

1. **Multi-Format Document Extraction**:
   - Extracting text content from PDF files (`pypdf`) and Word documents (`python-docx`).
2. **Structured Information Extraction**:
   - Parsing unstructured resume text into a type-safe `Resume` Pydantic model (`skills`, `experience`, `education`, `projects`).
   - Extracting structured requirements (`JobD` model) from raw Job Descriptions.
3. **Automated Screening & Scoring**:
   - Prompting LLMs to perform candidate-to-job matching, generating an overall score (0–100), matching skills list, missing skills, and hiring verdicts (`MatchResult`).
4. **Batch Processing & Rate Limit Resilience**:
   - Iterating through resume directories and managing API rate limits between consecutive LLM completions.

## 📂 Project Structure

- **[resume_parser.py](./resume_parser.py)**: Main python script implementing document reading, schema extraction, LLM scoring, and candidate ranking.
- **[resumes/](./resumes)**: Directory holding candidate resume files (`.pdf` / `.docx`).
- **[README.md](./README.md)**: Current documentation file.

## 🚀 How to Run

### 1. Setup Dependencies
Make sure you are in the `day5` directory:
```powershell
cd "c:\Users\callm\Desktop\AI ENGINNERING\week1\day5"
uv sync
```

### 2. Environment Variables
Verify your `.env` contains your key:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the Parser
```powershell
uv run python resume_parser.py
```
