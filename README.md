## 🔌 Model Context Protocol (MCP) Integration

This project demonstrates a lightweight MCP-style integration pattern for connecting a chatbot or LLM workflow to internal services without exposing raw databases directly. The example now includes an interactive student-loan assistant so you can see how a bot can guide users through eligibility, loan amount, and interest-rate questions.

### Architecture Flow
```text
[User Chat] <---> [LLM / Chatbot Core] <---> [MCP Client] <---(MCP Protocol)---> [Internal MCP Server] <---> [Secure DB / APIs]
```

### What this sample implements

The repository contains a minimal Python setup with four capabilities:

1. `get_daily_loan_metrics()`
   - Returns a simple demo metric for the current day.
   - Output: integer

2. `calculate_student_eligibility(course_type, income, country)`
   - Returns a simplified eligibility estimate with a maximum loan amount and baseline interest rate.
   - Output: JSON-like dictionary

3. `get_ux_bot_instructions(context)`
   - Returns guidance for a student-loan assistant in a specific scenario such as eligibility or rate questions.
   - Output: JSON-like dictionary

4. `run_interactive_ux_bot()`
   - Starts a simple command-line conversation loop where the student-loan UX bot responds based on the user’s question.

### Project Files

- [server.py](server.py) — implementation of the MCP-style tools and interactive bot loop
- [app.py](app.py) — FastAPI web app for the browser-based UX bot UI
- [templates/index.html](templates/index.html) — chat page layout
- [static/app.js](static/app.js) and [static/styles.css](static/styles.css) — frontend behavior and styling
- [test_server.py](test_server.py) — unit tests for the demo logic

### How to run

Run the sample implementation:

```bash
python server.py
```

Run the browser-based student-loan UX bot interface:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Then open:

```text
http://127.0.0.1:8000
```

Run the interactive student-loan UX bot from the terminal:

```bash
python
from server import run_interactive_ux_bot
run_interactive_ux_bot()
```

Example interaction:

```text
UX Bot interactive mode
Type 'checkout', 'support', or 'exit'.
You: checkout
UX Bot guidance for checkout:
Focus areas: clarity, trust, speed
Guidance: reduce friction; explain each step; confirm before payment
```

Run the tests:

```bash
python -m unittest -v
```

### Why this is useful

This pattern is valuable when you want an LLM or UX bot to interact with sensitive systems through a controlled interface. Instead of giving the model direct database access, you expose a small set of approved tools that return only the information needed for the task.
