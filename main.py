import streamlit as st
from agent import process_youtube_video

# Streamlit interface
st.title("YouTube Audio Summarizer/Blog Generator")

video_url = st.text_input("Enter YouTube Video Link:")
work = st.radio("Choose Work Type:", ["Summarize", "Blog"])

if st.button("Generate"):
    if video_url:
        api_key = "64880c44ef37384040dc253c954ed2f190c0e4702c3e80745e5eb78221f47376"
        success, result = process_youtube_video(video_url, work, api_key)
        if success:
            # Provide a download link for the PDF
            with open(result, "rb") as f:
                st.download_button("Download PDF", f, file_name="BSG.pdf")
        else:
            st.error(result)
    else:
        st.error("Please enter a valid YouTube video URL.")
