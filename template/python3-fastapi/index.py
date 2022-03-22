# inspired by python3-flask-debian template
import os
from fastapi import FastAPI, Request
from function import handler

app = FastAPI()

# distutils.util.strtobool() can throw an exception
def is_true(val):
    return len(val) > 0 and val.lower() == "true" or val == "1"

@app.get('/')
@app.post('/')
async def index(request: Request):
    raw_body = os.getenv("RAW_BODY", "false")
    as_text = True
    if is_true(raw_body):
        as_text = False
    body = await request.body()
    if as_text:
        body = body.decode("utf-8") 
    ret = handler.handle(body)
    return ret