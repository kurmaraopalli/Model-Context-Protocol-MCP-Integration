## 🔌 Model Context Protocol (MCP) Integration

This bot utilizes the **Model Context Protocol (MCP)** to securely bridge the LLM core with our live financial databases and internal tracking services. 

### Architecture Flow
```text
[User Chat] <---> [LLM / Chatbot Core] <---> [MCP Client] <---(MCP Protocol)---> [Internal MCP Server] <---> [Secure DB / APIs]
```

### Exposed MCP Tools

The internal MCP server exposes the following standardized tools to the LLM:

1. `get_daily_loan_metrics()`
   * **Description:** Fetches the total volume of applications processed dynamically for the current calendar date.
   * **Output:** Integer (e.g., `184`)

2. `calculate_student_eligibility(course_type, income, country)`
   * **Description:** Evaluates backend risk models to return the maximum loan cap an individual can avail.
   * **Output:** JSON object with max amount and baseline interest rate.
