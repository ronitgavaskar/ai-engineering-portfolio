from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv()

openai_client = OpenAI()
claude_client = Anthropic()

def openai_call():
    response = openai_client.responses.create(
        model="gpt-5-nano",
        input="Say hello world in 3 languages: Hindi, English, Spanish"
    )
    print(response.output_text)

def claude_call():
    response = claude_client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=256,
        messages=[
            {
                "role": "user",
                "content": "Say hello world in 3 languages: Hindi, English, Spanish"
            }
        ],
    )
    print(response.content[0].text)

if __name__ == "__main__":
    openai_call()
    print("====================")
    claude_call()
