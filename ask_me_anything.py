import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Store conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful and friendly AI assistant."}
]

print("🤖 Ask Me Anything Chatbot (type 'quit' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        print("Bot: Goodbye! 👋")
        break

    conversation_history.append({"role": "user", "content": user_input})

    try:
        # Get response from OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=conversation_history
        )

        bot_reply = response.choices[0].message.content
        print("Bot:", bot_reply)

        # Save reply to history
        conversation_history.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        print("⚠️ Error:", e)
        break
