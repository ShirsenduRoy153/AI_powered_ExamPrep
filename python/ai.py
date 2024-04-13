# Import libraries
import google.generativeai as genai
import sys



# Replace with your API key
API_KEY = "AIzaSyALXDhISha_-NhVRNY0ziI0JuhiYXNpXa0"

# Configure API key
genai.configure(api_key=API_KEY)

# Choose the Gemini model (change "gemini-1.0-pro" for other models)
model_name = "gemini-1.0-pro"

# Start a chat session
chat = genai.GenerativeModel(model_name=model_name).start_chat()

# Main loop for conversation
  # Get user input
user_input = sys.argv[1]
response = chat.send_message(user_input)
print(f"BOT: {response.text}")