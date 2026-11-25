
import os
from dotenv import load_dotenv
from groq import Groq


# ----------------------------------
# 1. LOAD GROQ API KEY
# ----------------------------------

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)


# ----------------------------------
# 2. TEMPERATURE SETTINGS
# ----------------------------------

GENRE_TEMPERATURE = {
    "Thriller": 0.7,
    "Comedy": 1.0,
    "Fiction": 0.9
}


# ----------------------------------
# 3. STORY LENGTH SETTINGS
# ----------------------------------

STORY_LENGTH = {
    "Brief": "Write approximately 300-400 words.",
    "Medium": "Write approximately 600-800 words.",
    "Full Length": "Write approximately 1200-1500 words."
}


# ----------------------------------
# 4. CREATE PROMPT
# ----------------------------------

def create_prompt(topic, genre, length):

    prompt = f"""
    You are a professional creative story writer.

    Write an engaging and original story using
    the following details:

    Story Topic: {topic}

    Genre: {genre}

    Story Length: {STORY_LENGTH[length]}

    Instructions:

    1. Create an interesting title.
    2. Develop an engaging storyline.
    3. Include interesting characters.
    4. Maintain the selected genre throughout.
    5. Make the story creative and original.
    6. Give the story a satisfying ending.
    7. Use simple and understandable language.

    Generate only the story with its title.
    """

    return prompt


# ----------------------------------
# 5. GENERATE STORY USING GROQ
# ----------------------------------

def generate_story(topic, genre, length):

    if not GROQ_API_KEY:
        raise ValueError("Groq API key not found. Check your .env file.")

    # Create prompt
    prompt = create_prompt(topic, genre, length)

    # Select temperature based on genre
    temperature = GENRE_TEMPERATURE[genre]

    # Send request to Groq
    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=temperature,

        max_completion_tokens=3500
    )

    # Extract generated story
    story = response.choices[0].message.content

    return story
