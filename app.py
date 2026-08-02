from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from server import build_chat_response

app = FastAPI(title="UX Bot Demo")

BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "docs" / "static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return FileResponse(BASE_DIR / "docs" / "index.html")


@app.post("/chat")
async def chat(request: Request):
    form = await request.json()
    message = (form.get("message") or "").strip()
    session_id = str(form.get("session_id") or "default")
    if not message:
        return {
            "reply": "Please enter a student-loan question such as eligibility, documents, or application steps.",
            "suggestions": ["How much can I borrow for a student loan?", "What documents do I need to apply?", "How do I apply for a student loan?"],
        }
    return build_chat_response(message, session_id)
