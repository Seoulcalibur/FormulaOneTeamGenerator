import openai
import os
import json

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

def save_responses(new_teamname, filename="F1TeamNames.json"):
     try:
        # Read existing data from the file
        with open(filename, "r") as file:
            teamnames = json.load(file)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        teamnames = []
    # Append the new response
    teamnames.append(new_response)
    # Write the updated list back to the file
    with open(filename, "w") as file:
        json.dump(teamnames, file)

prompt = "Create a unique and catchy Formula 1 team name combining a well-known automotive car brand (full name) with a globally recognized non-automotive brand. The team name should end with 'F1 Team'."
teamname = create_team(prompt)
teamname = [teamname]
save_responses(teamname)

print(teamname)
