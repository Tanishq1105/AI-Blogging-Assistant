import streamlit as st
from config import settings
from llm_client import generate_with_retry, stream_generate
from prompt_builder import build_blog_prompt
from seo import improve_seo
from utils import estimate_tokens
from pdf_export import create_pdf

st.set_page_config(layout="wide")
st.title("🚀 AI Blog Generator (Advanced)")

# Session state
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords")

    num_words = st.slider("Words", 250, 1500, 500)

    model_choice = "models/gemini-flash-latest"

    style_choice = st.selectbox(
        "Style",
        ["SEO-optimized", "Casual", "Technical", "Storytelling"]
    )

    enhance = st.checkbox("✨ SEO Enhance")
    stream = st.checkbox("⚡ Stream Output")

    generate = st.button("Generate")

# Title generator
if st.button("💡 Suggest Titles"):
    if keywords:
        titles = generate_with_retry(
            f"Generate 5 blog titles for: {keywords}",
            model_choice
        )
        st.write(titles)

# Main
if generate:
    if not blog_title or not keywords:
        st.warning("Enter title and keywords")
    else:
        prompt = build_blog_prompt(
            blog_title,
            keywords,
            num_words,
            style_choice
        )

        st.info(f"Estimated tokens: {estimate_tokens(prompt)}")

        st.subheader("📄 Blog Output")

        try:
            if stream:
                placeholder = st.empty()
                full_text = ""

                for chunk in stream_generate(prompt, model_choice):
                    full_text += chunk
                    placeholder.markdown(full_text)

                blog = full_text
            else:
                blog = generate_with_retry(prompt, model_choice)
                st.write(blog)

            if enhance:
                blog = improve_seo(blog, model_choice)
                st.subheader("✨ SEO Enhanced")
                st.write(blog)

            st.session_state.history.append(blog)

            # Download TXT
            st.download_button(
                "📥 Download TXT",
                blog,
                file_name="blog.txt"
            )

            # Download PDF
            pdf_file = create_pdf(blog)
            with open(pdf_file, "rb") as f:
                st.download_button("📄 Download PDF", f, file_name="blog.pdf")

        except Exception as e:
            st.error("Error generating blog")
            if settings.env == "development":
                st.exception(e)

# History
with st.expander("📜 History"):
    for i, item in enumerate(st.session_state.history[::-1]):
        st.markdown(f"### Blog {i+1}")
        st.write(item[:300] + "...")