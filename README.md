# Cybersecurity-Research-Portfolio
SOC Lab Iranian Hackers


# Cybersecurity Research Portfolio

Cybersecurity and AI Safety projects focused on:

• Threat detection  
• SOC investigation  
• Threat intelligence  
• Detection engineering  
• Adversarial AI security testing  

---

## Skills Demonstrated

- SOC Analysis
- Threat Hunting
- Detection Engineering
- Python Security Tooling
- SIEM Investigation
- MITRE ATT&CK Mapping
- AI Security Research

---

## Portfolio Projects

### SOC Attack Simulation Lab

Simulated enterprise attack scenario including phishing, privilege escalation, and data exfiltration.

Features:

- synthetic SOC log dataset (~100k events)
- detection rules
- investigation workflow
- interactive SOC dashboard

  **soc_attack_simulation/**

  ### Detection Engineering Lab

Custom detection rules designed for SIEM platforms.

Includes:

- Sigma rules
- YARA signatures
- Sentinel KQL queries

**detection_engineering/**

### Threat Hunting Lab

Threat hunting exercises using a simulated SOC dataset.

Includes:

- hunt queries
- investigation playbook
- attack timeline

**threat_hunting/**

### Dark Web Threat Monitor

Python-based OSINT tool that scans forums for ransomware activity.

Features:

- forum scraping
- keyword monitoring
- threat classification


**darkweb_threat_monitor/**

### AI Adversarial Security Lab

Research on prompt injection and AI security vulnerabilities.

Includes:

- jailbreak tests
- adversarial prompts
- AI security assessment

  **ai_adversial_security**

  ## SOC Investigation Dashboard

Interactive dashboard for exploring SOC logs.

Features:

- event timeline visualization
- suspicious command detection
- log search interface

**streamlit run soc_dashboard/dashboard.py**

## Example Dataset

Synthetic SOC dataset includes:

- Windows process events
- user authentication logs
- network traffic logs

**~100,000 events**

Generate dataset:

**python soc_threat_dataset/generate_logs.py**

## Project Architecture

Attacker Simulation  
↓  
Endpoint Activity  
↓  
SOC Log Dataset  
↓  
Threat Hunting Queries  
↓  
Detection Engineering  
↓  
SOC Dashboard Investigation

---

## Technologies Used

Python  
PowerShell  
Streamlit  
Pandas  
Sigma  
YARA  
KQL  
MITRE ATT&CK

---
**## License**

All rights reservered 

This repository contains simulated cybersecurity attack scenarios for defensive security research, SOC training, and detection engineering practice.

No real organizations or systems are targeted.
