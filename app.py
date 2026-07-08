from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/")
async def root():
    with open("/volume1/web/index.html") as f:
        return HTMLResponse(content=f.read())

@app.get("/{path:path}")
async def static(path: str):
    filepath = os.path.join("/volume1/web", path)
    if os.path.isfile(filepath):
        with open(filepath, "rb") as f:
            content = f.read()
        ext = os.path.splitext(path)[1]
        mime = {"css":"text/css","js":"application/javascript","png":"image/png","jpg":"image/jpeg","svg":"image/svg+xml","ico":"image/x-icon","html":"text/html","json":"application/json"}.get(ext, "application/octet-stream")
        return Response(content=content, media_type=mime)
    return HTMLResponse(content="<h1>Not Found</h1>", status_code=404)

@app.get("/health")
async def health():
    return {"status": "ok"}

