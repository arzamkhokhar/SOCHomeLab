# SOC Home Lab

A home lab simulating a Security Operations Center (SOC) environment using Wazuh SIEM, Windows 10, and Kali Linux.

## Lab Architecture
- **Ubuntu-Wazuh** (192.168.56.101) — Wazuh SIEM server
- **Windows-Endpoint** (192.168.56.103) — Monitored victim machine (Sysmon + Wazuh agent)
- **Kali-Attacker** (192.168.56.102) — Unmonitored attacker machine

## Tools Used
- Wazuh 4.9 (SIEM, detection rules, dashboard)
- Sysmon (process-level logging on Windows)
- VirtualBox (virtualization)
- Python 3 (log parsing automation)

## What I Did
- Built a 3-VM isolated lab network from scratch
- Installed and configured Wazuh SIEM with a Windows agent
- Simulated brute-force and discovery attacks
- Wrote a custom Wazuh correlation rule (T1110 - Brute Force)
- Built a Python script to parse logs and export CSV reports
- Mapped all detections to MITRE ATT&CK framework

## Folder Structure
- `screenshots/` — Evidence screenshots from each scenario
- `detectionrules/` — Custom Wazuh XML rules
- `incidentreports/` — Incident report documents
- `mitremapping/` — MITRE ATT&CK mapping summary
- `pythontools/` — Python automation scripts

## MITRE ATT&CK Coverage
| Technique | ID | Tactic |
|---|---|---|
| Brute Force | T1110 | Credential Access |
| Account Discovery | T1087 | Discovery |
