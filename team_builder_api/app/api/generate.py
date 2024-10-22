import os
from fastapi import APIRouter
import json
import boto3
from botocore.config import Config
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv(override=True)

router = APIRouter()
class PromptInput(BaseModel):
    prompt: str

@router.post("/generate")
async def get_zero_shot(body: PromptInput):
    try:
        config = Config(
            region_name = os.getenv("AWS_REGION"),
               retries = {
                    'mode': 'adaptive',
                }
        )
        # agent_client = boto3.client('bedrock-agent-runtime', region_name = os.getenv("AWS_REGION"))
        bedrock_client = boto3.client("bedrock-runtime", config=config)
        # response = bedrock_client.invoke_model(
        #     body = json.dumps({
        #         "prompt": body.prompt,
        #         "max_tokens_to_sample": 300,
        #         "temperature": 0.5,
        #         "top_k": 250,
        #         "top_p": 1,
        #         "stop_sequences": ["\n\nHuman:"],
        #         "anthropic_version": "bedrock-2023-05-31"
        #         }), 
        #     modelId = "anthropic.claude-3-sonnet-20240229-v1:0", 
        #     accept="application/json", 
        #     contentType="application/json"
        # )

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
        # response_text = model_response["completion"]
        response_text = model_response["results"][0]['outputText']
        return {"ok": True, "body": response_text, "error": None}

    except Exception as e:
        return {"ok": False, "body": None, "error": repr(e)}