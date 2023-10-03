import openai
from fastapi import APIRouter
from pydantic import BaseModel

from app.core.config import OPENAI_API_KEY

class PromptRequest(BaseModel):
    prompt: str

router = APIRouter()

openai.api_key = OPENAI_API_KEY

@router.post("/completion")
def get_completion(request: PromptRequest):
    return openai.Completion.create(
        engine="davinci", prompt=request.prompt, max_tokens=5
    )


@router.post("/image")
def create_image(request: PromptRequest):
    response = openai.Image.create(prompt=request.prompt, n=1, size="1024x1024")
    return response["data"][0]["url"]
