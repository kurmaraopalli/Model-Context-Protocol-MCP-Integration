from __future__ import annotations

from server import get_mcp_tool_definitions


if __name__ == "__main__":
    print("Student Loan MCP-style server prototype")
    print("Available tools:")
    for tool in get_mcp_tool_definitions():
        print(f"- {tool['name']}: {tool['description']}")
