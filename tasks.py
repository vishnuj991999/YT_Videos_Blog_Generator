import whisper
from together import Together

def transcribe_audio(audio_file):
    """Transcribe audio file using Whisper model."""
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]

def generate_content(text_generated, work_type, api_key):
    """Generate summary or blog using Together API."""
    system_content = ""
    role_content = ""
    word_count = 0

    if work_type == "Summarize":
        system_content = "You are a helpful assistant. You need to summarize the content given in bullet points only."
        role_content = "summarize this content bullet points only."
        word_count = 300
    elif work_type == "Blog":
        system_content = "You are a helpful assistant. You need to write a blog with the given content."
        role_content = "\n generate blog with this content more than 1200 words"
        word_count = 1500

    together_client = Together(api_key=api_key)

    response = together_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        messages=[
            {
                "role": "system",
                "content": system_content
            },
            {
                "role": "user",
                "content": f"{text_generated} {role_content}"
            }
        ],
        max_tokens=word_count,
        temperature=0.11,
        top_p=1,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>"]
    )

    return response.choices[0].message.content
