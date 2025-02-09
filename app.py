import streamlit as st
from google.cloud import speech

# Function to transcribe audio using Google Cloud Speech-to-Text
def transcribe_audio(audio_content, config):
    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(content=audio_content)
    operation = client.long_running_recognize(config=config, audio=audio)
    st.write("Waiting for operation to complete...")
    response = operation.result(timeout=90)
    return response

# Streamlit app
def main():
    st.title("Google Cloud Speech-to-Text Transcription")
    st.write(
        "Upload an audio file to transcribe it using Google Cloud's Speech-to-Text API."
    )
    
    # Upload audio file
    uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac"])
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")
        audio_content = uploaded_file.read()
        
        # Configure the transcription
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=24000,
            language_code="en-US",
            model="default",
            audio_channel_count=1,
            enable_word_confidence=True,
            enable_word_time_offsets=True,
        )
        
        # Call the transcription function
        with st.spinner("Transcribing audio..."):
            response = transcribe_audio(audio_content, config)
        
        # Display the transcription results
        st.write("### Transcription Results")
        for result in response.results:
            st.write("**Transcript:**", result.alternatives[0].transcript)
            st.write("**Confidence:**", result.alternatives[0].confidence)
            st.write("---")
    else:
        st.write("Please upload an audio file to start the transcription.")

if __name__ == "__main__":
    main()
