import os
import pandas as pd
from sqlalchemy import text
from datetime import datetime

def export_views_as_csv(views_list, engine, output_dir="views"):
    """
    Exports a list of SQL views from a PostgreSQL database to timestamped CSV files.
    - Deletes existing files in the output directory (if any).
    - For each view name provided, fetches the data via SQL query and saves it as a CSV file.
    - Output filenames follow the format: <view_name>_<YYYY-MM-DD>.csv

    Parameter:
        views_list (list of str): List of SQL view names to export.
        engine (SQLAlchemy Engine): SQLAlchemy database engine for connecting to the database.
        output_dir (str, optional): Directory to store exported CSV files. Defaults to 'views'.

    Returns:
        None
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    output_path = os.path.join(project_root, output_dir)

    os.makedirs(output_path, exist_ok=True)
    
    for file in os.listdir(output_path):
        file_path = os.path.join(output_path, file)
        if os.path.isfile(file_path) and file.lower().endswith(".csv"):
            os.remove(file_path)

    timestamp = datetime.now().strftime("%Y-%m-%d")

    with engine.connect() as conn:
        for view in views_list:
            df = pd.read_sql(text(f"SELECT * FROM {view};"), conn)
            out_file = os.path.join(output_path, f"{view}_{timestamp}.csv")
            df.to_csv(out_file, index=False)