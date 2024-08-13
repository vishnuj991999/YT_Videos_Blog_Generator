import streamlit as st
from agent import process_youtube_video

# Streamlit interface
st.title("YouTube Audio Summarizer/Blog Generator")

video_url = st.text_input("Enter YouTube Video Link:")
work = st.radio("Choose Work Type:", ["Summarize", "Blog"])

if st.button("Generate"):
    if video_url:
        api_key = "YOUR_API_KEY"
        success, result = process_youtube_video(video_url, work, api_key)
        if success:
            # Provide a download link for the PDF
            with open(result, "rb") as f:
                st.download_button("Download PDF", f, file_name="BSG.pdf")
        else:
            st.error(result)
    else:
        st.error("Please enter a valid YouTube video URL.")
