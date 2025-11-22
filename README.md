# HealthcareMAS 🏥
**Multi-Agent System for Healthcare Assistance**

Un sistema multi-agente avanzato progettato per assistere professionisti sanitari nella gestione integrata del paziente attraverso AI specializzata in diversi ambiti medici.

## 🎯 Panoramica del Progetto

HealthcareMAS è un sistema innovativo che utilizza agenti AI specializzati per supportare il processo decisionale medico in un ambiente "Human-in-the-Loop". Il sistema coordina tre agenti principali:

- 🩺 **MedAI** - Medico di base per analisi cliniche e piani terapeutici
- 🥗 **NutriAI** - Nutrizionista per piani alimentari personalizzati 
- 🧠 **PsyAI** - Psicologo per monitoraggio del benessere psicofisico

## ⚕️ Architettura del Sistema

### Pipeline di Workflow Clinico
```
Paziente → MedAI → NutriAI → PsyAI → Validazione Medico → Paziente
```

1. **Analisi Clinica**: MedAI analizza il report medico e genera un piano terapeutico
2. **Piano Nutrizionale**: NutriAI crea un piano alimentare sincronizzato con le terapie
3. **Monitoraggio Psicologico**: PsyAI valuta lo stato psicofisico e l'aderenza terapeutica
4. **Supervisione Medica**: Un medico qualificato valida tutte le raccomandazioni

### 🤖 Agenti Specializzati

#### MedAI - Medico di Base
- **Specializzazione**: Medicina interna e farmacologia clinica
- **Input**: Report clinici, risultati laboratorio, anamnesi
- **Output**: Piano terapeutico strutturato in JSON
- **Sicurezza**: Analisi drug interactions, flag di attenzione per il medico

#### NutriAI - Nutrizionista Clinico  
- **Specializzazione**: Piani alimentari personalizzati e sincronizzazione farmacologica
- **Input**: Piano terapeutico da MedAI
- **Output**: Piano settimanale completo (7 giorni) con timing farmaci
- **Features**: Drug-nutrient interactions, liste della spesa, macro bilanciamento

#### PsyAI - Psicologo Clinico
- **Specializzazione**: Analisi correlazione biometrica-psicologica
- **Input**: Feedback soggettivo + dati wearable (Apple Watch, Fitbit)
- **Output**: Assessment dello stato mentale con alerting medico
- **Monitoraggio**: HRV, qualità sonno, stress fisiologico

## 🛠️ Setup Tecnico

### Prerequisiti
```bash
Python 3.8+
OpenAI API Key
datapizza-ai framework
```

### Installazione
```bash
git clone https://github.com/FedeCarollo/HealthcareMAS
cd HealthcareMAS
pip install datapizza-ai
```

### Configurazione
1. Crea file `.env`:
```bash
OPEN_AI_KEY=your_openai_api_key_here
```

2. Importa il sistema di configurazione:
```python
from config import get_openai_key
```

## 🚀 Utilizzo

### Esempio Base - Workflow Completo
```python
from agents.medico_base import get_medico, clinical_summary
from agents.nutrizionista import get_nutrizionista  
from agents.psicologo import get_psyai, daily_payload
import json

# 1. Analisi Medica
medico = get_medico()
response = medico.run(clinical_summary)
piano_terapeutico = json.loads(response.text)

# 2. Piano Nutrizionale
nutrizionista = get_nutrizionista()
response = nutrizionista.run(json.dumps(piano_terapeutico))
piano_settimanale = json.loads(response.text)

# 3. Monitoraggio Psicologico
psicologo = get_psyai()
input_psicologo = {
    "clinical_summary": clinical_summary,
    "treatment_plan": piano_terapeutico, 
    "weekly_meal_plan": piano_settimanale,
    **daily_payload
}
assessment = psicologo.run(json.dumps(input_psicologo))
```

### Esempio Jupyter Notebook
Il progetto include un notebook interattivo (`notebook.ipynb`) che dimostra l'intero workflow clinico con dati di esempio.

## 📊 Formato Dati

### Input Clinico (MedAI)
```
- Anamnesi del paziente
- Parametri vitali (PA, FC, SpO2)
- Risultati laboratorio (HbA1c, colesterolo, ecc.)
- Sintomi e diagnosi preliminari
```

### Output Terapeutico (MedAI)
```json
{
  "diagnostic_summary": "Riassunto clinico",
  "treatment_plan": [
    {
      "medication": "Principio attivo",
      "dosage": "500mg", 
      "frequency": "1 compressa ogni 12 ore",
      "administration_instructions": "Dopo i pasti",
      "duration": "7 giorni",
      "purpose": "Finalità clinica"
    }
  ],
  "medical_recommendations": ["Consigli non farmacologici"],
  "attention_flag": "Alert per il medico"
}
```

## ⚠️ Compliance e Sicurezza

### Disclaimer Medico
- ❌ **NON sostituisce** la consulenza medica professionale
- ❌ **NON fornisce** diagnosi definitive 
- ❌ **NON prescrive** farmaci autonomamente
- ✅ **Supporta** il processo decisionale del medico
- ✅ **Richiede** sempre validazione da parte di professionista qualificato

### Privacy e HIPAA
- Tutti i dati del paziente sono processati localmente
- Nessuna informazione sensibile viene memorizzata permanentemente
- Compliance con standard di privacy sanitari

## 🔧 Personalizzazione Agenti

### Aggiungere Nuovi Tool
```python
from datapizza.tools import tool

@tool
def check_drug_interactions(med1: str, med2: str) -> str:
    """Verifica interazioni farmacologiche"""
    # Logic per controllo interazioni
    return f"Controllo {med1} vs {med2} completato"

# Aggiungi all'agente
agent = Agent(client=client, tools=[check_drug_interactions])
```

### Modificare Prompt Sistema
Ogni agente ha un `system_prompt` personalizzabile nel file corrispondente in `/agents/`.

## 📁 Struttura del Progetto
```
HealthcareMAS/
├── agents/
│   ├── client.py          # Client OpenAI condiviso
│   ├── medico_base.py     # Agente MedAI
│   ├── nutrizionista.py   # Agente NutriAI  
│   └── psicologo.py       # Agente PsyAI
├── config.py              # Gestione configurazioni
├── main.py                # Script principale
├── notebook.ipynb        # Demo interattiva
├── test.py                # Test sistema
└── README.md
```

## 📈 Casi d'Uso

### Scenario Tipico: Paziente con Sindrome Metabolica
1. **Input**: Report con diabete T2, ipertensione, GERD
2. **MedAI**: Prescrive Metformina, ACE-inibitore, PPI
3. **NutriAI**: Dieta mediterranea a basso sodio, timing farmaci sincronizzati
4. **PsyAI**: Monitora stress da cambio lifestyle, aderenza terapeutica

### Integrazione Wearable
PsyAI analizza dati da dispositivi come Apple Watch:
- Heart Rate Variability (HRV) 
- Qualità del sonno
- Livelli di attività
- Correlazione con stato emotivo self-reported

## 🤝 Contributi

Il progetto è open-source sotto licenza Apache 2.0. Contributi benvenuti per:
- Nuovi agenti specialistici 
- Integrazioni con API mediche
- Miglioramenti algoritmi di correlazione
- Test clinici e validazioni

## 📞 Supporto

Per supporto tecnico o questioni mediche:
- 🚨 **Emergenze**: Contatta sempre il 118
- 🏥 **Questioni Cliniche**: Consulta il tuo medico di fiducia
- 💻 **Supporto Tecnico**: Apri una issue su GitHub

---
**⚕️ Ricorda: Questo sistema supporta ma non sostituisce mai il giudizio clinico professionale**
