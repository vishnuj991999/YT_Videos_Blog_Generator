**YouTube Video Blog Generator**

**Overview**

The YouTube Video Blog Generator is a tool that converts YouTube videos into detailed blog posts. It extracts audio from the video, transcribes it using Whisper, and generates a blog or summary using the Meta Llama 3.1 405B AI model. The final output is saved as a PDF for easy sharing and distribution.

**Features**

Audio Extraction: Download and convert YouTube video audio into WAV format.
Transcription: Convert audio to text using the Whisper model.
Content Generation: Generate summaries or blog posts using Meta Llama 3.1 405B AI.
PDF Generation: Save the generated content as a downloadable PDF.

**Requirements**

Python 3.7 or higher
Streamlit
Pydub
yt-dlp
Whisper
Together API
FPDF


Replace YOUR_API_KEY with your actual API key in agent.py or directly in main.py.

**Usage**

**Run the Streamlit App:**

streamlit run main.py

**Interact with the App:**

Enter YouTube Video URL: Provide the link to the YouTube video you want to convert.
Choose Work Type: Select between "Summarize" or "Blog".
Generate: Click the "Generate" button to process the video.
Download PDF: Once processing is complete, download the generated blog or summary as a PDF.
Files
tools.py: Contains utility functions for downloading audio and saving text as PDF.
tasks.py: Includes functions for transcribing audio and generating content.
agent.py: Integrates functions from tools.py and tasks.py to handle the processing logic.
main.py: Sets up the Streamlit interface and connects with agent.py.
Contributing
Feel free to submit issues, fork the repository, and create pull requests to contribute to the project. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or support, please contact vishnuj1999@outlook.com.




![Image](https://github.com/user-attachments/assets/a1c5b7d8-113e-4418-be67-a5b53ba0a85b)


![Image](https://github.com/user-attachments/assets/aeef4ddc-c691-41f6-9c13-67f3ab147bbf)



![Image](https://github.com/user-attachments/assets/f32ad534-5b54-48b7-aa0f-2abd7e42a59b)




![Image](https://github.com/user-attachments/assets/37b57717-d63a-455a-abca-9152616b788e)




