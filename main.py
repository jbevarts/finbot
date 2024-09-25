import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()

# Load environment variables from the .env file
load_dotenv()

# Retrieve the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

# Example usage
if api_key:
    print("API key loaded successfully.")
else:
    print("API key not found.")

client = OpenAI(api_key=api_key)


class Message(BaseModel):
    content: str


@app.post("/chat")
async def chat(message: Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o", messages=[{"role": "user", "content": message.content}], max_tokens=150
        )
        return {"response": response.choices[0].message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Example curl command to hit the service
# curl -X POST "http://0.0.0.0:8000/chat"
# -H "Content-Type: application/json"
# -d '{"content": "Should i purchase a call on NVDA with expiration 9/27 at a 1.96 premium"}'
