from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# CORS to allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Show all columns in output
pd.set_option('display.max_columns', None)

# OR for direct online URL (e.g., from OneDrive, Dropbox)
file_path = "https://docs.google.com/spreadsheets/d/1yKx5o5sU47jmB8xXFkccDursyd5atwyk/export?format=xlsx"


# --- Load the Excel file ---
df = pd.read_excel(file_path ,engine='openpyxl')

# --- Search for a row by ID ---
@app.get("/search/{pr_id}")
def search_pr_id(pr_id: str):
    result = df[df["PR No"] == pr_id]
    if not result.empty:
        return result.to_dict(orient="records")
    return {"message": "ID not found"}



