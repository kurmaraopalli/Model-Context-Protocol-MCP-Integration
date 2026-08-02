from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from server import (
    build_chat_response,
    get_mcp_prompt_definitions,
    get_mcp_resource_definitions,
    get_mcp_tool_definitions,
    invoke_mcp_tool,
    read_mcp_resource,
    render_mcp_prompt,
)

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


@app.get("/mcp/tools")
async def list_mcp_tools():
    return {"tools": get_mcp_tool_definitions()}


@app.post("/mcp/tools/call")
async def call_mcp_tool(request: Request):
    payload = await request.json()
    tool_name = payload.get("name")
    arguments = payload.get("arguments") or {}
    if not tool_name:
        return {"error": "Missing tool name"}
    try:
        result = invoke_mcp_tool(tool_name, arguments)
        return {"result": result}
    except ValueError as exc:
        return {"error": str(exc)}


@app.get("/mcp/resources")
async def list_mcp_resources():
    return {"resources": get_mcp_resource_definitions()}


@app.get("/mcp/resources/{resource_name}")
async def get_mcp_resource(resource_name: str):
    try:
        return read_mcp_resource(resource_name)
    except ValueError as exc:
        return {"error": str(exc)}


@app.get("/mcp/prompts")
async def list_mcp_prompts():
    return {"prompts": get_mcp_prompt_definitions()}


@app.post("/mcp/prompts/{prompt_name}")
async def render_prompt(prompt_name: str, request: Request):
    payload = await request.json() if await request.body() else {}
    try:
        return render_mcp_prompt(prompt_name, payload.get("arguments") or {})
    except ValueError as exc:
        return {"error": str(exc)}
