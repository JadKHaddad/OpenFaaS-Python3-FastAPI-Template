from fastapi.responses import PlainTextResponse # , JSONResponse, Response

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    return PlainTextResponse(content=req, status_code=200)