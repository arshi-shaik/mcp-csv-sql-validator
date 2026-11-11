import pandas as pd
from sqlalchemy import create_engine, inspect

def check_csv_or_excel(file_path: str) -> str:
    try:
        df = pd.read_excel(file_path) if file_path.endswith((".xlsx", ".xls")) else pd.read_csv(file_path)
    except Exception as e:
        return f"Error reading file: {str(e)}"

    issues = []
    if df.empty:
        issues.append("The file is completely empty.")

    # Check for missing values
    null_counts = df.isnull().sum()
    for col, count in null_counts.items():
        if count > 0:
            issues.append(f"Column '{col}' has {count} missing/empty values.")

    # Check for exact duplicate rows
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        issues.append(f"Found {dup_count} duplicate rows.")

    if not issues:
        return f"SUCCESS: '{file_path}' passed all checks ({len(df)} rows, {len(df.columns)} columns)."
    return "VALIDATION ISSUES FOUND:\n- " + "\n- ".join(issues)

def check_sql_table(db_url: str, table_name: str) -> str:
    try:
        engine = create_engine(db_url)
        inspector = inspect(engine)
        if not inspector.has_table(table_name):
            return f"ERROR: Table '{table_name}' does not exist in the database."
        columns = [col["name"] for col in inspector.get_columns(table_name)]
        return f"SUCCESS: Table '{table_name}' exists with columns: {', '.join(columns)}"
    except Exception as e:
        return f"Database connection error: {str(e)}"
