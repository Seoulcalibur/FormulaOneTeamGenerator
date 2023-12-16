import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def create_team(prompt):
    try:
        response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def save_responses(response, filename="F1TeamNames.json"):
    with open(filename, "w") as file:
        json.dump(responses, file)

prompt = "Create a unique and catchy Formula 1 team name combining a well-known automotive car brand (full name) with a globally recognized non-automotive brand. The team name should end with 'F1 Team'."
response = create_team(prompt)
response = [response]
save_responses(response)

print(response)
