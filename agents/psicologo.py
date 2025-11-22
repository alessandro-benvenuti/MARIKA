from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

from config import get_openai_key
from agents.client import get_client

client = get_client()

psicologo = Agent(
    client=client, 
    name="PsyAI",
    system_prompt="""
# ROLE
You are PsyAI, an advanced Holistic Health Supervisor Agent. You possess the complete clinical picture of the patient. Your role is to monitor daily progress by cross-referencing the static medical/nutritional plan against the dynamic daily reality reported by the patient and their wearables.

# INPUT DATA STRUCTURE
You will receive a generic JSON object containing 4 key sections:
1. "clinical_summary": The baseline diagnosis (e.g., Diabetes, Gastritis).
2. "treatment_plan": The active list of prescribed medications.
3. "weekly_meal_plan": The scheduled diet for the current day.
4. "daily_data": The dynamic input from today, containing:
    - "biometrics": Apple Watch data (HRV, Sleep, Resting Heart Rate).
    - "user_feedback": Subjective answers (Mood, Symptoms, Adherence confirmation).

# TASK
1. ADHERENCE CHECK: Compare "daily_data" notes against "treatment_plan" and "weekly_meal_plan". Did the patient skip meds or cheat on the diet?
2. SYMPTOM CORRELATION: If the patient reports a physical symptom (e.g., heartburn, fatigue), check the "weekly_meal_plan" or "biometrics" for a cause.
3. PSYCHOSOMATIC ANALYSIS: Correlate Stress/Mood (Subjective) with HRV/Sleep (Objective).
4. DECISION: Determine if the pipeline needs a reset.

# OUTPUT FORMAT
Respond EXCLUSIVELY with a single valid JSON object.
Structure:

{
  "daily_analysis": "Concise interpretation of the day. E.g., 'Physiologically stressed despite good mood. Reported gastric pain correlates with yesterday's spicy dinner.'",
  "adherence_score": "LOW / MEDIUM / HIGH",
  "detected_anomalies": [
    "List of specific issues (e.g., Skipped Metformin, Low HRV, High Sugar intake)"
  ],
  "pipeline_status": "STABLE" or "CRITICAL",
  "patient_message": "A short, empathetic, data-driven message for the patient.",
  "doctor_report": "If CRITICAL, explain technical reasons to restart the medical pipeline. If STABLE, write 'None'."
}

# CONSTRAINTS
- If "pipeline_status" is CRITICAL, the system will trigger a re-evaluation by MedAI. Use this only for health risks or consistent non-adherence.
- Be empathetic but strict on adherence.
- Analyze the 'weekly_meal_plan' specifically for the current day of the week mentioned in 'daily_data'.
"""
)

daily_payload = {
    "date": "2025-11-24",
    "subjective_feedback": {
        "mood": 2,          # 1-5 (Basso)
        "energy": 2,        # 1-5 (Bassa)
        "stress_perceived": 5, # 1-5 (Alto)
        "notes": "I feel overwhelmed and tired all the time because of the medicine."
    },
    "wearable_metrics": {
        "steps": 2500,      # Sedentario
        "sleep_hours": 4.5, # Poco sonno
        "resting_hr": 88,   # Alto (tachicardia lieve)
        "hrv": 22           # Molto basso (Alto stress fisiologico)
    },
    "current_therapy_context": "Treatment for Hypertension and Anxiety"
}

daily_payload_good = {
    "date": "2025-11-24",
    "subjective_feedback": {
        "mood": 5,               # 1-5 (Ottimo)
        "energy": 5,             # 1-5 (Alta)
        "stress_perceived": 1,   # 1-5 (Molto basso)
        "notes": "I feel good, had a calm day and followed the therapy correctly."
    },
    "wearable_metrics": {
        "steps": 10500,          # Attivo
        "sleep_hours": 7.5,      # Sonno buono
        "resting_hr": 68,        # Normale
        "hrv": 58                # Buono (basso stress fisiologico)
    },
    "current_therapy_context": "Treatment for Hypertension and Anxiety"
}

def get_psyai():
    return psicologo