from mcp.server.mcpserver import MCPServer
from validators import check_csv_or_excel, check_sql_table

mcp = MCPServer("CSV SQL Validator")

@mcp.tool()
def validate_file(file_path: str) -> str:
    """Validate a CSV or Excel file for empty cells, missing data, and duplicate rows."""
    return check_csv_or_excel(file_path)

@mcp.tool()
def validate_sql_schema(db_url: str, table_name: str) -> str:
    """Inspect a SQL database table to verify it exists and list its columns."""
    return check_sql_table(db_url, table_name)

if __name__ == "__main__":
    mcp.run()
