from openai import OpenAI

client = OpenAI(api_key="my api key")

MODEL = "gpt-5-nano"

SYSTEM_PROMPT = "You are a helpful assistant. Reply short and simple."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


def chat(user_input):
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_completion_tokens=200
    )

    reply = response.choices[0].message.content

    if not reply:
        reply = "I couldn't generate a response."

    messages.append({"role": "assistant", "content": reply})

    return reply


while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    reply = chat(user_input)

    print("Assistant:", reply)