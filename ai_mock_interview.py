import time
import random
import re

# ==================================================
# CONFIGURATION
# ==================================================
MAX_QUESTIONS = 5
TIME_LIMIT = 30  # seconds per question

DIFFICULTY_LEVELS = ["easy", "medium", "hard"]

QUESTION_BANK = {
    "easy": [
        "Explain REST APIs.",
        "What is a primary key in a database?",
        "What is Git and why is it used?"
    ],
    "medium": [
        "How does JWT authentication work?",
        "Explain ACID properties in databases.",
        "What is database normalization?"
    ],
    "hard": [
        "Design a scalable authentication system.",
        "How would you optimize a high-traffic API?",
        "Design a URL shortener system."
    ]
}

# ==================================================
# HELPER FUNCTIONS
# ==================================================
def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return set(words)

def extract_experience(text):
    match = re.search(r'(\d+)\s+year', text.lower())
    return int(match.group(1)) if match else 0

# ==================================================
# RESUME & JD ANALYSIS
# ==================================================
def analyze_resume(resume_text):
    return {
        "skills": extract_keywords(resume_text),
        "experience": extract_experience(resume_text)
    }

def analyze_jd(jd_text):
    return {
        "required_skills": extract_keywords(jd_text)
    }

def calculate_skill_match(resume_skills, jd_skills):
    if not jd_skills:
        return 0
    return round((len(resume_skills & jd_skills) / len(jd_skills)) * 100)

# ==================================================
# SCORING ENGINE
# ==================================================
def score_answer(answer, response_time):
    word_count = len(answer.split())

    accuracy = min(40, word_count * 2)     # proxy for correctness
    clarity = 20 if word_count > 20 else 10
    depth = 20 if word_count > 40 else 10
    relevance = 10 if any(
        kw in answer.lower() for kw in ["api", "system", "design", "data", "auth"]
    ) else 5
    time_score = 10 if response_time <= TIME_LIMIT else 0

    return accuracy + clarity + depth + relevance + time_score

# ==================================================
# ADAPTIVE DIFFICULTY
# ==================================================
def update_difficulty(current_level, score):
    if score >= 75 and current_level < 2:
        return current_level + 1
    elif score < 40 and current_level > 0:
        return current_level - 1
    return current_level

# ==================================================
# EARLY TERMINATION CHECK
# ==================================================
def should_terminate(scores):
    if len(scores) >= 3:
        recent_avg = sum(scores[-3:]) / 3
        return recent_avg < 35
    return False

# ==================================================
# FINAL REPORT
# ==================================================
def generate_final_report(scores):
    avg_score = round(sum(scores) / len(scores))

    if avg_score >= 75:
        category = "Strong"
    elif avg_score >= 50:
        category = "Average"
    else:
        category = "Needs Improvement"

    return {
        "Final Interview Readiness Score": avg_score,
        "Performance Level": category,
        "Strengths": "Good conceptual understanding" if avg_score >= 60 else "Basic fundamentals",
        "Weaknesses": "System design & time management" if avg_score < 75 else "Minor gaps",
        "Hiring Recommendation": category
    }

# ==================================================
# INTERVIEW ENGINE
# ==================================================
def run_interview(resume_text, jd_text):
    resume_data = analyze_resume(resume_text)
    jd_data = analyze_jd(jd_text)

    print("\n================ RESUME ANALYSIS ================")
    print(f"Experience: {resume_data['experience']} years")
    print(f"Skill Match: {calculate_skill_match(resume_data['skills'], jd_data['required_skills'])}%")

    difficulty = 0
    scores = []

    for i in range(MAX_QUESTIONS):
        question = random.choice(QUESTION_BANK[DIFFICULTY_LEVELS[difficulty]])

        print(f"\nQ{i + 1} ({DIFFICULTY_LEVELS[difficulty].upper()}): {question}")
        print(f"You have {TIME_LIMIT} seconds.")

        start_time = time.time()
        answer = input("Your answer: ")
        end_time = time.time()

        response_time = round(end_time - start_time, 2)
        score = score_answer(answer, response_time)

        scores.append(score)
        difficulty = update_difficulty(difficulty, score)

        print(f"Score: {score}/100 | Time Taken: {response_time}s")

        if should_terminate(scores):
            print("\n⚠ Interview terminated early due to low performance.")
            break

    report = generate_final_report(scores)

    print("\n================ FINAL REPORT ================")
    for key, value in report.items():
        print(f"{key}: {value}")

# ==================================================
# ENTRY POINT
# ==================================================
if __name__ == "__main__":
    print("=== AI-POWERED MOCK INTERVIEW PLATFORM ===")

    resume_text = input("\nPaste Resume Text:\n")
    jd_text = input("\nPaste Job Description Text:\n")

    run_interview(resume_text, jd_text)
