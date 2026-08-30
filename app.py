# app.py — FastAPI wrapper for SUDARSHAN
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import subprocess
import os
import sys
from typing import Optional

app = FastAPI(
    title="SUDARSHAN API",
    description="Enterprise DAST Engine — 22 vulnerability rules",
    version="3.0.0"
)

class ScanRequest(BaseModel):
    target: str
    threads: int = 10
    report: str = "both"
    max_pages: int = 10

@app.get("/", response_class=HTMLResponse)
def root():
    """Serve the HTML interface"""
    html_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    if os.path.exists(html_file):
        with open(html_file, "r") as f:
            return f.read()
    return {"message": "SUDARSHAN API is running", "status": "online"}

@app.post("/scan")
def scan(request: ScanRequest):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        main_path = os.path.join(script_dir, "main.py")
        
        result = subprocess.run(
            [sys.executable, main_path,
             "--target", request.target,
             "--threads", str(request.threads),
             "--report", request.report,
             "--max-pages", str(request.max_pages)],
            capture_output=True,
            text=True,
            timeout=300,
            cwd=script_dir
        )
        
        return {
            "target": request.target,
            "output": result.stdout,
            "error": result.stderr if result.stderr else None,
            "status": "completed" if result.returncode == 0 else "failed"
        }
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=408, detail="Scan timed out after 300 seconds")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "healthy", "version": "3.0.0", "service": "SUDARSHAN"}
