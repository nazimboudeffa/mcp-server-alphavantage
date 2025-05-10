# MCP Server for Alpha Vantage

An MCP Server for Alpha Vantage

# Prerequisites

- Python 3.12+
- uv package manager
- MCP-compatible client (e.g., Claude for Desktop)

# Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/nazimboudeffa/mcp-server-alphavantage.git
   cd mcp-server-alphavantage
   ```

2. Install dependencies
    ```bash
    pip install uv
    uv add "mcp[cli]"
    ```

3. Create a .env file with your API KEY:
    ```
    API_KEY=demo
    ```

# Usage

Run

`uv run mcp install server.py`

Then check the Claude for Desktop config file

```json
{
  "mcpServers": {
    "alphavantage": {
      "command": "C:\\Users\\YOU_USERNAME\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\uv.EXE",
      "args": [
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "C:\\Users\\YOUR_USERNAME\\Documents\\GitHub\\mcp-server-alphavantage\\server.py"
      ]
    }
  }
}
```

