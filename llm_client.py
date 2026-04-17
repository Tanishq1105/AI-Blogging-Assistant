from google import genai
from config import settings
import time

client = genai.Client(api_key=settings.api_key)

def generate_with_retry(prompt: str, model: str):
    last_error = None

    for attempt in range(settings.max_retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text

        except Exception as e:
            last_error = e
            time.sleep(1 + attempt)

    raise RuntimeError(f"Failed after retries: {last_error}")


def stream_generate(prompt: str, model: str):
    response = client.models.generate_content_stream(
        model=model,
        contents=prompt
    )

    for chunk in response:
        if chunk.text:
            yield chunk.text