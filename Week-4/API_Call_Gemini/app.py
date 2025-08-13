import os
from google import genai
from dotenv import load_dotenv
load_dotenv()
# Initialize the client using the API key from the environment variable
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Generate content using the specified model
response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="Explain how AI works in a few words"
)

# Print the generated response
print(response.text)
