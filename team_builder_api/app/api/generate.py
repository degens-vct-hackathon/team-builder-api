from fastapi import APIRouter
import json
import boto3
import os
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()
class PromptInput(BaseModel):
    prompt: str

@router.post("/generate/")
async def get_zero_shot(body: PromptInput):
    try:
        boto3_bedrock = boto3.client("bedrock-runtime", region_name = os.getenv("AWS_REGION"))
        response = boto3_bedrock.invoke_model(
            body = json.dumps({
                "inputText": body.prompt,
                "textGenerationConfig": {"topP": 0.95, "temperature": 0.1},
            }), 
            modelId = "amazon.titan-tg1-large", 
            accept="application/json", 
            contentType="application/json"
        )

        response_body = json.loads(response.get("body").read())
        outputText = response_body.get("results")[0].get("outputText") or "\n"
        res = outputText[outputText.index("\n") + 1 :]
        return {"ok": True, "body": res, "error": None}

    except Exception as e:
        return {"ok": False, "body": None, "error": repr(e)}
