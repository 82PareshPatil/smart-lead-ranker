import requests
import whois
import re
from datetime import datetime

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except:
        return False

def get_domain_age(url):
    try:
        domain = whois.whois(url)
        creation_date = domain.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        age = (datetime.now() - creation_date).days // 365
        return age
    except:
        return 0

def validate_email(email):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

def score_lead(website_ok, domain_age, linkedin_ok, email_ok):
    score = 0
    if website_ok: score += 2
    if linkedin_ok: score += 2
    if email_ok: score += 3
    if domain_age > 1: score += 3
    return score

def tag_lead(score):
    if score >= 8:
        return "🔥 High"
    elif score >= 5:
        return "⚠️ Medium"
    else:
        return "❌ Low"
