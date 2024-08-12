import os
from pydub import AudioSegment
import yt_dlp
from fpdf import FPDF

def download_youtube_audio(video_url, audio_file='audio.wav'):
    """Download audio from YouTube and convert to WAV format."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.webm',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Convert to WAV if needed
    mp3_file = 'audio.mp3'
    if os.path.exists(mp3_file):
        try:
            audio = AudioSegment.from_file(mp3_file, format='mp3')
            audio.export(audio_file, format='wav')
            return True, "Video fetched successfully"
        except Exception as e:
            return False, f"Error converting file: {e}"
    else:
        return False, "Error: The downloaded audio file does not exist."

def save_text_as_pdf(text, filename):
    """Save text to a PDF file using a Unicode font."""
    pdf = FPDF()
    pdf.add_page()
    
    # Set font to a Unicode TrueType font
    pdf.set_font("Arial", size=12)
    
    # Add text to PDF
    pdf.multi_cell(0, 10, text)
    
    # Save the PDF to a file
    pdf.output(filename)
    return filename
