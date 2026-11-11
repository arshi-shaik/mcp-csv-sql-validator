# mcp-csv-sql-validator

A lightweight **MCP (Model Context Protocol)** server built with Python that lets AI assistants (Claude Desktop, Cursor) validate CSV, Excel, and SQL database schemas before loading data.

## Features
* **CSV & Excel Auditing**: Detects empty files, missing/null values per column, and exact duplicate rows using Pandas.
* **SQL Schema Verification**: Inspects SQLite and PostgreSQL databases via SQLAlchemy to confirm table existence and list column structures.
* **Ready-to-Test Dataset**: Includes `sample_data.csv` with intentional errors so you can test validation right away.

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com
   cd mcp-csv-sql-validator
   ```

2. **Create a virtual environment and install dependencies**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run a quick test on the sample file**
   ```bash
   python -c "from validators import check_csv_or_excel; print(check_csv_or_excel('sample_data.csv'))"
   ```

## Connect to Claude Desktop or Cursor
Add this configuration to your client's `mcpServers` JSON file:

```json
{
  "mcpServers": {
    "csv-sql-validator": {
      "command": "C:\\Users\\YOUR_USERNAME\\mcp-csv-sql-validator\\venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\YOUR_USERNAME\\mcp-csv-sql-validator\\server.py"]
    }
  }
}
```
