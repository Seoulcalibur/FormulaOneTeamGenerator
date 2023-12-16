import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt):
    try:
        response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

prompt = "Create a unique and catchy Formula 1 team name combining a well-known automotive car brand (full name) with a globally recognized non-automotive brand. The team name should end with 'F1 Team'."
response = get_completion(prompt)

print(response)
