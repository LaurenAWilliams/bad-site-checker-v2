from fastapi import FastAPI, Request
from mangum import Mangum
import structlog

LOGGER = structlog.get_logger()

app = FastAPI()

@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/v2/urlinfo/{url_path:path}")
async def check_url(url_path, request: Request):
    # reconstruct url with query params
    if request.query_params:
        path = f"{url_path}?{request.query_params}"

    LOGGER.info("urlinfo request received", url=path)

    return {"msg": path}

handler = Mangum(app)
