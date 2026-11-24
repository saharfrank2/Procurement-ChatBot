import os
from pathlib import Path
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
policy_text = Path("data/policy.txt").read_text(encoding="utf-8")

system_prompt = f"""
את עוזרת דיגיטלית למחלקת רכש.
עני בעברית ברורה, קצרה ומסודרת על בסיס הנהלים הבאים:
{policy_text}

אם חסרים פרטים (כמו סכום, קטגוריה או מספר הזמנה), שאלי שאלה ממוקדת.
אם המידע לא מופיע בנהלים, צייני זאת במפורש ואל תמציאי חוקים.
"""

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

print("בוט מחלקת רכש מוכן! הקלידו 'יציאה' לסיום.\n")

while True:
    user_input = input("את: ").strip()
    if not user_input:
        continue
    if user_input.lower() in {"יציאה", "exit", "quit"}:
        print("להתראות!")
        break

    response = chat.send_message(user_input)
    print(f"\nבוט: {response.text}\n")
