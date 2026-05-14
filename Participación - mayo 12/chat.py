from openai import OpenAI
import os
from dotenv import load_dotenv

SYSTEM_MESSAGE = "You are a friendly and concise chatbot."

if __name__ == "__main__":
    load_dotenv()
    
    client = OpenAI(
        base_url=os.environ.get('OPENAI_BASE_URL'),
        api_key=os.environ.get('OPENAI_KEY'),
    )

    history = [{"role": "system", "content": SYSTEM_MESSAGE}]
    
    print(f"--- Chat Iniciado (Modelo: {os.environ.get('MODEL')}) ---\n")

    while True:
        user_input = input("> ")
        if user_input.lower() in ["exit", "salir"]: break

        history.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=os.environ.get('MODEL'),
            messages=history,
        )

        reply = response.choices[0].message.content
        print(f"\n{reply}\n")

        history.append({"role": "assistant", "content": reply})