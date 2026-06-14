import ollama
import streamlit as st

st.set_page_config(
    page_title="AI Career Mentor",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Mentor & Study Coach")

question = st.text_area(
    "Ask about studies, careers, coding, productivity, AI, or self-improvement:"
)

def ai_mentor(question):

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": """
                You are an expert AI Career Mentor and Study Coach.

                Responsibilities:
                - Help students with studies and career planning.
                - Explain concepts in simple language.
                - Suggest learning roadmaps.
                - Help with coding projects.
                - Improve productivity and time management.
                - Motivate users when needed.

                Rules:
                - Be professional and friendly.
                - Use bullet points whenever possible.
                - Give practical advice.
                - Keep answers concise but useful.
                - If asked for a roadmap, provide step-by-step guidance.
                - End each answer with one actionable next step.
                """
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]

if st.button("Get Advice"):
    with st.spinner("Thinking..."):
        answer = ai_mentor(question)

    st.success("Response Generated")
    st.write(answer)
