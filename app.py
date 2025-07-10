# ✅ app.py — Streamlit Zoning Compliance Assistant

import streamlit as st
from zone_lookup import get_zone_by_address
from rag_agent import query_zoning
from letter_generator import format_letter

st.set_page_config(page_title="Miami 21 Zoning Advisor")
st.title("🏗️ Miami 21 Zoning Compliance Assistant")

# --- Inputs ---
address = st.text_input("Enter a Property Address (Miami, FL):")
manual_zone = st.text_input("Or enter a Zone Code manually (e.g., T4-L):")
question = st.text_area("Ask a zoning or permitting question:", height=100)

use_letter_format = st.checkbox("Generate Article 7-style compliance letter")

# --- Logic ---
if st.button("Submit"):
    if not address and not manual_zone:
        st.warning("Please provide an address or a zone code.")
    elif not question.strip():
        st.warning("Please enter a zoning question.")
    else:
        # Get zone from API if no manual input
        zone = manual_zone.strip()
        if not zone and address:
            zone = get_zone_by_address(address)
            if zone:
                st.success(f"Zone Detected: {zone}")
            else:
                st.error("Unable to retrieve zone from address. Please check spelling or format.")
                st.stop()

        # RAG + GPT logic
        answer = query_zoning(question=question, zone_code=zone)

        if use_letter_format:
            letter = format_letter(question, zone, answer)
            st.text_area("📄 Compliance Letter", letter, height=300)
        else:
            st.markdown("### 🧠 Zoning Compliance Answer")
            st.write(answer)

st.markdown("---")
st.markdown("Built using Miami 21 Code, Tables 3/4/13 and Article 7.")
