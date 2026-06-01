from groq import Groq
import base64
import os
from dotenv import load_dotenv

# Charge .env en local uniquement
load_dotenv()


def encode_image(image_bytes):
    return base64.b64encode(image_bytes).decode("utf-8")


def ask_model_on_image(question, image_bytes):
    base64_image = encode_image(image_bytes)

    api_key = os.getenv("GROQ_KEY")

    if not api_key:
        raise ValueError("GROQ_KEY is missing")

    client = Groq(api_key=api_key)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )

    return chat_completion.choices[0].message.content