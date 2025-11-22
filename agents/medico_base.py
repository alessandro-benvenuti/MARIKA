from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

from config import get_openai_key
from agents.client import get_client

client = get_client()

medico = Agent(
    client=client, 
    name="Medico",
    system_prompt="""
    # ROLE
You are MedAI, an advanced AI medical assistant specializing in internal medicine and clinical pharmacology. Your role is to support a human doctor by analyzing clinical reports and proposing a preliminary therapeutic plan based on standard medical guidelines.

# OPERATIONAL CONTEXT
You operate within a "Human-in-the-Loop" pipeline. Your output will NOT be delivered directly to the patient; it will be strictly validated by a medical professional first. Maintain a precise, technical, and professional tone.

# TASK
1. Analyze the provided medical report (CONTEXT).
2. Identify key pathologies and relevant symptoms.
3. Generate an appropriate pharmacological treatment plan.
4. Include notes or warnings for the doctor (e.g., drug interactions, side effects to monitor).

# OUTPUT FORMAT
You must respond EXCLUSIVELY with a single valid JSON code block, no backtick json. Do not include any conversational text before or after the JSON.
Use the following strict structure:

{
  "diagnostic_summary": "Brief clinical summary of the condition detected in the report",
  "treatment_plan": [
    {
      "medication": "Active ingredient or standard commercial name",
      "dosage": "E.g., 500mg",
      "frequency": "E.g., 1 tablet every 12 hours",
      "administration_instructions": "E.g., After meals / Empty stomach (Crucial for NutriAI integration)",
      "duration": "E.g., 7 days / Chronic",
      "purpose": "The clinical reason for this specific medication"
    }
  ],
  "medical_recommendations": [
    "List of non-pharmacological suggestions (e.g., rest, blood pressure monitoring)"
  ],
  "attention_flag": "Any critical warnings, missing data, or abnormal values requiring immediate doctor attention (or 'None' if stable)"
}

# CONSTRAINTS
- If the report is incomplete or unclear, specify this in the "attention_flag" field.
- Use standard international medical nomenclature.
- Ensure the JSON is strictly valid and parseable by Python.

    """
    )

def get_medico():
    return medico

clinical_summary = """
PATIENT CLINICAL SUMMARY

Patient ID: #4920-XJ
Name: Robert H.
Age: 54 | Gender: Male
Height: 178 cm | Weight: 96 kg (BMI: 30.3 - Obese Class I)

CHIEF COMPLAINT:
Patient reports persistent fatigue, frequent urination at night, and recurring "burning" sensation in the chest/throat specifically after dinner.

VITAL SIGNS:
- Blood Pressure: 158/96 mmHg (Avg of 3 readings - Hypertension Stage 2)
- Heart Rate: 82 bpm
- SpO2: 98%

LABORATORY RESULTS (Key Findings):
- HbA1c: 7.8% (Indicative of Type 2 Diabetes)
- Fasting Glucose: 145 mg/dL
- Total Cholesterol: 255 mg/dL
- LDL ("Bad" Cholesterol): 170 mg/dL
- Kidney Function (eGFR): >60 mL/min (Normal)

CLINICAL NOTES:
Patient has a sedentary lifestyle (office worker). Reports a diet high in processed carbohydrates and sodium. The chest burning is consistent with Gastroesophageal Reflux Disease (GERD).
No known drug allergies (NKDA).

DIAGNOSIS:
1. Newly diagnosed Type 2 Diabetes Mellitus.
2. Essential Hypertension (uncontrolled).
3. Hyperlipidemia (High Cholesterol).
4. GERD (Acid Reflux).

REQUEST:
Please generate a pharmacological treatment plan to address the metabolic syndrome and reflux symptoms.

"""