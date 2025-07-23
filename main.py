import cohere
import os


os.environ['COHERE_API_KEY'] = 's7qgwB0QeSCV0p1xjhDkOiDhwYQ9Sp1ejLQ9mjX7'


co = cohere.Client(os.getenv("COHERE_API_KEY"))

def generate_email(recipient, topic, purpose, tone, additional_notes=""):
    prompt = f"""
    Write a {tone.lower()} email to {recipient} about "{topic}".
    The purpose of the email is: {purpose.lower()}.
    Include this context: {additional_notes}
    Sign off with a polite closing.
    """

    response = co.generate(
        model="command",
        prompt=prompt,
        max_tokens=300,
        temperature=0.7
    )
    return response.generations[0].text.strip()

if __name__ == "__main__":
    print("\n📧 Automatic Email Generator (Cohere CLI Version)")
    recipient = input("To (Name or Email): ")
    topic = input("Email Topic: ")
    purpose = input("Purpose (e.g., Information, Request, Follow-up, etc.): ")
    tone = input("Tone (Formal, Semi-formal, Casual): ")
    additional_notes = input("Additional Info (Optional): ")

    print("\nGenerating email ... Please wait...\n")
    email_output = generate_email(recipient, topic, purpose, tone, additional_notes)
    print("📬 Generated Email:\n")
    print(email_output)


    with open("generated_email.txt", "w", encoding="utf-8") as f:
        f.write(email_output)
    print("\n✅ Email saved as 'generated_email.txt'")
