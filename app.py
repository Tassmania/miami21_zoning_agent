import streamlit as st
from zone_lookup import get_zone_by_address
from rag_agent import query_zoning
from letter_generator import generate_compliance_letter, get_permission_workflow

st.title("🏗️ Miami 21 Zoning Compliance Agent")
st.markdown("Check if a proposed use is allowed at a given Miami address.")

# Step 1: Address input
address = st.text_input("Enter a Miami address (e.g., 3232 NW 102nd St, Miami, FL)")

if st.button("Check Zoning"):
    with st.spinner("🔍 Looking up zoning and verifying use..."):
        zoning = get_zone_by_address(address)
        if zoning:
            st.success(f"📍 Zone found: **{zoning}**")
            st.session_state["zoning"] = zoning
            st.session_state["address"] = address
        else:
            st.error("⚠️ Unable to retrieve zone from address. Please check spelling or format.")

# Step 2: Ask your question
if "zoning" in st.session_state:
    question = st.text_area("Ask a zoning question related to this property", height=100)

    if st.button("Get Answer"):
        with st.spinner("🤖 Analyzing Miami 21 Code..."):
            result = query_zoning(question, st.session_state["zoning"])
            st.session_state["result"] = result
            st.success("✅ Answer ready:")
            st.markdown(result["answer"])
            st.session_state["use"] = result.get("use", "")
            st.session_state["permission_type"] = result.get("permission_type", "")

# Step 3: Generate Compliance Letter
if all(k in st.session_state for k in ["address", "zoning", "use", "permission_type"]):
    st.markdown("---")
    st.subheader("📄 Generate Zoning Compliance Letter")

    with st.form("letter_form"):
        custom_summary = st.text_area("Optional Summary (or leave blank to auto-generate)", "", height=100)
        generate_letter = st.form_submit_button("Generate Letter")

    if generate_letter:
        summary = custom_summary.strip() or get_permission_workflow(st.session_state["permission_type"])
        letter_text = generate_compliance_letter(
            st.session_state["address"],
            st.session_state["zoning"],
            st.session_state["use"],
            st.session_state["permission_type"],
            summary,
        )

        # Show preview
        st.text_area("📄 Letter Preview", value=letter_text, height=300)

        # Download as .txt
        st.download_button("📥 Download Letter (.txt)", letter_text, file_name="Zoning_Letter.txt", mime="text/plain")
else:
    st.info("ℹ️ Run a zoning lookup and ask a question to enable letter generation.")
