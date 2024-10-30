from fastapi import FastAPI
from fastapi.responses import JSONResponse, HTMLResponse

app = FastAPI()

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "Hello World"

# JSON endpoint
@app.get("/json", response_class=JSONResponse)
async def get_json():
    return {"message": "Hello, this is a JSON response"}

# HTML endpoint
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    items = ["item1", "item2", "item3"]
    html_content = "<ul>"
    for item in items:
        html_content += f"<li>{item}</li>"
    html_content += "</ul>"
    return html_content
