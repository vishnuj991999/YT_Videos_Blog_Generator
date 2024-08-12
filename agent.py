from tasks import transcribe_audio, generate_content
from tools import download_youtube_audio, save_text_as_pdf

def process_youtube_video(video_url, work_type, api_key):
    """Process YouTube video to generate summary or blog."""
    success, message = download_youtube_audio(video_url)
    if not success:
        return False, message
    
    text_generated = transcribe_audio("audio.mp3")

    # Token limit handling
    max_tokens = 1500
    max_input_length = 4097 - max_tokens
    if len(text_generated) > max_input_length:
        text_generated = text_generated[:max_input_length]

    text_1 = generate_content(text_generated, work_type, api_key)

    # Filename for the PDF
    filename = "BSG.pdf"
    pdf_file = save_text_as_pdf(text_1, filename)

    return True, pdf_file
