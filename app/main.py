from fastapi import FastAPI
import uvicorn

from dotenv import load_dotenv
import os

from app.api.routes import router as api_router

app = FastAPI(
    title="Automated Tester API",
    description="API for generating automated test cases from UI images",
    version="1.0.0"
)

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

# Include routers
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Automated Tester API is running. Go to /docs for API documentation."}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)