# Podcast Summarizer 🎙

**Podcast Summarizer** is a Streamlit-based web application that allows users to upload podcast audio or video file and get a summarized version of the content. The app uses OpenAI's Whisper model for transcription and Google's Gemini API (via LangChain) for generating concise summaries in Roman English. The summary is displayed in a clean and user-friendly interface, with the transcription and summary neatly organized for easy reading.

---

## Features ✨

- **Audio Transcription**: Automatically transcribes podcast audio files using OpenAI's Whisper model.
- **AI-Powered Summarization**: Generates concise summaries of the podcast content using Google's Gemini API.
- **User-Friendly Interface**: Built with Streamlit, the app provides an intuitive and responsive interface.
- **Sidebar Summary**: Displays the summary in a left-hand sidebar for quick reference.
- **Supports Multiple Formats**: Accepts MP3 and WAV audio files for transcription.

---

## How It Works 🛠️

1. **Upload Audio**: Users upload a podcast audio or video file through the Streamlit interface.
2. **Transcription**: The app uses OpenAI's Whisper model to transcribe the audio into text.
3. **Summarization**: The transcribed text is passed to Google's Gemini API, which generates a summary in 3-5 bullet points.
4. **Display Results**: The full transcription is displayed in the main area, while the summary is shown in the left sidebar.

---

## Technologies Used 💻

- **Streamlit**: For building the web application interface.
- **OpenAI Whisper**: For audio transcription.
- **Google Gemini API**: For generating summaries via LangChain.
- **LangChain**: For integrating Gemini API and managing the summarization prompt.
- **Python**: The core programming language used for the project.

---

## Setup Instructions 🚀

### Prerequisites

- Python 3.8 or higher
- A Google API key for Gemini (set up via [Google Cloud Console](https://console.cloud.google.com/))
- OpenAI Whisper dependencies (FFmpeg)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/podcast-summarizer.git
   cd podcast-summarizer

   ```

2. Install the required dependencies:

pip install -r requirements.txt

3. Set up your environment variables:

Create a .env file in the root directory.

Add your Google API key:

GOOGLE_API_KEY=your_api_key_here

4. Run the Streamlit app:
   streamlit run app.py
   Open your browser and navigate to http://localhost:8501 to use the app.

## Usage 📝

1. **Upload a podcast audio or video file** using the file uploader.
2. **Click the "Summarize" button** to transcribe and summarize the content.
3. **View the transcription** in the main area and the **summary** in the left sidebar.
