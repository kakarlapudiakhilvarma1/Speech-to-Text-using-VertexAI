# Speech-to-Text Transcription using Google Cloud Speech-to-Text API

This project is a simple Streamlit-based web application that transcribes audio files using Google Cloud's Speech-to-Text API.

## Features
- Transcribe audio files into text.
- Uses Google Cloud's advanced speech recognition models.
- Supports various audio formats like WAV, MP3, and FLAC.
- Displays confidence levels and word timestamps.
- Interactive Streamlit UI for ease of use.

## Installation and Setup

### Prerequisites
- Python 3.8+
- Google Cloud account with Speech-to-Text API enabled
- Streamlit installed
- Google Cloud SDK installed and authenticated

### Set Up Google Cloud Authentication

Follow this link to setup local authorization to use Google Vertex AI Services: https://cloud.google.com/sdk/docs/initializing

### Installing Dependencies
1. Clone the repository:
   ```sh
   git clone https://github.com/kakarlapudiakhilvarma1/Speech-to-Text-using-VertexAI.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Speech-to-Text-using-VertexAI
   ```
3. Create a virtual environment and activate it:
   ```sh
   conda create -p myenv python==3.10 -y
   conda activate myenv/   # On Windows 
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running the Application
1. Ensure you have set up authentication (as described above).
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```

## Output Screenshots

![image](https://github.com/user-attachments/assets/9843c4a7-a673-4c5b-b099-81c656d9239b)

---
Generated Text
![image](https://github.com/user-attachments/assets/6cc16baa-9e77-4cd6-a06d-332080e44225)


## Notes
- Make sure your Google Cloud project has billing enabled to use the Speech-to-Text API.
- You can customize the transcription model and parameters in the script.


## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to improve the project.

