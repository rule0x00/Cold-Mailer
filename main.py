import streamlit as st
import tempfile
from nodes.parse import parse_document
from nodes.chunk import chunk_document
from nodes.embed import embed_document

st.set_page_config(page_title="Resume Uploader", layout="centered")
st.title("📄 COLD MAIL GENERATOR")

st.subheader("🔐 Resume & Profile Details")


user_name = st.text_input("Your Name")
resume_name = st.text_input("Resume Name")


uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

with st.form("portfolio_form"):
    st.subheader("🔗 Portfolio Links")

    github_link = st.text_input("GitHub Profile URL")
    resume_link = st.text_input("Resume (Hosted URL)")
    portfolio_website = st.text_input("Portfolio Website")
    linkedin_link = st.text_input("LinkedIn URL")

    submit_button = st.form_submit_button("Submit")

    if submit_button:
        if not (user_name and resume_name and uploaded_file):
            st.error("Please provide your name, resume name, and upload a resume.")
        elif not github_link or not resume_link:
            st.error("Please provide at least GitHub and Hosted Resume links.")
        else:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            with st.spinner("🔍 Parsing your resume..."):
                text = parse_document(tmp_path)

            with st.spinner("✂️ Chunking text..."):
                chunks = chunk_document(text)

            with st.spinner("🧠 Embedding chunks..."):
                metadata = {
                    "User": user_name,
                    "ResumeName": resume_name,
                    "GitHub": github_link,
                    "ResumeLink": resume_link,
                    "Portfolio": portfolio_website,
                    "LinkedIn": linkedin_link,
                }
                embeddings = embed_document(chunks, metadata)

            st.success("STORED YOUR RESUME! ✅")
