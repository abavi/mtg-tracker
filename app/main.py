from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome the the MTG Tracker App"}

@app.get("/health")
def health_check():
    return {"status": "Healthy!"}