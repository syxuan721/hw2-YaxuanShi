import json
import os
import sys
from pathlib import Path

from google import genai
from dotenv import load_dotenv
load_dotenv()


SYSTEM_PROMPT = """
You are a business writing assistant.

Your task is to draft a professional follow-up email after a meeting.

Requirements:
- Write in a polite, professional, and concise business tone.
- Thank the recipient for their time.
- Briefly summarize the meeting topic and key points.
- Clearly mention next steps if they are available in the notes.
- Do not invent facts, deadlines, or decisions that are not supported by the input.
- If the notes are incomplete or unclear, stay general and cautious.
- Output only the email text.
""".strip()


def load_eval_case(json_path: str, case_id: int) -> dict:
    path = Path(json_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {json_path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for case in data:
        if case.get("id") == case_id:
            return case["input"]

    raise ValueError(f"Case id {case_id} not found in {json_path}")


def build_user_prompt(data: dict) -> str:
    recipient_name = data.get("recipient_name", "there")
    meeting_topic = data.get("meeting_topic", "our recent meeting")
    notes = data.get("notes", [])

    notes_text = "\n".join(f"- {note}" for note in notes) if notes else "- No detailed notes were provided."

    prompt = f"""
Draft a follow-up email based on the information below.

Recipient name: {recipient_name}
Meeting topic: {meeting_topic}
Meeting notes:
{notes_text}

Write a professional follow-up email.
""".strip()

    return prompt


def generate_email(data: dict, model_name: str = "gemini-3-flash-preview") -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GEMINI_API_KEY is not set. Please add it to your .env file or set it in your terminal."
        )

    client = genai.Client(api_key=api_key)

    user_prompt = build_user_prompt(data)
    full_prompt = f"{SYSTEM_PROMPT}\n\n{user_prompt}"

    response = client.models.generate_content(
        model=model_name,
        contents=full_prompt,
    )

    if not getattr(response, "text", None):
        raise ValueError("Model returned an empty response.")

    return response.text.strip()


def save_output(output_text: str, output_path: str = "results.txt") -> None:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output_text)


def main():
    """
    Usage:
        python app.py 1
        python app.py 2
    """
    if len(sys.argv) < 2:
        print("Usage: python app.py <case_id>")
        sys.exit(1)

    case_id = int(sys.argv[1])

    try:
        data = load_eval_case("eval_set.json", case_id)
        email_text = generate_email(data)

        print("\n=== GENERATED FOLLOW-UP EMAIL ===\n")
        print(email_text)

        save_output(email_text, "results.txt")
        print("\nSaved output to results.txt")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
