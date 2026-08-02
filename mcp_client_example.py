import json

from server import invoke_mcp_tool


def main() -> None:
    request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "calculate_student_eligibility",
            "arguments": {
                "course_type": "engineering",
                "income": 35000,
                "country": "US",
            },
        },
    }

    if request["method"] != "tools/call":
        raise ValueError("Unsupported method")

    result = invoke_mcp_tool(request["params"]["name"], request["params"].get("arguments", {}))
    print(json.dumps({"jsonrpc": "2.0", "id": request["id"], "result": result}, indent=2))


if __name__ == "__main__":
    main()
