# 🔐 AI Cybersecurity Agent for Scam Detection

An event-driven **AI cybersecurity agent** that automatically detects phishing and scam messages in real time. The system analyzes SMS-like text, extracts URLs, checks them using **VirusTotal threat intelligence**, applies heuristic text analysis, and generates an **explainable risk verdict with a confidence score**.

---

## 🚀 Features

- 📩 Real-time analysis of SMS-like messages  
- 🔗 Automatic URL extraction from message content  
- 🛡️ Threat-intelligence integration using VirusTotal API  
- 🧠 Heuristic text-based scam detection  
- 📊 Explainable verdict: **SAFE / SUSPICIOUS / HIGH RISK**  
- 🔢 Confidence score (%) for each prediction  
- 🌐 Web-based simulation UI for live demos  

---

## 🏗️ System Architecture

Message Event (SMS Simulation)
↓
AI Cyber Agent (FastAPI Backend)
|
|-- URL Extraction
|-- VirusTotal Threat Check
|-- Text Pattern Analysis
|-- Risk Aggregation Engine
↓
Final Verdict + Confidence Score

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI  
- **Threat Intelligence:** VirusTotal API  
- **Frontend:** HTML, CSS, JavaScript  
- **Server:** Uvicorn  

---

## 📁 Project Structure
backend/
├── main.py
├── agent/
│ └── cyber_agent.py
├── services/
│ └── vt_service.py
├── analysis/
│ ├── text_analysis.py
│ └── decision.py
├── utils/
│ └── extractor.py
├── config/
│ └── settings.py
├── requirements.txt


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ai-cyber-agent.git
cd ai-cyber-agent/backend


2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add VirusTotal API Key

Create a .env file inside backend/:

VT_API_KEY=your_virustotal_api_key_here

4️⃣ Run the backend server
python -m uvicorn main:app --reload

🧪 Testing the Agent
Using Swagger UI

Open:

http://127.0.0.1:8000/docs


Test with:

{
  "message": "Your KYC is blocked. Click https://upi-refund.xyz immediately"
}

🌐 Frontend Demo

Open index.html using Live Server or a local HTTP server

Paste an SMS message into the textarea

The agent automatically analyzes and displays the verdict
