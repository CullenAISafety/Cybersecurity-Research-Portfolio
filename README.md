# Cybersecurity-Research-Portfolio
SOC Lab 
_____________________________________________________________________________________________________________________________________________________________________________
**Cybersecurity Research SOC Lab**

SOC simulation platform for threat detection engineering, incident investigation, and AI adversarial testing.

This repository simulates realistic enterprise security telemetry and provides tools for:

• SOC attack simulation
• detection engineering
• threat hunting
• malware analysis
• threat intelligence monitoring
• AI adversarial security testing
• interactive SOC investigation dashboard

The goal of the project is to demonstrate practical cybersecurity capabilities similar to those used by professional SOC and incident response teams at organizations like:

CrowdStrike

Microsoft

Mandiant

Features
**SOC Attack Simulation**

Generates realistic enterprise security logs simulating user behavior and attacker activity.

Includes simulated behaviors such as:

malicious PowerShell execution

phishing payload download

data exfiltration simulation

Used for:

SOC analyst training

detection engineering testing

incident investigation exercises

**Detection Engineering**

Detection engine for identifying suspicious activity in log telemetry.

Example detections include:

PowerShell payload downloads

encoded command execution

suspicious command-line behavior

Includes Sigma-style detection rules.

**Threat Hunting Engine**

Threat hunting scripts to identify anomalies across security logs.

Capabilities include:

process behavior analysis

attacker infrastructure discovery

command-line pattern analysis

**Malware Sandbox (Safe Static Analysis)**

Lightweight malware analysis environment that performs:

file hashing (SHA256)

suspicious string extraction

command and network artifact detection

This simulates the early triage process used in malware analysis labs.

**Dark Web Threat Monitor**

Simulated threat intelligence monitoring tool that scans public web sources for indicators of:

ransomware activity

leaked data mentions

initial access brokers

fraud operations

Includes a small machine learning classifier to categorize threat posts.

**AI Adversarial Security Lab**

Security testing environment for evaluating AI systems against adversarial prompts.

Tests include:

prompt injection attempts

data exfiltration attempts

policy bypass attempts

This simulates red-team testing used in AI safety evaluations.

**Threat Actor Infrastructure Map**

Visualization tool for mapping attacker infrastructure globally.

Shows:

command-and-control servers

phishing infrastructure

data exfiltration nodes

**SOC Alert Correlation Engine**

Basic SOC correlation engine that links multiple alerts into a single security incident.

Example correlations:

PowerShell execution

payload download

suspicious outbound connection

This simulates incident grouping used in modern security platforms.

**Live SOC Investigation Dashboard**

Interactive dashboard built with Streamlit for SOC analysts.

Capabilities include:

event timeline visualization

process behavior statistics

suspicious activity detection

log search and investigation

_____________________________________________________________________________________________________________________________________________________________________________


**Repository Structure**
cybersecurity-research-portfolio

soc_attack_simulation
detection_engineering
threat_hunting
malware_sandbox
darkweb_threat_monitor
ai_adversarial_security
threat_actor_map
soc_correlation_engine
soc_dashboard
Installation

**Clone the repository:**

git clone https://github.com/CullenAISafety/cybersecurity-research-portfolio
cd cybersecurity-research-portfolio

**Install dependencies:**


pip install -r requirements.txt


**Running the Lab**

**Generate SOC Logs**

python soc_attack_simulation/attack_simulator.py

**Run Detection Engine**

python detection_engineering/detection_engine.py

**Run Threat Hunting**

python threat_hunting/hunt_engine.py

**Analyze Malware Sample**

python malware_sandbox/sandbox_analyzer.py

**Run Dark Web Monitor**

python darkweb_threat_monitor/darkweb_scraper.py

**Run AI Red Team Tests**

python ai_adversarial_security/redteam_tester.py

**Launch SOC Dashboard**

streamlit run soc_dashboard/dashboard.py


[setup.sh(https://github.com/CullenAISafety/Cybersecurity-Research-Portfolio/blob/main/setup.sh)}
_____________________________________________________________________________________________________________________________________________________________________________


**## License**

All rights reservered 

This repository contains simulated cybersecurity attack scenarios for defensive security research, SOC training, and detection engineering practice.

No real organizations or systems are targeted.
