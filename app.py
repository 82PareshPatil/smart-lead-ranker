import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from utils import check_website, get_domain_age, validate_email, score_lead, tag_lead

st.set_page_config(
    page_title="Smart Lead Ranker",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Dark style with custom CSS
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: white;
    }
    .main {
        background-color: #000000;
        color: white;
    }
    h1, h2, h3, h4 {
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #FFD700;
        color: black;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        transition: 0.3s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #FFEB3B;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🧠 Smart Lead Ranker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload a CSV of leads and get enriched, ranked, and ready-to-use prospects.</p>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.markdown("⏳ <b>Processing leads...</b>", unsafe_allow_html=True)

    enriched_data = []

    for _, row in df.iterrows():
        website = row.get("Website", "")
        email = row.get("Email", "")
        linkedin = row.get("LinkedIn URL", "")

        website_ok = check_website(website)
        domain_age = get_domain_age(website)
        linkedin_ok = bool(linkedin and "linkedin.com" in linkedin)
        email_ok = validate_email(email)

        score = score_lead(website_ok, domain_age, linkedin_ok, email_ok)
        tag = tag_lead(score)

        enriched_data.append({
            **row,
            "Website OK": website_ok,
            "Domain Age": domain_age,
            "LinkedIn OK": linkedin_ok,
            "Email OK": email_ok,
            "Score": score,
            "Tag": tag
        })

    enriched_df = pd.DataFrame(enriched_data)
    st.success("✅ Leads Processed and Ranked!")

    st.dataframe(enriched_df)

    csv = enriched_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Enriched CSV",
        data=csv,
        file_name='ranked_leads.csv',
        mime='text/csv'
    )
# ElevenLabs Convai integration (add at the bottom or sidebar)
st.markdown("---")
st.subheader("💬 Need help? Talk to our AI Agent")

components.html("""
    <elevenlabs-convai agent-id="agent_01jy6eg2k9ffds3qf2vcp6m99g"></elevenlabs-convai>
    <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async type="text/javascript"></script>
""", height=400)