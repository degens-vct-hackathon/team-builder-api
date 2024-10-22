from fastapi import APIRouter
import json
import boto3
import os
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv(override=True)

router = APIRouter()
class PromptInput(BaseModel):
    prompt: str

@router.post("/generate")
async def get_zero_shot(body: PromptInput):
    try:
        bedrock_client = boto3.client("bedrock-runtime", region_name = os.getenv("AWS_REGION"))
        response = bedrock_client.invoke_model(
            body = json.dumps({
                "inputText": body.prompt,
                "textGenerationConfig" : {
                    "maxTokenCount": 512,
                    "temperature": 0.5,
                }
            }),
            modelId = "amazon.titan-text-premier-v1:0",
            accept="application/json",
            contentType="application/json"
        )

        model_response = json.loads(response["body"].read())
        response_text = model_response["results"][0]['outputText']
        return {"ok": True, "body": response_text, "error": None}

    except Exception as e:
        return {"ok": False, "body": None, "error": repr(e)}
