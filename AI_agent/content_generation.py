import openai

def generate_post(topic: str, platform: str) -> str:
    prompt = f"Create a {platform}-friendly post about {topic}. Max 280 chars for Twitter."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content