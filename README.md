# 🧠 Smart Lead Ranker

**An AI-powered tool that helps sales and investment teams filter, enrich, and rank B2B leads based on real-world trust indicators.**

> 🔗 [Live Demo](https://smart-lead-ranker.streamlit.app/)  
> 🎥 [Watch Demo Video](
> smart-lead-ranker guide.mp4)  
> 📄 [Project Report PDF](Smart%20Lead%20Ranker.pdf)

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Setup Instructions](#setup-instructions)
- [Screenshots](#screenshots)
- [AI Assistant Feature](#ai-assistant-feature)
- [Future Scope](#future-scope)
- [Demo Video](#demo-video)
- [Contact](#contact)

---

## 🧩 About the Project

Smart Lead Ranker is a lightweight AI application built for Caprae Capital’s AI-Readiness Internship Challenge. It automates the process of evaluating the **quality of leads** by using practical indicators like:
- Website status
- Domain age
- Email validity
- LinkedIn presence

The tool helps users **save time**, **focus on high-value leads**, and **make smarter business decisions**.

---

## 🚀 Features

✅ Upload your lead `.csv` file  
✅ Automated enrichment of leads  
✅ Intelligent scoring (0–10)  
✅ Auto-tagging (🔥 High / ⚠️ Medium / ❌ Low)  
✅ Download enriched leads  
✅ Optional AI voice assistant for user interaction  

---

## ⚙️ How It Works

| Step | What Happens |
|------|----------------|
| 1. Upload | Upload CSV with `Website`, `Email`, `LinkedIn URL` |
| 2. Enrichment | App checks each lead for domain age, validity, LinkedIn |
| 3. Scoring | Calculates score using weighted logic |
| 4. Tagging | Assigns High/Medium/Low tag |
| 5. Export | Download final ranked leads |

---

## 🧪 Tech Stack

- **Python 3.10+**
- [Streamlit](https://streamlit.io/)
- `requests`, `whois`, `re`, `pandas`
- `pyttsx3` (for AI voice assistant)

---

## 🛠 Setup Instructions

1. **Clone this repository:**

   ```bash
   git clone https://github.com/82PareshPatil/smart-lead-ranker.git
   cd smart-lead-ranker

