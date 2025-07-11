from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS to allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Show all columns in output
pd.set_option('display.max_columns', None)

# OR for direct online URL (e.g., from OneDrive, Dropbox)
file_path = os.getenv("EXCEL_FILE_URL")


# --- Load the Excel file ---
df = pd.read_excel(file_path ,engine='openpyxl')

# --- Search for a row by ID ---
@app.get("/search/{pr_id}")
def search_pr_id(pr_id: str):
    try:
        df["PR No"] = df["PR No"].astype(str).str.strip().str.upper()
        pr_id = pr_id.strip().upper()
        result = df[df["PR No"] == pr_id]

        if not result.empty:
            clean_result = result.fillna("").to_dict(orient="records")
            return clean_result
        return {"message": "ID not found"}
    except Exception as e:
        print("Backend Error:", e)
        return {"message": "Internal server error"}




