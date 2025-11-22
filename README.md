# HealthcareMAS 🏥
**Multi-Agent System for Healthcare Assistance**

An advanced multi-agent system designed to assist healthcare professionals in integrated patient management through specialized AI agents across different medical domains.

## 🎯 Project Overview

HealthcareMAS is an innovative system that uses specialized AI agents to support medical decision-making in a "Human-in-the-Loop" environment. The system coordinates three main agents:

- 🩺 **MedAI** - Primary care physician for clinical analysis and therapeutic plans
- 🥗 **NutriAI** - Nutritionist for personalized meal planning
- 🧠 **PsyAI** - Psychologist for psychophysical wellness monitoring

## ⚕️ System Architecture

### Clinical Workflow Pipeline
```
Patient → MedAI → NutriAI → PsyAI → Medical Validation → Patient
```

1. **Clinical Analysis**: MedAI analyzes medical reports and generates therapeutic plans
2. **Nutritional Planning**: NutriAI creates meal plans synchronized with therapies
3. **Psychological Monitoring**: PsyAI evaluates psychophysical state and therapy adherence
4. **Medical Supervision**: A qualified physician validates all recommendations

### 🤖 Specialized Agents

#### MedAI - Primary Care Physician
- **Specialization**: Internal medicine and clinical pharmacology
- **Input**: Clinical reports, laboratory results, patient history
- **Output**: Structured therapeutic plan in JSON format
- **Safety**: Drug interaction analysis, attention flags for physicians

#### NutriAI - Clinical Nutritionist  
- **Specialization**: Personalized meal planning and pharmacological synchronization
- **Input**: Therapeutic plan from MedAI
- **Output**: Complete 7-day plan with medication timing
- **Features**: Drug-nutrient interactions, shopping lists, macro balancing

#### PsyAI - Clinical Psychologist
- **Specialization**: Biometric-psychological correlation analysis
- **Input**: Subjective feedback + wearable data (Apple Watch, Fitbit)
- **Output**: Mental state assessment with medical alerting
- **Monitoring**: HRV, sleep quality, physiological stress

## 🛠️ Technical Setup

### Prerequisites
```bash
Python 3.8+
OpenAI API Key
datapizza-ai framework (Core dependency)
```

### Installation
```bash
git clone https://github.com/FedeCarollo/HealthcareMAS
cd HealthcareMAS

# Install all dependencies from requirements.txt
pip install -r requirements.txt

# Or install manually
pip install datapizza-ai
```

### Datapizza-AI Framework Integration
HealthcareMAS is built on the **datapizza-ai** framework, a powerful tool for creating specialized AI agents:

- **🤖 Agent Creation**: Simple agent instantiation with custom prompts
- **🔧 Tool Integration**: Easy addition of custom medical tools
- **🔗 Client Management**: Unified OpenAI API client handling
- **📊 Response Processing**: Structured JSON output parsing

```python
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient
from datapizza.tools import tool

# Example: Creating a medical agent with datapizza
client = OpenAIClient(api_key=your_api_key)
agent = Agent(
    client=client,
    name="MedicalAssistant",
    system_prompt="Your specialized medical prompt...",
    tools=[your_custom_tools]
)
```

### Configuration
1. Create `.env` file:
```bash
OPEN_AI_KEY=your_openai_api_key_here
```

2. Import configuration system:
```python
from config import get_openai_key
```

## 🚀 Usage

### Basic Example - Complete Workflow
```python
# Unified Pipeline Function (Recommended)
from healthcare_mas_pipeline import healthcare_mas_pipeline
from agents.medico_base import clinical_summary
from agents.psicologo import daily_payload

# Complete execution with automatic file saving
result = healthcare_mas_pipeline(
    clinical_summary=clinical_summary,
    daily_data=daily_payload,
    doctor_report=None,  # Optional medical updates
    save_folder="medical_reports"  # Custom folder name
)

# Access results
medical_plan = result['medical_plan']
nutrition_plan = result['nutrition_plan']
psych_assessment = result['psychological_assessment']
```

### Manual Step-by-Step Workflow
```python
from agents.medico_base import get_medico, clinical_summary
from agents.nutrizionista import get_nutrizionista  
from agents.psicologo import get_psyai, daily_payload
import json

# 1. Medical Analysis
medico = get_medico()
response = medico.run(clinical_summary)
piano_terapeutico = json.loads(response.text)

# 2. Nutritional Planning
nutrizionista = get_nutrizionista()
response = nutrizionista.run(json.dumps(piano_terapeutico))
piano_settimanale = json.loads(response.text)

# 3. Psychological Monitoring
psicologo = get_psyai()
input_psicologo = {
    "clinical_summary": clinical_summary,
    "treatment_plan": piano_terapeutico, 
    "weekly_meal_plan": piano_settimanale,
    **daily_payload
}
assessment = psicologo.run(json.dumps(input_psicologo))
```

### Interactive Jupyter Notebook
The project includes an interactive notebook (`notebook.ipynb`) demonstrating the complete clinical workflow with example data.

## 📊 Data Format

### Clinical Input (MedAI)
```
- Patient history
- Vital signs (BP, HR, SpO2)
- Laboratory results (HbA1c, cholesterol, etc.)
- Symptoms and preliminary diagnosis
```

### Therapeutic Output (MedAI)
```json
{
  "diagnostic_summary": "Clinical summary",
  "treatment_plan": [
    {
      "medication": "Active ingredient",
      "dosage": "500mg", 
      "frequency": "1 tablet every 12 hours",
      "administration_instructions": "After meals",
      "duration": "7 days",
      "purpose": "Clinical purpose"
    }
  ],
  "medical_recommendations": ["Non-pharmacological suggestions"],
  "attention_flag": "Medical alerts or 'None'"
}
```

## 📁 Automatic File Management

### Generated Reports
The `healthcare_mas_pipeline()` function automatically generates:

- **📄 `medical_plan_{timestamp}.json`** - Complete therapeutic plan
- **🥗 `nutrition_plan_{timestamp}.json`** - Weekly meal plan
- **🧠 `psychological_assessment_{timestamp}.json`** - Psychological assessment
- **📋 `complete_summary_{timestamp}.json`** - Complete summary
- **📖 `human_readable_report_{timestamp}.txt`** - Human-readable report
- **🛒 `shopping_list_{timestamp}.txt`** - Shopping list (if available)

### File Structure Example
```
medical_reports_20251122_143052/
├── medical_plan_20251122_143052.json
├── nutrition_plan_20251122_143052.json
├── psychological_assessment_20251122_143052.json
├── complete_summary_20251122_143052.json
├── human_readable_report_20251122_143052.txt
└── shopping_list_20251122_143052.txt
```

## ⚠️ Compliance and Safety

### Medical Disclaimer
- ❌ **DOES NOT replace** professional medical consultation
- ❌ **DOES NOT provide** definitive diagnoses
- ❌ **DOES NOT prescribe** medications autonomously
- ✅ **SUPPORTS** physician decision-making
- ✅ **REQUIRES** validation by qualified professionals

### Privacy and HIPAA
- All patient data is processed locally
- No sensitive information is permanently stored
- Compliant with healthcare privacy standards

## 🔧 Agent Customization

### Adding New Tools with Datapizza Framework
The datapizza-ai framework makes tool integration seamless:

```python
from datapizza.tools import tool
from datapizza.agents import Agent

@tool
def check_drug_interactions(med1: str, med2: str) -> str:
    """Check drug interactions using medical databases"""
    # Advanced interaction checking logic
    return f"Interaction analysis: {med1} vs {med2} - Status: Safe/Warning/Contraindicated"

@tool
def calculate_drug_dosage(weight: float, age: int, medication: str) -> str:
    """Calculate appropriate drug dosage based on patient parameters"""
    # Dosage calculation algorithm
    return f"Recommended dosage for {medication}: calculated based on {weight}kg, {age}y"

# Create enhanced medical agent
enhanced_agent = Agent(
    client=client,
    name="EnhancedMedAI", 
    system_prompt="Advanced medical AI with drug interaction analysis...",
    tools=[check_drug_interactions, calculate_drug_dosage]
)
```

### Modifying System Prompts
Each agent has a customizable `system_prompt` leveraging datapizza's prompt engineering:

## 📁 Project Structure
```
HealthcareMAS/
├── agents/
│   ├── client.py          # Shared OpenAI client (datapizza integration)
│   ├── medico_base.py     # MedAI agent (datapizza Agent)
│   ├── nutrizionista.py   # NutriAI agent (datapizza Agent)
│   └── psicologo.py       # PsyAI agent (datapizza Agent)
├── .github/
│   └── copilot-instructions.md  # AI coding guidelines
├── config.py              # Configuration management
├── main.py                # Main script
├── notebook.ipynb        # Interactive demo
├── test.py                # System tests
├── requirements.txt       # Project dependencies
└── README.md
```

## 🔧 Datapizza-AI Framework Features

### Core Agent Architecture
Each healthcare agent leverages datapizza-ai's robust architecture:

```python
# Agent creation with datapizza framework
from datapizza.agents import Agent
from datapizza.clients.openai import OpenAIClient

agent = Agent(
    client=OpenAIClient(api_key=api_key),
    name="HealthcareAgent",
    system_prompt="Specialized medical prompt",
    tools=[medical_tools]  # Custom healthcare tools
)

# Structured agent execution
response = agent.run(clinical_input)
structured_output = json.loads(response.text)
```

### Medical Tool Integration
Datapizza's `@tool` decorator enables seamless medical tool integration:

```python
from datapizza.tools import tool

@tool
def analyze_vital_signs(bp: str, hr: int, temp: float) -> str:
    """Analyze patient vital signs using medical protocols"""
    # Medical analysis logic
    return clinical_assessment

@tool
def check_drug_interactions(med1: str, med2: str) -> str:
    """Check potential drug interactions"""
    # Drug interaction database lookup
    return interaction_report
```

## 📈 Use Cases

### Typical Scenario: Patient with Metabolic Syndrome
1. **Input**: Report with T2 diabetes, hypertension, GERD
2. **MedAI**: Prescribes Metformin, ACE inhibitor, PPI
3. **NutriAI**: Mediterranean low-sodium diet, synchronized medication timing
4. **PsyAI**: Monitors lifestyle change stress, therapy adherence

### Wearable Integration
PsyAI analyzes data from devices like Apple Watch:
- Heart Rate Variability (HRV) 
- Sleep quality
- Activity levels
- Correlation with self-reported emotional state

### Doctor Report Updates
The system supports iterative medical updates:
```python
# Example with doctor feedback
doctor_update = """
MEDICAL UPDATE - Dr. Smith Review (2025-11-22):
1. Increase Metformin to 1000mg twice daily
2. Add Atorvastatin 20mg daily
3. Monitor for lactic acidosis
"""

result = healthcare_mas_pipeline(
    clinical_summary=clinical_summary,
    daily_data=daily_payload,
    doctor_report=doctor_update,  # Medical update
    save_folder="updated_reports"
)
```

## 🤝 Contributions

The project is open-source under Apache 2.0 license. Contributions welcome for:
- New specialized agents 
- Medical API integrations
- Correlation algorithm improvements
- Clinical testing and validations

## 📞 Support

For technical support or medical questions:
- 🚨 **Emergencies**: Always contact 911/emergency services
- 🏥 **Clinical Questions**: Consult your healthcare provider
- 💻 **Technical Support**: Open a GitHub issue

---
**⚕️ Remember: This system supports but never replaces professional clinical judgment**
