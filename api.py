import json
import torch
import uvicorn
from fastapi import FastAPI, Request
from transformers import AutoTokenizer, AutoModel

DEVICE = "cuda"
DEVICE_ID = "0"
CUDA_DEVICE = f"{DEVICE}:{DEVICE_ID}" if DEVICE_ID else DEVICE


def torch_gc():
    if torch.cuda.is_available():
        with torch.cuda.device(CUDA_DEVICE):
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()


app = FastAPI()


@app.post("/checkParams")
async def chat(request: Request):
    json_post_raw = await request.json()
    json_post = json.dumps(json_post_raw)
    params = json.loads(json_post)
    response = {}
    success = True
    message = ""
    max_length = params.get('max_length')
    if max_length is not None and (max_length > 2048 or max_length < 200):
        success = False
        message += "max_length must be between 200 and 2048"
        message += "\n"
    top_p = params.get('top_p')
    if top_p is not None and (top_p > 1 or top_p < 0):
        success = False
        message += "top_p must be between 0 and 1"
        message += "\n"
    temperature = params.get('temperature')
    if temperature is not None and (temperature > 2 or temperature < 0):
        success = False
        message += "temperature must be between 0 and 2"
        message += "\n"
    response["success"] = success
    response["message"] = message
    return response


@app.post("/chat")
async def chat(request: Request):
    global model, tokenizer
    json_post_raw = await request.json()
    json_post = json.dumps(json_post_raw)
    json_post_list = json.loads(json_post)
    prompt = json_post_list.get('input')
    chat_context_list = json_post_list.get('chatContextList')
    history = []
    if chat_context_list is not None:
        for chat_context in chat_context_list:
            dialogue = []
            dialogue.append(chat_context['user'])
            dialogue.append(chat_context['assistant'])
            history.append(dialogue)
    params = json_post_list.get('params')
    max_length = 2048
    top_p = 0.7
    temperature = 0.95
    if params is not None:
        max_length = params.get('max_length')
        top_p = params.get('top_p')
        temperature = params.get('temperature')

    response, history = model.chat(tokenizer,
                                   prompt,
                                   history=history,
                                   max_length=max_length if max_length else 2048,
                                   top_p=top_p if top_p else 0.7,
                                   temperature=temperature if temperature else 0.95)
    torch_gc()
    return response


if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained("model", trust_remote_code=True)
    model = AutoModel.from_pretrained("model", trust_remote_code=True).half().cuda()
    # model = AutoModel.from_pretrained("model", trust_remote_code=True).float()
    model.eval()
    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1)
