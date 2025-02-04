import streamlit as st
import whisper
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os



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
    llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=os.getenv("GOOGLE_API_KEY"))
    return llm

# Summarize text using Gemini
def summarize_text(text, llm):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following podcast transcript in 3-5 bullet points\n\n{text}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run(text)
    return summary

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

            # Display results
            st.subheader("Transcription:")
            st.write(transcription)

            # Display summary in the left panel
            st.sidebar.subheader("Summary:")
            st.sidebar.write(summary)

            # Clean up temporary file
            os.remove("temp_audio.mp3")

if __name__ == "__main__":
    main()