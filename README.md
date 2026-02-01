# AI-Powered Mock Interview Platform

## Problem
Traditional mock interviews are manual, subjective, and do not simulate real interview pressure, adaptability, or objective evaluation. As a result, many capable candidates perform poorly despite having strong technical skills.

## Solution
This project implements an **AI-powered mock interviewer** that simulates real-world interview behavior using adaptive decision logic.

The system:
- Analyzes the candidate’s resume
- Aligns questions with the job description
- Dynamically adapts question difficulty
- Enforces strict time limits
- Scores answers objectively
- Terminates interviews early if performance drops
- Produces a final Interview Readiness Score and hiring recommendation

---

## Key Features
- Resume and Job Description analysis
- Easy → Medium → Hard adaptive questioning
- Objective scoring based on:
  - Accuracy
  - Clarity
  - Depth
  - Relevance
  - Time efficiency
- Time pressure simulation
- Early interview termination logic
- Final readiness and hiring indicator

---

## How It Works
The interviewer is implemented as a **state-based decision system**:

