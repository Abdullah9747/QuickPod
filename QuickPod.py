import streamlit as st
import whisper
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from zyphra import ZyphraClient
import io

st.set_page_config(
    page_title="QuickPod",
    page_icon="quickpodlogo.webp",
)

# Set up Whisper model
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("small")

# Set up Gemini API (via LangChain)
def setup_gemini():
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=os.getenv("GOOGLE_API_KEY"))
    return llm

def setup_zyphra():
    client = ZyphraClient(api_key=os.getenv("ZYPHRA_API_KEY"))
    return client

# Summarize text using Gemini
def summarize_text(text, llm):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following podcast transcript in 3-5 bullet points\n\n{text}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run(text)
    return summary

# Initialize session state variables if not present
if "summary" not in st.session_state:
    st.session_state.summary = None  # Stores the summary

# Main function
def main():
    load_dotenv()
    st.title("Podcast Summarizer 🎙")
    st.write("Upload a podcast audio or video file to get a summary.")

    # File uploader
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        st.audio(uploaded_file)

        if st.button("Summarize"):
            with st.spinner("Transcribing audio..."):
                # Save the uploaded file temporarily
                with open("temp_audio.mp3", "wb") as f:
                    f.write(uploaded_file.getbuffer())

                # Transcribe using Whisper
                model = load_whisper_model()
                result = model.transcribe("temp_audio.mp3")
                transcription = result["text"]
                st.success("Transcription complete!")

            with st.spinner("Generating summary..."):
                # Summarize using Gemini
                llm = setup_gemini()
                summary = summarize_text(transcription, llm)
                st.success("Summary generated!")

                # Store summary in session state
                st.session_state.summary = summary

            # Clean up temporary file
            os.remove("temp_audio.mp3")

    # Display the summary if it exists
    if st.session_state.summary:
        st.subheader("Generated Summary:")
        st.write(st.session_state.summary)

        # Speak Button
        if st.button("🔊 Speak"):
            with st.spinner("Generating speech..."):
                client = setup_zyphra()
                if client:
                    audio_data = client.audio.speech.create(
                        text=st.session_state.summary,
                        speaking_rate=15,
                        model="zonos-v0.1-transformer"
                    )
                    audio_bytes = io.BytesIO(audio_data)
                    st.audio(audio_bytes, format="audio/mp3")
                else:
                    st.error("Failed to initialize Zyphra client.")

if __name__ == "__main__":
    main()
